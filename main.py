from dotenv import load_dotenv
load_dotenv()

import logging
import os

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)

from dbhelper import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

MAIN, CHAT, CHAT_LOGIN, DRAGON_CHAT, TRAINER_CHAT = range(5)

user_db = userdb()
am_db = amdb()

# EMOJI UNICODE
CAKE = u"\U0001F382"
WHALE = u"\U0001F40B"
ROBOT = u"\U0001F916"
SKULL = u"\U0001F480"
SMILEY = u"\U0001F642"
SPOUTING_WHALE = u"\U0001F433"
SPEECH_BUBBLE = u"\U0001F4AC"
THINKING_FACE = u"\U0001F914"
QUESTION_MARK = u"\U0001F64F"
MONKEY = u"\U0001F64A"
DRAGON = u"\U0001F432" #In use for Dragon Trainer Bot
BLUE_HEART = u"\U0001F499"

# TELEGRAM KEYBOARD KEYS
ABOUT_THE_BOT_KEY = u"About the Bot" + " " + DRAGON
ADMIN_KEY = u"admin"
ANONYMOUS_CHAT_KEY = u"Dragon-Trainer Anonymous Chat" + " " + SPEECH_BUBBLE
HELP_KEY = u"Help" + " " + QUESTION_MARK
RULES_KEY = u"Rules" + " " + MONKEY
MENU_KEY = u"mainmenu"
TRAINER_KEY = u"trainer"
DRAGON_KEY = u"dragon"
SEND_ALL_KEY = u"Send_All"
SEND_ONE_KEY = u"Send_One"
CHECK_REGIS_KEY = u"Check_Player_Registration"
DONE_KEY = u"done"

# GREETINGS
ABOUT_THE_BOT = DRAGON + " *About DracoBot* " + DRAGON + "\n\n" + CAKE + " Birthday: June 2017\n\n" +\
                ROBOT + " Currently maintained by Ji Cheng and Daniel Lau\n\n" + SKULL +\
                " Past Bot Developers: Shao Yi, Bai Chuan, Fiz, Youkuan, Kang Ming, Zhi Yu\n\n"
AM_GREETING = "Hello there, {}!\n\n" +\
              "Click or type any of the following:\n" +\
              "/trainer: Chat with your Trainer\n" +\
              "/dragon: Chat with your Dragon\n" +\
              "/mainmenu: Exits the Chat feature, and returns to the Main Menu"

AM_LOGIN_GREETING = "Please enter your 4-character Game ID. (Remember Caps!)\n\n" +\
                     "or click /mainmenu to exit the registration process"
INVALID_PIN = "You have entered the wrong 4-character Game ID. Please try again, or type /mainmenu to exit."
REDIRECT_GREETING = "Did you mean: /mainmenu"
REQUEST_ADMIN_ID = "Please enter your Admin ID to proceed."
SEND_ADMIN_GREETING = "Hello there, Administrator! What do you want to say to everyone?\n" +\
                      "Whatever you submit from now on will be broadcasted to all users, be CAREFUL!" +\
                      "Type /mainmenu to exit, once you have made your announcement."
SEND_CONNECTION_FAILED = u"This feature is unavailable now as he/she has yet to sign in to the game." +\
                         u" Please be patient and try again soon!" + SMILEY + "\n\nType /mainmenu to go back."
SUCCESSFUL_TRAINER_CONNECTION = "You have been connected with your Trainer." +\
                            " Anything you type here will be sent anonymously to him/her.\n" +\
                            "To exit, type /done"
SUCCESSFUL_DRAGON_CONNECTION = "You have been connected with your Dragon." +\
                               " Anything you type here will be sent anonymously to him/her.\n" +\
                               "To exit, type /done"
HELLO_GREETING = "Hello there, {}! DracoBot at your service! Press /mainmenu to bring up keyboard! " + DRAGON
HELP_MESSAGE = "Hello there, {}!\n\n" +\
               "Dragon Trainer Bot is a homegrown telegram bot that allows you to anonymously chat with your Dragon or Trainer.\n\n" +\
               "While in the Main Menu, click on:\n" +\
               ANONYMOUS_CHAT_KEY + ": To chat with your Dragon or Trainer\n" +\
               ABOUT_THE_BOT_KEY + ": To view information about the bot\n" +\
               HELP_KEY + ": To explore this bot's functionality\n" +\
               RULES_KEY + ": To view the game rules\n\n" +\
               "While in the Chat feature, type any of the following to:\n" +\
               TRAINER_KEY + ": Chat with your Trainer\n" +\
               DRAGON_KEY + ": Chat with your Dragon\n\n" +\
               "Type " + MENU_KEY + " at any point in time to exit the Chat feature, and return to the Main Menu\n\n" +\
               "Please message @JichNgan @dlau98 if you need technical assistance!\n" +\
               "Thank you and we hope you'll have fun throughout this game! :)"
