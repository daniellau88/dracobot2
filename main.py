from dracobot2.utils import SUPPORTED_MESSAGE_FILTERS, forward_message, handle_edited_message, format_registered_message, delete_message, delete_message_reply
from dracobot2.resources import *
from dracobot2.models import User, MsgFrom
from dracobot2.config import SessionLocal
from sqlalchemy.orm import scoped_session
from sqlalchemy import or_
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import os
import logging
from dotenv import load_dotenv
load_dotenv()


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

UNREGISTERED, MAIN, CHAT, CHAT_LOGIN, DRAGON_CHAT, TRAINER_CHAT, ADMIN_CHAT = range(
    7)

KEYBOARD_OPTIONS = [[DRAGON_CHAT_KEY], [TRAINER_CHAT_KEY],
                    [HELP_KEY, STATUS_KEY], [RULES_KEY, ABOUT_THE_BOT_KEY]]
DEFAULT_REPLY_MARKUP = {'reply_markup': ReplyKeyboardMarkup(
    KEYBOARD_OPTIONS, one_time_keyboard=True)}
REMOVE_REPLY_MARKUP = {'reply_markup': ReplyKeyboardRemove()}

Session = scoped_session(SessionLocal)


def db_session(method):
    def db_session_decorator(update, context):
        session = Session()
        return_value = method(update, context, session)
        session.close()
        return return_value
    return db_session_decorator


@db_session
@handle_edited_message
def start(update, context, session):
    chat_id = update.message.chat_id
    user = update.message.from_user

    user_db = session.query(User).filter(
        or_(User.tele_handle == user.username, User.chat_id == chat_id)).first()

    if user_db is not None:
        is_new_user = not user_db.registered

        if user_db.chat_id != chat_id:
            user_db.chat_id = chat_id
        if not user_db.registered:
            user_db.registered = True

        user_db.tele_handle = user.username
        user_db.tele_name = user.first_name

        if is_new_user:
            dragon = user_db.dragon
            if dragon and dragon.details and user_db.details:
                update.message.reply_text(WELCOME_MESSAGE.format(**{
                    'name': user_db.details.name,
                    'dragon_name': dragon.details.name,
                    'dragon_room_number': dragon.details.room_number,
                    'dragon_likes': dragon.details.likes,
                    'dragon_dislikes': dragon.details.dislikes,
                    'dragon_requests': dragon.details.requests,
                    'dragon_level': dragon.details.level
                }))
            else:
                update.message.reply_text(USER_NO_DRAGON)

        session.commit()

        update.message.reply_text(HELLO_GREETING.format(
            user.first_name), **DEFAULT_REPLY_MARKUP)

        return MAIN
    else:
        update.message.reply_text(USER_UNREGISTERED)

        if user.username is None:
            update.message.reply_text(USER_NO_TELE_HANDLE)

        return UNREGISTERED


def about(update, context):
    update.message.reply_text(ABOUT_THE_BOT, **DEFAULT_REPLY_MARKUP)

    return MAIN


def helps(update, context):
    user = update.message.from_user
    update.message.reply_text(HELP_MESSAGE.format(
        user.first_name), **DEFAULT_REPLY_MARKUP)

    return MAIN


def rules(update, context):
    update.message.reply_text(GAME_RULES_MESSAGE, **DEFAULT_REPLY_MARKUP)

    return MAIN


@db_session
def check_trainer(update, context, session):
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(
        User.chat_id == chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id == cur_user_id).first()

    if trainer is None:
        update.message.reply_text(USER_NO_TRAINER, **DEFAULT_REPLY_MARKUP)
        return MAIN
    elif not trainer.registered:
        update.message.reply_text(
            USER_UNREGISTERED_TRAINER, **DEFAULT_REPLY_MARKUP)
        return MAIN
    else:
        update.message.reply_text(
            TRAINER_CONNECTION_SUCCESS, **REMOVE_REPLY_MARKUP)
        return TRAINER_CHAT


@db_session
def check_dragon(update, context, session):
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(
        User.chat_id == chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id == dragon_id).first()

    if dragon is None:
        update.message.reply_text(USER_NO_DRAGON, **DEFAULT_REPLY_MARKUP)
        return MAIN
    elif not dragon.registered:
        update.message.reply_text(
            USER_UNREGISTERED_DRAGON, **DEFAULT_REPLY_MARKUP)
        return MAIN
    else:
        update.message.reply_text(
            DRAGON_CONNECTION_SUCCESS, **REMOVE_REPLY_MARKUP)
        return DRAGON_CHAT


@db_session
def check_admin(update, context, session):
    chat_id = update.message.chat_id
    user_db = session.query(User).filter(
        User.chat_id == chat_id).first()

    if user_db and user_db.is_admin:
        update.message.reply_text(ADMIN_GREETING)
        return ADMIN_CHAT

    update.message.reply_text(UNKNOWN_COMMAND)
    return MAIN


@db_session
@handle_edited_message
def send_trainer(update, context, session):
    user = update.message.from_user
    chat_id = update.message.chat_id
    cur_user_id = session.query(User).filter(
        User.chat_id == chat_id).first().id

    trainer = session.query(User).filter(User.dragon_id == cur_user_id).first()

    if trainer is not None:
        forward_message(update.message, trainer.chat_id,
                        context.bot, session, message_from=MsgFrom.DRAGON)
        return TRAINER_CHAT
    else:
        update.message.reply_text(CONNECTION_ERROR, **REMOVE_REPLY_MARKUP)
        return MAIN


