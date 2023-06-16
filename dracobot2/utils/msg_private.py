def is_message_private(message):
    is_photo = len(message.photo) > 0
    is_document = message.document is not None
    is_video = message.video is not None
    is_audio = message.audio is not None
    is_voice = message.voice is not None
    is_sticker = message.sticker is not None
    is_video_note = message.video_note is not None
    is_text = message.text is not None

    return is_text or is_document or is_sticker or is_photo
