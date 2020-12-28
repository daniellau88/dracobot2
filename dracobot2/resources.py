# EMOJI UNICODE
CAKE_EMOJI = u"\U0001F382"
ROBOT_EMOJI = u"\U0001F916"
SKULL_EMOJI = u"\U0001F480"
SMILEY_EMOJI = u"\U0001F642"
HELP_EMOJI = u"\U0001F64F"
MONKEY_EMOJI = u"\U0001F64A"
DRAGON_EMOJI = u"\U0001F432"  # In use for Dragon Trainer Bot
TRAINER_EMOJI = u"\U0001F3CB"
BLUE_HEART_EMOJI = u"\U0001F499"
GREEN_STATUS_EMOJI = u"\U0001F7E2"
RED_STATUS_EMOJI = u"\U0001F534"
CROSS_EMOJI = u"\U0000274C"

WHALE_EMOJI = u"\U0001F40B"
SPOUTING_WHALE_EMOJI = u"\U0001F433"
SPEECH_BUBBLE_EMOJI = u"\U0001F4AC"
THINKING_FACE_EMOJI = u"\U0001F914"

# TELEGRAM KEYBOARD KEYS
ABOUT_THE_BOT_KEY = u"About the Bot" + " " + DRAGON_EMOJI
ADMIN_KEY = u"admin"
DRAGON_CHAT_KEY = u"Chat with Dragon" + " " + DRAGON_EMOJI
TRAINER_CHAT_KEY = u"Chat with Trainer" + " " + TRAINER_EMOJI
STATUS_KEY = u"Status" + " " + GREEN_STATUS_EMOJI
HELP_KEY = u"Help" + " " + HELP_EMOJI
RULES_KEY = u"Rules" + " " + MONKEY_EMOJI
MENU_KEY = u"menu"
TRAINER_KEY = u"trainer"
DRAGON_KEY = u"dragon"
START_KEY = u"start"
DELETE_KEY = u"delete"
CANCEL_KEY = u"cancel"
DONE_KEY = u"done"

# GREETINGS
ABOUT_THE_BOT = DRAGON_EMOJI + " *About DracoBot* " + DRAGON_EMOJI + "\n\n" + CAKE_EMOJI + " Birthday: June 2017\n\n" +\
    ROBOT_EMOJI + " Currently maintained by Daniel Lau\n\n" + SKULL_EMOJI +\
    " Past Bot Developers: Ji Cheng, Shao Yi, Bai Chuan, Fiz, Youkuan, Kang Ming, Zhi Yu\n\n"
REQUEST_ADMIN_ID = "Please enter your Admin ID to proceed."
ADMIN_GREETING = "Hello there, Administrator! What do you want to say to everyone?\n" +\
    "Whatever you submit from now on will be broadcasted to all users, be CAREFUL!" +\
    "Type /" + DONE_KEY + " to exit, once you have made your announcement."
HELLO_GREETING = "Hello there, {}! DracoBot at your service! Press /" + \
    MENU_KEY + " to bring up keyboard! " + DRAGON_EMOJI
HELP_MESSAGE = "Hello there, {}!\n\n" +\
    "Dragon Trainer Bot is a homegrown telegram bot that allows you to anonymously chat with your Dragon or Trainer.\n\n" +\
    "While in the Main Menu, click on:\n" +\
    DRAGON_CHAT_KEY + ": To chat with your Dragon \n" +\
    TRAINER_CHAT_KEY + ": To chat with your Trainer\n" +\
    HELP_KEY + ": To explore this bot's functionality\n" +\
    STATUS_KEY + ": To view status of Dragon and Trainer\n\n" +\
    ABOUT_THE_BOT_KEY + ": To view information about the bot\n" +\
    RULES_KEY + ": To view the game rules\n" +\
    "Type /" + DONE_KEY + " at any point in time to exit the Chat feature\n" +\
    "Type /" + MENU_KEY + " to show the Main Menu\n\n" +\
    "Please message @dlau98 if you need technical assistance!\n" +\
    "Thank you and we hope you'll have fun throughout this game! :)"
GAME_RULES_MESSAGE = "Rules of Dragons and Trainers " + DRAGON_EMOJI + "\n\n" +\
    "Each of you who participated will be assigned a Trainer and a Dragon. " +\
    "Of course, you will know the identity of your Dragon while your Trainer’s identity will be kept " +\
    "from you. Throughout the course of the event, feel free to chat with both your Dragon and Trainer " +\
    "through telegram bot where your identity will be kept secret, and take care of your dragon with " +\
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
    "Draco House Comm" + BLUE_HEART_EMOJI
WELCOME_MESSAGE = "Dear {name},\n\n"\
    "You woke up dizzy in the highest floors of a building known as AreSeaFore and you don't know how you were transported here. Next to you a piece of paper which reads:\n\n"\
    "\"Trainer, you are tasked to train dragon ‘{dragon_name}’ for the next 3 weeks. Slowly approach the dragon at unit {dragon_room_number} to tame it and teach it new skills. Your dragon likes ‘{dragon_likes}’ but it really dislikes ‘{dragon_dislikes}‘. ‘{dragon_requests}' is stated as off limits. The difficulty of training is LEVEL {dragon_level:d}.\n\n"\
    "To assist you in your journey and communicate with your dragons and your trainers, invoke the mystical help of @DragonTrainerBot\n\n"\
    "I am your creator @dlau98, and I will watch over all of you trainers throughout the next 3 weeks. Do contact me should you need assistance in taming your dragon.\n\n"\
    "Set forth young one and be the best dragon tamer of AreSeaFore Draco.\"\n\n"\
    "*Game of Thrones Music Intensifies*"
STATUS = "Trainer Status: {trainer_status}\n"\
    "Dragon Status: {dragon_status}\n"
DRAGON_DETAILS = "Dragon Details " + DRAGON_EMOJI + "\n"\
    "Name: {name}\n"\
    "Likes: {likes}\n"\
    "Dislikes: {dislikes}\n"\
    "Unit: {room_number}\n"\
    "Off Limits: {requests}\n"\
    "Level: {level:d}\n"
CHAT_COMPLETE = "Done chatting."
TRAINER_CONNECTION_SUCCESS = "You have been connected with your Trainer." +\
    " Anything you type here will be sent anonymously to him/her.\n" +\
    "To exit, type /" + DONE_KEY
DRAGON_CONNECTION_SUCCESS = "You have been connected with your Dragon." +\
    " Anything you type here will be sent anonymously to him/her.\n" +\
    "To exit, type /" + DONE_KEY
DELETE_MESSAGE_SUCCESS = "Message deleted."

# Error Messages
USER_UNREGISTERED = "You have not been registered. Press /start once you have registered."
USER_NO_TELE_HANDLE = "Please register with your telegram handle."
USER_NO_TRAINER = "You have no trainer. Please ask the admin to assign a trainer to you."
USER_UNREGISTERED_TRAINER = "Your trainer has not register. Please try again later."
USER_NO_DRAGON = "You have no dragon. Please ask the admin to assign a trainer to you."
USER_UNREGISTERED_DRAGON = "Your dragon has not register. Please try again later."
UNSUPPORTED_MEDIA = "Media not supported."
CONNECTION_ERROR = "Connection error. Please be patient and try again soon!" + SMILEY_EMOJI
CANNOT_DELETE_ERROR = "Cannot delete message."
DELETE_MESSAGE_ERROR = "Message has been deleted."
DELETE_MESSAGE_REPLY_ERROR = "Please reply a message to delete."
UNKNOWN_COMMAND = "Unknown command. Press /" + \
    MENU_KEY + " to bring up keyboard."
