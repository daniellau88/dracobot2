from dotenv import load_dotenv
load_dotenv()

import logging
import os

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

from sqlalchemy import or_

from config import SessionLocal
from models import User, MsgFrom
from resources import *

from utils import SUPPORTED_MESSAGE_FILTERS, forward_message, delete_message, handle_edited_message

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

UNREGISTERED, MAIN, CHAT, CHAT_LOGIN, DRAGON_CHAT, TRAINER_CHAT = range(6)

KEYBOARD_OPTIONS = [[DRAGON_CHAT_KEY], [TRAINER_CHAT_KEY], [HELP_KEY], [ABOUT_THE_BOT_KEY, RULES_KEY]]

session = SessionLocal()

def start(update, context):
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
            pass

        update.message.reply_text(HELLO_GREETING.format(user.first_name),
            reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

        return MAIN
    else:
        # Updates session
        session.commit()

        update.message.reply_text(UNREGISTERED_USER)

        if user.username is None:
            update.message.reply_text(USER_NO_TELE_HANDLE)

        return UNREGISTERED

def about(update, context):
    update.message.reply_text(ABOUT_THE_BOT, reply_markup=ReplyKeyboardRemove())

    return start(update, context)

def helps(update, context):
    user = update.message.from_user

    update.message.reply_text(HELP_MESSAGE.format(user.first_name), reply_markup=ReplyKeyboardRemove())

    return start(update, context)

def rules(update, context):
    update.message.reply_text(GAME_RULES_MESSAGE, reply_markup=ReplyKeyboardRemove())

    return start(update, context)

def check_trainer(update, context):
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(User.chat_id==chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id==cur_user_id).first()

    if trainer is None:
        update.message.reply_text(USER_NO_TRAINER)
        return MAIN
    elif not trainer.registered:
        update.message.reply_text(USER_UNREGISTERED_TRAINER)
        return MAIN
    else:
        update.message.reply_text(CONNECTED_TRAINER)
        return TRAINER_CHAT

def check_dragon(update, context):
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(User.chat_id==chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id==dragon_id).first()

    if dragon is None:
        update.message.reply_text(USER_NO_DRAGON)
        return MAIN
    elif not dragon.registered:
        update.message.reply_text(USER_UNREGISTERED_DRAGON)
        return MAIN
    else:
        update.message.reply_text(CONNECTED_DRAGON)
        return DRAGON_CHAT

@handle_edited_message(session)
def send_trainer(update, context):
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

@handle_edited_message(session)
def send_dragon(update, context):
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

@handle_edited_message(session)
def main_edited_message(update, context):
    return MAIN

def handle_delete_message(return_state):
    def inner_handle_delete_message(update, context):
        delete_message(update.message, context.bot, session)
        return return_state
    return inner_handle_delete_message

def unsupported_media(return_state):
    def inner_unsupported_media(update, context):
        update.message.reply_text(UNSUPPORTED_MEDIA, reply_to_message_id=update.message.message_id, reply_markup=ReplyKeyboardRemove())
        return return_state
    return inner_unsupported_media

def done_chat(update, context):
    update.message.reply_text(CHAT_COMPLETE, reply_markup=ReplyKeyboardRemove())

    return MAIN

def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)

    return start(update, context)

NON_COMMAND_REGEX = u'^[^\/]'

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler(START_KEY, start)],

        states={
            UNREGISTERED: [CommandHandler(START_KEY, start)],

            MAIN: [CommandHandler(MENU_KEY, start),
                    CommandHandler(DELETE_KEY, handle_delete_message(MAIN)),
                    MessageHandler(Filters.regex(ABOUT_THE_BOT_KEY), about),
                    MessageHandler(Filters.regex(HELP_KEY), helps),
                    MessageHandler(Filters.regex(RULES_KEY), rules),
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