@db_session
@handle_edited_message
def send_dragon(update, context, session):
    user = update.message.from_user
    chat_id = update.message.chat_id
    dragon_id = session.query(User).filter(
        User.chat_id == chat_id).first().dragon_id

    dragon = session.query(User).filter(User.id == dragon_id).first()

    if dragon is not None:
        forward_message(update.message, dragon.chat_id,
                        context.bot, session, message_from=MsgFrom.TRAINER)
        return DRAGON_CHAT
    else:
        update.message.reply_text(CONNECTION_ERROR, **REMOVE_REPLY_MARKUP)
        return MAIN


@db_session
@handle_edited_message
def send_admin(update, context, session):
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_db = session.query(User).filter(User.chat_id == chat_id).first()

    if not user_db.is_admin:
        return MAIN

    all_users = session.query(User).filter(User.registered == True).all()

    for to_send_user in all_users:
        if to_send_user.id != user_db.id:
            forward_message(update.message, to_send_user.chat_id,
                            context.bot, session, message_from=MsgFrom.ADMIN)

    return ADMIN_CHAT


@db_session
@handle_edited_message
def main_edited_message(update, context, session):
    update.message.reply_text(UNKNOWN_COMMAND)

    return MAIN


def handle_delete_message(return_state):
    @db_session
    def inner_handle_delete_message(update, context, session):
        delete_message_reply(update.message, context.bot, session)
        return return_state
    return inner_handle_delete_message


@db_session
def delete_admin(update, context, session):
    if len(context.args) == 2:
        chat_id, message_id = context.args
        delete_message(update.message, message_id,
                       chat_id, None, context.bot, session)
    else:
        delete_message_reply(update.message, context.bot, session)
    return ADMIN_CHAT


def unsupported_media(return_state):
    def inner_unsupported_media(update, context):
        update.message.reply_text(
            UNSUPPORTED_MEDIA, reply_to_message_id=update.message.message_id, reply_markup=ReplyKeyboardRemove())
        return return_state
    return inner_unsupported_media


def done_chat(update, context):
    update.message.reply_text(CHAT_COMPLETE, **DEFAULT_REPLY_MARKUP)

    return MAIN


def cancel(update, context):
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)

    return start(update, context)


@db_session
def status(update, context, session):
    user = update.message.from_user

    chat_id = update.message.chat_id
    cur_user = session.query(User).filter(User.chat_id == chat_id).first()

    trainer = session.query(User).filter(User.dragon_id == cur_user.id).first()
    dragon = session.query(User).filter(User.id == cur_user.dragon_id).first()

    dragon_details = None
    if dragon and dragon.details:
        dragon_details = {
            'name': dragon.details.name,
            'likes': dragon.details.likes,
            'dislikes': dragon.details.dislikes,
            'room_number': dragon.details.room_number,
            'requests': dragon.details.requests,
            'level': dragon.details.level
        }

    t_registered = format_registered_message(trainer)
    d_registered = format_registered_message(dragon)

    message = STATUS.format(**{
        'trainer_status': t_registered,
        'dragon_status': d_registered
    })

    if dragon_details is not None:
        message += '\n' + DRAGON_DETAILS.format(**dragon_details)

    update.message.reply_text(message, **DEFAULT_REPLY_MARKUP)

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
                   MessageHandler(Filters.regex(
                       DRAGON_CHAT_KEY), check_dragon),
                   MessageHandler(Filters.regex(
                       TRAINER_CHAT_KEY), check_trainer),
                   CommandHandler(DRAGON_KEY, check_dragon),
                   CommandHandler(TRAINER_KEY, check_trainer),
                   CommandHandler(ADMIN_KEY, check_admin),
                   MessageHandler(SUPPORTED_MESSAGE_FILTERS, main_edited_message)],

            # Chat with dragon
            DRAGON_CHAT: [CommandHandler(MENU_KEY, start),
                          CommandHandler(DONE_KEY, done_chat),
                          CommandHandler(
                              DELETE_KEY, handle_delete_message(DRAGON_CHAT)),
                          MessageHandler(
                              SUPPORTED_MESSAGE_FILTERS, send_dragon),
                          MessageHandler(~SUPPORTED_MESSAGE_FILTERS, unsupported_media(DRAGON_CHAT))],

            # Chat with trainer
            TRAINER_CHAT: [CommandHandler(MENU_KEY, start),
                           CommandHandler(DONE_KEY, done_chat),
                           CommandHandler(
                               DELETE_KEY, handle_delete_message(TRAINER_CHAT)),
                           MessageHandler(
                               SUPPORTED_MESSAGE_FILTERS, send_trainer),
                           MessageHandler(~SUPPORTED_MESSAGE_FILTERS, unsupported_media(TRAINER_CHAT))],

            ADMIN_CHAT: [CommandHandler(MENU_KEY, start),
                         CommandHandler(DONE_KEY, done_chat),
                         CommandHandler(DELETE_KEY, delete_admin),
                         MessageHandler(SUPPORTED_MESSAGE_FILTERS, send_admin),
                         MessageHandler(~SUPPORTED_MESSAGE_FILTERS, unsupported_media(ADMIN_CHAT))],
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
