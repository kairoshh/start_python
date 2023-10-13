import telebot 
from config import TOKEN


import os

import datetime

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    msg = f'Привет{message.from_user.username}'
    bot.send_message(message.chat.id, msg)

@bot.message_handler(content_types=['photo'])
def get_photos(message):
    file_name = message.photo[-1].file_id
    file_id_info = bot.get_file(file_name)
    downloaded_file = bot.download_file(file_id_info.file_path)

    dir_ = os.path.join('photos')
    if not os.path.exists(dir_):
        os.mkdir(dir_)


    with open(f'./photos/{datetime.datetime.timestamp(datetime.datetime.now())}.jpg','wb') as f:
        f.write(downloaded_file)

    bot.send_message(message.chat.id,'Фото успешно сохранено')


@bot.message_handler(content_types=['document'])
def get_docs(message):
    file_name = message.document.file_id
    file_id_info = bot.get_file(file_name)
    downloaded_file = bot.download_file(file_id_info.file_path)

    dir1_ = os.path.join('documents')
    if not os.path.exists(dir1_):
        os.mkdir(dir1_)


    with open('./documents/{datetime.datetime.timestamp(datetime.datetime.now())}.png','wb') as f:
        f.write(downloaded_file)

    bot.send_message(message.chat.id,'Фото успешно сохранено')

if __name__ == "__main__":
    bot.polling(none_stop=True)