GAME_RULES_MESSAGE = "Rules of Dragons and Trainers" + DRAGON + "\n\n" +\
                     "Each of you who participated will be assigned an Angel (Trainer) and a Mortal (Dragon). " +\
                     "Of course, you will know the identity of your Dragon while your Trainer’s identity will be kept " +\
                     "from you. Throughout the course of the event, feel free to chat with both your Dragon and Trainer " +\
                     "through telegram bot where your identity will be kept secret, and take care of your dragonwith " +\
                     "anonymous gift and pranks according to their indicated tolerance levels! " +\
                     "Of course, you can look forward to seeing what your own trainer does for you as well!\n\n" +\
                     "Explanation for tolerance levels\n\n" +\
                     "1: Gift Exchange, do nice things only!\n" +\
                     "2: Pranks are to be minimal, and no clean up required!\n" +\
                     "3: Pranks are fine, but do take care of what your dragon says is OFF LIMITS\n\n" +\
                     "Dos :)\n" +\
                     "• Observe the Tolerance Levels your dragons have indicated.\n" +\
                     "• Try to accommodate (if any) requests of your dragons e.g. avoid allergies\n" +\
                     "• Balance out the pranks with gifts - moderation is key!\n" +\
                     "• Try (your best) to keep your identity hidden.\n" +\
                     "• Be active in the event! :)\n" +\
                     "• Share your pranks and gifts throughout the event in the Draco group chat!\n\n" +\
                     "Don'ts :(\n" +\
                     "• Cause major damage (eg. breaking a treasured object) even if they’ve indicated no boundaries.\n" +\
                     "• Flout other RC/NUS rules (e.g. theft, possession of alcohol *ahem ahem*).\n" +\
                     "• Cause major inconveniences, especially along the common corridor" +\
                     "(e.g. blockade the walkway, pranks involving powdered substances like flour or curry powder).\n" +\
                     "• Cause fire hazards and hinder evacuation routes.\n" +\
                     "• Write, draw or scribble any obscene/vulgar contents on doors/common area.\n\n" +\
                     "**IMPORTANT!**\n\n" +\
                     "NO LIVE ANIMALS OR INSECTS\n" +\
                     "NO MOVING OF FURNITURE OUT OF THE ROOMS\n\n" +\
                     "If you have any other questions, concerns or doubts, don’t be afraid to reach out to the" +\
                     " organizing comm! We hope you have fun and make new friends as well!\n\n" +\
                     "Love,\n" +\
                     "Draco House Comm" + BLUE_HEART

KEYBOARD_OPTIONS = [[ANONYMOUS_CHAT_KEY], [ABOUT_THE_BOT_KEY], [HELP_KEY], [RULES_KEY]]

DT1 = ['ABCD', 'BCDE', 'CDEF']
DT2 = []
DT3 = []
DT4 = []
DT5 = []
DT6 = []
DT7 = []
DT8 = []
DT9 = []

DT = [DT1, DT2, DT3, DT4, DT5, DT6, DT7, DT8, DT9]

DRAGON_LIST = {}
TRAINER_LIST = {}

for dt_list in DT:
    for i in range(0, len(dt_list)):
        DRAGON_LIST[dt_list[i - 1]] = dt_list[i]
        TRAINER_LIST[dt_list[i]] = dt_list[i - 1]

def start(update, context):
    user = update.message.from_user

    update.message.reply_text(HELLO_GREETING.format(user.first_name),
        reply_markup=ReplyKeyboardMarkup(KEYBOARD_OPTIONS, one_time_keyboard=True))

    return MAIN

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

def anonymous_chat(update, context):
    user = update.message.from_user
    existing_user = am_db.get_user_record_from_user_chat_id(user.id)

    if existing_user is not None:
        update.message.reply_text(AM_GREETING.format(user.first_name), reply_markup=ReplyKeyboardRemove())
        return CHAT
    else:
        update.message.reply_text(AM_LOGIN_GREETING.format(user.first_name), reply_markup=ReplyKeyboardRemove())
        return CHAT_LOGIN

