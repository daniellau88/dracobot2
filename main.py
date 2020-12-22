from dotenv import load_dotenv
load_dotenv()

import logging
import os

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

from sqlalchemy import or_
from sqlalchemy.orm import scoped_session

from config import SessionLocal
from models import User, MsgFrom
from resources import *

from utils import SUPPORTED_MESSAGE_FILTERS, forward_message, delete_message, handle_edited_message, format_registered_message

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

UNREGISTERED, MAIN, CHAT, CHAT_LOGIN, DRAGON_CHAT, TRAINER_CHAT = range(6)

KEYBOARD_OPTIONS = [[DRAGON_CHAT_KEY], [TRAINER_CHAT_KEY], [HELP_KEY, STATUS_KEY], [ABOUT_THE_BOT_KEY, RULES_KEY]]

Session = scoped_session(SessionLocal)

def db_session(method):
    def db_session_decorator(update, context):
        session = Session()
        return_value = method(update, context, session=session)
        session.close()
        return return_value
    return db_session_decorator

@db_session
@handle_edited_message
def start(update, context, session):
    chat_id = update.message.chat_id
    user = update.message.from_user

    user_db = session.query(User).filter(or_(User.tele_handle==user.username, User.chat_id==chat_id)).first()

    if user_db is not None:
        is_new_user = not user_db.registered

        if user_db.chat_id != chat_id:
            user_db.chat_id = chat_id
        if not user_db.registered:
            user_db.registered = True

        user_db.tele_handle = user.username
        user_db.tele_name = user.first_name

        session.commit()

        if is_new_user:
            update.message.reply_text(WELCOME_MESSAGE % user.first_name)

        update.message.reply_text(HELLO_GREETING.format(user.first_name),
            reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

        return MAIN
    else:
        update.message.reply_text(USER_UNREGISTERED)

        if user.username is None:
            update.message.reply_text(USER_NO_TELE_HANDLE)

        return UNREGISTERED

def about(update, context):
    update.message.reply_text(ABOUT_THE_BOT, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

    return MAIN

def helps(update, context):
    user = update.message.from_user
    update.message.reply_text(HELP_MESSAGE.format(user.first_name), reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

    return MAIN

def rules(update, context):
    update.message.reply_text(GAME_RULES_MESSAGE, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

    return MAIN

@db_session
def check_trainer(update, context, session):
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(User.chat_id==chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id==cur_user_id).first()

    if trainer is None:
        update.message.reply_text(USER_NO_TRAINER, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))
        return MAIN
    elif not trainer.registered:
        update.message.reply_text(USER_UNREGISTERED_TRAINER, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))
        return MAIN
    else:
        update.message.reply_text(SUCCESSFUL_TRAINER_CONNECTION)
        return TRAINER_CHAT

@db_session
def check_dragon(update, context, session):
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(User.chat_id==chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id==dragon_id).first()

    if dragon is None:
        update.message.reply_text(USER_NO_DRAGON, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))
        return MAIN
    elif not dragon.registered:
        update.message.reply_text(USER_UNREGISTERED_DRAGON, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))
        return MAIN
    else:
        update.message.reply_text(SUCCESSFUL_DRAGON_CONNECTION)
        return DRAGON_CHAT

@db_session
@handle_edited_message
def send_trainer(update, context, session):
    user = update.message.from_user
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(User.chat_id==chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id==cur_user_id).first()

    if trainer is not None:
        forward_message(update.message, trainer.chat_id, context.bot, session, message_from=MsgFrom.DRAGON)
        return TRAINER_CHAT
    else:
        update.message.reply_text(SEND_CONNECTION_FAILED, reply_markup=ReplyKeyboardRemove())
        return MAIN

@db_session
@handle_edited_message
def send_dragon(update, context, session):
    user = update.message.from_user
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(User.chat_id==chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id==dragon_id).first()

    if dragon is not None:
        forward_message(update.message, dragon.chat_id, context.bot, session, message_from=MsgFrom.TRAINER)
        return DRAGON_CHAT
    else:
        update.message.reply_text(SEND_CONNECTION_FAILED, reply_markup=ReplyKeyboardRemove())
        return MAIN

@db_session
@handle_edited_message
def main_edited_message(update, context, session):
    return MAIN

def handle_delete_message(return_state):
    @db_session
    def inner_handle_delete_message(update, context, session):
        delete_message(update.message, context.bot, session)
        return return_state
    return inner_handle_delete_message

def unsupported_media(return_state):
    def inner_unsupported_media(update, context):
        update.message.reply_text(UNSUPPORTED_MEDIA, reply_to_message_id=update.message.message_id, reply_markup=ReplyKeyboardRemove())
        return return_state
    return inner_unsupported_media

def done_chat(update, context):
    update.message.reply_text(CHAT_COMPLETE, reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

    return MAIN

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)

    return start(update, context)

@db_session
def status(update, context, session):
    user = update.message.from_user

    chat_id = update.message.chat_id
    cur_user = session.query(User).filter(User.chat_id==chat_id).first()

    trainer = session.query(User).filter(User.dragon_id==cur_user.id).first()
    dragon = session.query(User).filter(User.id==cur_user.dragon_id).first()


    t_registered = format_registered_message(trainer)
    d_registered = format_registered_message(dragon)

    update.message.reply_text(STATUS.format(t_registered, d_registered), reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

    return MAIN

NON_COMMAND_REGEX = u'^[^\/]'

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.all, start)],

        states={
            UNREGISTERED: [MessageHandler(Filters.all, start)],

            MAIN: [CommandHandler(MENU_KEY, start),
                    CommandHandler(DELETE_KEY, handle_delete_message(MAIN)),
                    MessageHandler(Filters.regex(ABOUT_THE_BOT_KEY), about),
                    MessageHandler(Filters.regex(HELP_KEY), helps),
                    MessageHandler(Filters.regex(RULES_KEY), rules),
                    MessageHandler(Filters.regex(STATUS_KEY), status),
                    MessageHandler(Filters.regex(DRAGON_CHAT_KEY), check_dragon),
                    MessageHandler(Filters.regex(TRAINER_CHAT_KEY), check_trainer),
                    CommandHandler(DRAGON_KEY, check_dragon),
                    CommandHandler(TRAINER_KEY, check_trainer),
                    MessageHandler(SUPPORTED_MESSAGE_FILTERS, main_edited_message)],

            # Chat with dragon
            DRAGON_CHAT: [CommandHandler(MENU_KEY, start),
                            CommandHandler(DONE_KEY, done_chat),
                            CommandHandler(DELETE_KEY, handle_delete_message(DRAGON_CHAT)),
                            MessageHandler(SUPPORTED_MESSAGE_FILTERS, send_dragon),
                            MessageHandler(~SUPPORTED_MESSAGE_FILTERS, unsupported_media(DRAGON_CHAT))],

            # Chat with trainer
            TRAINER_CHAT: [CommandHandler(MENU_KEY, start),
                            CommandHandler(DONE_KEY, done_chat),
                            CommandHandler(DELETE_KEY, handle_delete_message(TRAINER_CHAT)),
                            MessageHandler(SUPPORTED_MESSAGE_FILTERS, send_trainer),
                            MessageHandler(~SUPPORTED_MESSAGE_FILTERS, unsupported_media(TRAINER_CHAT))],
        },

        fallbacks=[CommandHandler(CANCEL_KEY, cancel)]
    )

    dp.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info("Initialised....")
    logger.info("Starting main()...")
    main()