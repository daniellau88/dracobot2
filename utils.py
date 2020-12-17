from telegram.ext import Filters

SUPPORTED_MESSAGE_FILTERS = Filters.photo | Filters.sticker | Filters.document | Filters.video | Filters.video_note | Filters.audio | Filters.voice | Filters.text

def forward_message(message, chat_id, bot, is_dragon=True):
    is_forward = message.forward_from is not None or message.forward_from_message_id is not None
    is_photo = len(message.photo) > 0
    is_document = message.document is not None
    is_video = message.video is not None
    is_audio = message.audio is not None
    is_voice = message.voice is not None
    is_sticker = message.sticker is not None
    is_video_note = message.video_note is not None

    caption = message.caption
    receiver_type = 'Dragon' if is_dragon else 'Trainer'
    if caption is not None:
        caption_style_text = message.caption + ('\n' if len(message.caption) > 0 else '') + '- From ' + receiver_type
    else:
        caption_style_text = '- From ' + receiver_type

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
        bot.send_message(chat_id=chat_id, text="From " + receiver_type + ":\n" + message.text, reply_to_message_id=reply_to_message_id)