def trainer(update, context):
    update.message.reply_text(SUCCESSFUL_TRAINER_CONNECTION, reply_markup=ReplyKeyboardRemove())

    user = update.message.from_user
    existing_user = am_db.get_user_record_from_user_chat_id(user.id)
    game_id = existing_user[1]
    
    if game_id in TRAINER_LIST:
        trainer_game_id = TRAINER_LIST[game_id]
        trainer_user = am_db.get_user_record_from_game_id(trainer_game_id)
        if trainer_user is not None:
            update.message.reply_text(SUCCESSFUL_TRAINER_CONNECTION, reply_markup=ReplyKeyboardRemove())
            return TRAINER_CHAT

    update.message.reply_text(SEND_CONNECTION_FAILED, reply_markup=ReplyKeyboardRemove())
    return anonymous_chat(update, context)

def dragon(update, context):
    user = update.message.from_user
    existing_user = am_db.get_user_record_from_user_chat_id(user.id)
    game_id = existing_user[1]
    
    if game_id in DRAGON_LIST:
        dragon_game_id = DRAGON_LIST[game_id]
        dragon_user = am_db.get_user_record_from_game_id(dragon_game_id)
        if dragon_user is not None:
            update.message.reply_text(SUCCESSFUL_DRAGON_CONNECTION, reply_markup=ReplyKeyboardRemove())
            return DRAGON_CHAT

    update.message.reply_text(SEND_CONNECTION_FAILED, reply_markup=ReplyKeyboardRemove())
    return anonymous_chat(update, context)

def send_trainer(update, context):
    user = update.message.from_user
    existing_user = am_db.get_user_record_from_user_chat_id(user.id)
    game_id = existing_user[1]
    
    if game_id in TRAINER_LIST:
        trainer_game_id = TRAINER_LIST[game_id]
        # TODO: Cache DB
        trainer_user = am_db.get_user_record_from_game_id(trainer_game_id)
        trainer_id = trainer_user[2]

        if trainer_user is not None:
            context.bot.send_message(chat_id=trainer_id, text="From your Trainer:\n" + update.message.text)
            return TRAINER_CHAT

    update.message.reply_text(SEND_CONNECTION_FAILED, reply_markup=ReplyKeyboardRemove())
    return CHAT

def send_dragon(update, context):
    user = update.message.from_user
    existing_user = am_db.get_user_record_from_user_chat_id(user.id)
    game_id = existing_user[1]
    
    if game_id in DRAGON_LIST:
        dragon_game_id = DRAGON_LIST[game_id]
        # TODO: Cache DB
        dragon_user = am_db.get_user_record_from_game_id(dragon_game_id)
        dragon_id = dragon_user[2]

        if dragon_user is not None:
            context.bot.send_message(chat_id=dragon_id, text="From your Dragon:\n" + update.message.text)
            return DRAGON_CHAT

    update.message.reply_text(SEND_CONNECTION_FAILED, reply_markup=ReplyKeyboardRemove())
    return CHAT

def done_chat(update, context):
    update.message.reply_text("Done chatting", reply_markup=ReplyKeyboardRemove())

    return anonymous_chat(update, context)

def register(update, context):
    user = update.message.from_user
    user_pin = update.message.text
    if user_pin in DRAGON_LIST and user_pin in TRAINER_LIST:
        am_db.register(user_pin, user.id, user.first_name)
        update.message.reply_text(AM_GREETING.format(user.first_name), reply_markup=ReplyKeyboardRemove())
        return CHAT

    update.message.reply_text(INVALID_PIN, reply_markup=ReplyKeyboardRemove())
    return CHAT_LOGIN

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

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            MAIN: [CommandHandler(MENU_KEY, start), 
                    MessageHandler(Filters.regex(ABOUT_THE_BOT_KEY), about),
                    MessageHandler(Filters.regex(HELP_KEY), helps),
                    MessageHandler(Filters.regex(RULES_KEY), rules),
                    MessageHandler(Filters.regex(ANONYMOUS_CHAT_KEY), anonymous_chat)],

            CHAT: [CommandHandler(DRAGON_KEY, dragon),
                    CommandHandler(TRAINER_KEY, trainer),
                    CommandHandler(MENU_KEY, start)],

            CHAT_LOGIN: [MessageHandler(Filters.regex(NON_COMMAND_REGEX), register)],

            # Chat with dragon
            DRAGON_CHAT: [CommandHandler(MENU_KEY, start), 
                            CommandHandler(DONE_KEY, done_chat),
                            MessageHandler(Filters.regex(NON_COMMAND_REGEX), send_dragon)],

            # Chat with trainer
            TRAINER_CHAT: [CommandHandler(MENU_KEY, start), 
                            CommandHandler(DONE_KEY, done_chat),
                            MessageHandler(Filters.regex(NON_COMMAND_REGEX), send_trainer)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
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
    user_db.setup()
    logger.info("User database set up done.")
    am_db.setup()
    logger.info("AM database set up done.")
    logger.info("Starting main()...")
    main()