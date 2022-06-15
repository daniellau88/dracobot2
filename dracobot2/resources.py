# EMOJI UNICODE
CAKE_EMOJI = u"\U0001F382"
ROBOT_EMOJI = u"\U0001F916"
SKULL_EMOJI = u"\U0001F480"
SMILEY_EMOJI = u"\U0001F642"
HELP_EMOJI = u"\U0001F64F"
MONKEY_EMOJI = u"\U0001F64A"
DRAGON_EMOJI = u"\U0001F937"  # In use for Dragon Trainer Bot
TRAINER_EMOJI = u"\U0001F607"
BLUE_HEART_EMOJI = u"\U0001F499"
GREEN_STATUS_EMOJI = u"\U0001F7E2"
RED_STATUS_EMOJI = u"\U0001F534"
CROSS_EMOJI = u"\U0000274C"
GIFT_EMOJI = u"\U0001F381"
DEVIL_EMOJI = u"\U0001F608"
WINK_EMOJI = u"\U0001F609"
GRIN_EMOJI = u"\U0001F601"
SMILE_EMOJI = u"\U0001F642"
SAD_EMOJI = u"\U00002639"
SPARKLE_EMOJI = u"\U00002728"
SWORD_EMOJI = u"\U0001F5E1"
KNIFE_EMOJI = u"\U0001F52A"
FIRE_EMOJI = u"\U0001F525"
SUNGLASS_EMOJI = u"\U0001F60E"
PARTY_EMOJI = u"\U0001F973"
STAR_EMOJI = u"\U0001F31F"
MEAT_EMOJI = u"\U0001F356"
MUSIC_EMOJI = u"\U0001F3B6"
SPEAK_EMOJI = u"\U0001F5E3"
DRUM_EMOJI = u"\U0001F941"


WHALE_EMOJI = u"\U0001F40B"
SPOUTING_WHALE_EMOJI = u"\U0001F433"
SPEECH_BUBBLE_EMOJI = u"\U0001F4AC"
THINKING_FACE_EMOJI = u"\U0001F914"

# TELEGRAM KEYBOARD KEYS
ABOUT_THE_BOT_KEY = u"About the Bot" + " " + SUNGLASS_EMOJI
ADMIN_KEY = u"admin"
DRAGON_CHAT_KEY = u"Chat with Mortal" + " " + DRAGON_EMOJI
TRAINER_CHAT_KEY = u"Chat with Angel" + " " + TRAINER_EMOJI
STATUS_KEY = u"Status" + " " + GREEN_STATUS_EMOJI
HELP_KEY = u"Help" + " " + HELP_EMOJI
RULES_KEY = u"Rules" + " " + MONKEY_EMOJI
MENU_KEY = u"menu"
TRAINER_KEY = u"angel"
DRAGON_KEY = u"mortal"
START_KEY = u"start"
DELETE_KEY = u"delete"
CANCEL_KEY = u"cancel"
DONE_KEY = u"done"

# GREETINGS
ABOUT_THE_BOT = DRAGON_EMOJI + " *About BizcomAMBot* " + DRAGON_EMOJI + "\n\n" + "Adapted from: DracoBot\n\n" + CAKE_EMOJI + " Birthday: June 2017\n\n" +\
    ROBOT_EMOJI + " Currently maintained by Daniel Lau\n\n" + SKULL_EMOJI +\
    " Past Bot Developers: Ji Cheng, Shao Yi, Bai Chuan, Fiz, Youkuan, Kang Ming, Zhi Yu\n\n"
ADMIN_GREETING = "Hello there, Administrator! What do you want to say to everyone?\n" +\
    "Whatever you submit from now on will be broadcasted to all users, be CAREFUL!\n" +\
    "Type /" + DONE_KEY + " to exit, once you have made your announcement."
HELLO_GREETING = "Hello there, {}! BizcomAMBot at your service! Press /" + \
    MENU_KEY + " to bring up keyboard! " + DRAGON_EMOJI
HELP_MESSAGE = "Hello there, {}!\n\n" +\
    "<u>Main Menu</u>\n" +\
    DRAGON_CHAT_KEY + ": To chat with your Mortal \n" +\
    TRAINER_CHAT_KEY + ": To chat with your Angel\n" +\
    HELP_KEY + ": To explore this bot's functionality\n" +\
    STATUS_KEY + ": To view status of Angel and Mortal\n" +\
    RULES_KEY + ": To view the game rules\n" +\
    ABOUT_THE_BOT_KEY + ": To view information about the bot\n\n" +\
    "Type /" + DONE_KEY + " at any point in time to exit the chat\n" +\
    "Type /" + MENU_KEY + " to show the Main Menu\n\n" +\
    "<u>Features</u>\n" +\
    "1. <b>Reply message</b>: You can reply to a message to automatically chat with your angel / mortal.\n" +\
    "2. <b>Delete message</b>: You can select a message and type /delete\n" +\
    "3. <b>Edit message</b>: You can edit your message to your angel / mortal\n" +\
    "4. <b>Media files</b>: Supported files are <i>audio</i>, <i>document</i>, <i><b>photo</b></i>, <i><b>sticker</b></i>, <i>videos</i>, <i>video note</i> and <i>voice</i>\n\n" +\
    "Please message @dlau98 if you need technical assistance!\n" +\
    "Thank you and we hope you'll have fun throughout this game! :)"
