from telegram.ext import Filters
from models import MessageMapping

SUPPORTED_MESSAGE_FILTERS = Filters.photo | Filters.sticker | Filters.document | Filters.video | Filters.video_note | Filters.audio | Filters.voice | Filters.text

def format_message(message_text, is_dragon=True, is_prefix=False):
    receiver_type = 'Dragon' if is_dragon else 'Trainer'

    if is_prefix:
        ret_msg = "From %s:\n%s" % (receiver_type, message_text)
    else:
        if message_text is not None and len(message_text) > 0:
            ret_msg = "%s\n- From %s" % (message_text, receiver_type)
        else:
            ret_msg = "- From %s" % (receiver_type)
    return ret_msg

def forward_message(message, chat_id, bot, session, is_dragon=True):
    is_forward = message.forward_from is not None or message.forward_from_message_id is not None
    is_photo = len(message.photo) > 0
    is_document = message.document is not None
    is_video = message.video is not None
    is_audio = message.audio is not None
    is_voice = message.voice is not None
    is_sticker = message.sticker is not None
    is_video_note = message.video_note is not None

    caption = message.caption
    caption_style_text = format_message(caption, is_dragon=is_dragon, is_prefix=False)

    reply_to_message_id = None
    if message.reply_to_message is not None:
        # TODO: query for message mapping
        # reply_to_message_id = update.message.reply_to_message (.message_id or .chat_id)
        pass

    if is_forward:
        sent_msg = message.forward(chat_id)
        bot.send_message(chat_id=chat_id, text=caption_style_text, reply_to_message_id=sent_msg.message_id)
    elif is_photo:
        highest_res_photo = max(message.photo, key=lambda x: x.file_size)
        sent_msg = bot.send_photo(chat_id=chat_id, photo=highest_res_photo, caption=caption_style_text, reply_to_message_id=reply_to_message_id)
    elif is_document:
        sent_msg = bot.send_document(chat_id=chat_id, document=message.document, caption=caption_style_text, reply_to_message_id=reply_to_message_id)
    elif is_video:
        sent_msg = bot.send_video(chat_id=chat_id, video=message.video, caption=caption_style_text, reply_to_message_id=reply_to_message_id)
    elif is_audio:
        sent_msg = bot.send_audio(chat_id=chat_id, audio=message.audio, caption=caption_style_text, reply_to_message_id=reply_to_message_id)
    elif is_voice:
        sent_msg = bot.send_voice(chat_id=chat_id, voice=message.voice, caption=caption_style_text, reply_to_message_id=reply_to_message_id)
    elif is_sticker:
        sent_msg = bot.send_sticker(chat_id=chat_id, sticker=message.sticker, reply_to_message_id=reply_to_message_id)
        bot.send_message(chat_id=chat_id, text=caption_style_text, reply_to_message_id=sent_msg.message_id)
    elif is_video_note:
        sent_msg = bot.send_video_note(chat_id=chat_id, video_note=message.video_note, reply_to_message_id=reply_to_message_id)
        bot.send_message(chat_id=chat_id, text=caption_style_text, reply_to_message_id=sent_msg.message_id)
    else:
        sent_msg = bot.send_message(chat_id=chat_id, text=format_message(message.text, is_dragon=is_dragon, is_prefix=True), reply_to_message_id=reply_to_message_id)

    mapping = MessageMapping(sender_message_id=message.message_id, receiver_message_id=sent_msg.message_id, receiver_chat_id=sent_msg.chat_id, is_dragon=is_dragon)
    session.add(mapping)
    session.commit()

def handle_edited_message(session):
    def handle_edited_message_decorator(func):
        def inner_edited_message(update, context):
            if update.edited_message is not None:
                message_id = update.edited_message.message_id
                edited_message = session.query(MessageMapping).filter(MessageMapping.sender_message_id==message_id).first()
                if edited_message is not None:
                    if update.edited_message.text:
                        formatted_text = format_message(update.edited_message.text, is_dragon=edited_message.is_dragon, is_prefix=True)
                        context.bot.edit_message_text(formatted_text, chat_id=edited_message.receiver_chat_id, message_id=edited_message.receiver_message_id)
                    elif update.edited_message.caption:
                        import pdb; pdb.set_trace()
                        formatted_caption = format_message(update.edited_message.caption, is_dragon=edited_message.is_dragon, is_prefix=False)
                        context.bot.edit_message_caption(caption=formatted_caption, chat_id=edited_message.receiver_chat_id, message_id=edited_message.receiver_message_id)
            else:
                return func(update, context)
        return inner_edited_message
    return handle_edited_message_decorator