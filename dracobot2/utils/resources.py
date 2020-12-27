from dracobot2.models import MsgFrom
from dracobot2.resources import *


def format_message(message_text, message_from=MsgFrom.DRAGON, is_prefix=False, is_edited=False):
    receiver_type = 'Dragon' if message_from == MsgFrom.DRAGON else 'Trainer' if message_from == MsgFrom.TRAINER else 'Admin'

    if is_edited:
        message_text += ' (edited)'

    if is_prefix:
        ret_msg = "%s:\n%s" % (receiver_type, message_text)
    else:
        if message_text is not None and len(message_text) > 0:
            ret_msg = "%s\n- %s" % (message_text, receiver_type)
        else:
            ret_msg = "- %s" % (receiver_type)
    return ret_msg


def format_registered_message(user):
    if user is None:
        return "Not assigned " + CROSS_EMOJI
    elif user.registered:
        return "Registered " + GREEN_STATUS_EMOJI
    else:
        return "Not registered " + RED_STATUS_EMOJI