GAME_RULES_MESSAGE = "Rules of Angel and Mortal " + DRAGON_EMOJI + "\n\n" +\
    "Each of you who participated will be assigned a Angel and a Mortal. " +\
    "Of course, you will know the identity of your Mortal while your Angel's identity will be kept " +\
    "from you. Throughout the course of camp, feel free to chat with both your Angel and Mortal " +\
    "through this telegram bot where your identity will be kept secret\n\n" \
    "<i>What can you do with your mortal?</i>\n"\
    "1: Share a worship song\n" +\
    "2: Send them an encouraging word\n" +\
    "3: Wake them up (if they are sleeping during service)\n" +\
    "4: Pray for them (or secretly with them)\n" +\
    "5: Compliment them\n" +\
    "6: Forward a joke\n" +\
    "7: Whatever the Lord leads you to do " + SMILE_EMOJI
WELCOME_MESSAGE = "Dear {name},\n\n\n"\
    "<i>You woke up dizzy in Star Vista " + STAR_EMOJI + " unsure of how you were transported here. Next to you lies a piece of paper which reads:</i>\n\n\n"\
    "Esteemed Angel " + TRAINER_EMOJI + "\n\n\n"\
    "" + PARTY_EMOJI + " Welcome to Legacy Camp " + PARTY_EMOJI + "\n\n\n"\
    "For the next few days, as you feast " + MEAT_EMOJI + " on the word of God and enjoy the Praise & Worship " + MUSIC_EMOJI + "\n\n\n"\
    "Don't just keep it to yourself, share it with your Mortal to bless them\n\n"\
    "Give them an encouraging word, or just share what is on your heart " + BLUE_HEART_EMOJI + "\n\n\n"\
    "If you don't know what to do, look out for random tasks / ideas that will be sent here\n\n\n"\
    "And now your mortal is " + DRUM_EMOJI * 2 + " (drumroll) " + DRUM_EMOJI * 2 + "\n\n\n"\
    "" + STAR_EMOJI * 2 + " <b>{dragon_name}</b> "+ STAR_EMOJI * 2 +  "\n\n\n"\
    "<i>Set forth beloved angel and be the bestest blessing " + STAR_EMOJI * 2 + " to your mortal</i>\n\n\n"\
    
STATUS = "Angel Status: {trainer_status}\n"\
    "Mortal Status: {dragon_status}\n"
DRAGON_DETAILS = "Mortal Details " + DRAGON_EMOJI + "\n\n"\
    "Name: {name}\n"
TRAINER_DETAILS = "Trainer Details " + TRAINER_EMOJI + SPARKLE_EMOJI + "\n\n"\
    "Name: {name}\n"
CHAT_COMPLETE = "You have finish chatting with your {}."
CONNECTION_SUCCESS = "You have been connected with your {}." +\
    " Anything you type here will be sent anonymously to him/her.\n" +\
    "To exit, type /" + DONE_KEY
DELETE_MESSAGE_SUCCESS = "Message deleted."
USER_REPLY_SHORTCUT = "This message has been sent. You are currently connected with your {}. Send /" + DONE_KEY + " when you are done."
USER_REPLY_CHANGE_MODE = "You are currently connected with your {}. Send /" + DONE_KEY + " when you are done."

# Error Messages
USER_UNREGISTERED = "You have not been registered. Press /start once you have registered."
USER_NO_TELE_HANDLE = "Please register with your telegram handle."
USER_NO_TRAINER = "You have no angel. Please ask the admin to assign a angel to you."
USER_UNREGISTERED_TRAINER = "Your angel has not register. Please try again later."
USER_NO_DRAGON = "You have no mortal. Please ask the admin to assign a mortal to you."
USER_UNREGISTERED_DRAGON = "Your mortal has not register. Please try again later."
UNSUPPORTED_MEDIA = "Media not supported."
CONNECTION_ERROR = "Connection error. Please be patient and try again soon!" + SMILEY_EMOJI
CANNOT_DELETE_ERROR = "Cannot delete message."
DELETE_MESSAGE_ERROR = "Message has been deleted."
DELETE_MESSAGE_REPLY_ERROR = "Please reply a message to delete."
UNKNOWN_COMMAND = "Unknown command. Press /" + \
    MENU_KEY + " to bring up keyboard."
UNKNOWN_CHAT_COMMAND = "You are still chatting with your {}. Press /" + \
    DONE_KEY + " if you are done chatting."
TIMEOUT_MESSAGE = "You have been inactive for more than {}. You will be disconnected from the chat."
