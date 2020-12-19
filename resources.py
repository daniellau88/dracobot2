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
DRAGON_CHAT_KEY = u"Chat with Dragon" + " " + SPEECH_BUBBLE
TRAINER_CHAT_KEY = u"Chat with Trainer" + " " + SPEECH_BUBBLE
HELP_KEY = u"Help" + " " + QUESTION_MARK
RULES_KEY = u"Rules" + " " + MONKEY
MENU_KEY = u"mainmenu"
TRAINER_KEY = u"trainer"
DRAGON_KEY = u"dragon"
START_KEY = u"start"
DELETE_KEY = u"delete"
CANCEL_KEY = u"cancel"
DONE_KEY = u"done"

# GREETINGS
ABOUT_THE_BOT = DRAGON + " *About DracoBot* " + DRAGON + "\n\n" + CAKE + " Birthday: June 2017\n\n" +\
                ROBOT + " Currently maintained by Ji Cheng and Daniel Lau\n\n" + SKULL +\
                " Past Bot Developers: Shao Yi, Bai Chuan, Fiz, Youkuan, Kang Ming, Zhi Yu\n\n"
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
               DRAGON_CHAT_KEY + ": To chat with your Dragon \n" +\
               TRAINER_CHAT_KEY + ": To chat with your Trainer\n" +\
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

WELCOME_MESSAGE = "Dear %s,\n"\
                    "You woke up dizzy in the highest floors of a building known as AreSeaFore and you don't know how you were transported here. Next to you a piece of paper which reads:\n\n"\
                    "\"Trainer, you are tasked to train dragon ‘%s’ for the next 3 weeks. Slowly approach the dragon at unit %s to tame it and teach it new skills. Your dragon likes ‘%s’ but it really dislikes ‘%s‘. ‘%s’ is stated as off limits. The difficulty of training is LEVEL %d.\n\n"\
                    "To assist you in your journey and communicate with your dragons and your trainers, invoke the mystical help of @DragonTrainerBot\n\n"\
                    "I am your creator @JichNgan, and I will watch over all of you trainers throughout the next 3 weeks. Together alongside me are @MistaChewy and @dlau98 who will assist me in your journey. Contact us shall you need assistance in taming your dragon.\n\n"\
                    "Set forth young one and be the best dragon tamer of AreSeaFore Draco.\"\n\n"\
                    "*Game of Thrones Music Intensifies*"

CONNECTED_TRAINER = "You are now connected to your trainer. Type /done when you have finish the conversation."
CONNECTED_DRAGON = "You are now connected to your dragon. Type /done when you have finish the conversation."
CHAT_COMPLETE = "Done chatting"

# Error Messages
USER_UNREGISTERED = "Unregistered user. Press /start once you have registered."
USER_NO_TELE_HANDLE = "Please register with your telegram handle."
USER_NO_TRAINER = "You have no trainer. Please ask the admin to assign a trainer to you."
USER_UNREGISTERED_TRAINER = "Your trainer has not register. Please try again later."
USER_NO_DRAGON = "You have no dragon. Please ask the admin to assign a trainer to you."
USER_UNREGISTERED_DRAGON = "Your dragon has not register. Please try again later."
UNSUPPORTED_MEDIA = "Media not supported."