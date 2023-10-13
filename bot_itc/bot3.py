import telebot
from config import TOKEN
from random import choice
from words import allWords
from telebot import types

bot = telebot.TeleBot(TOKEN)
keyboard = types.ReplyKeyboardMarkup(True)

stars = 'random words'
keyboard.add(stars)

bot = telebot.TeleBot(TOKEN)


def select_values():
    
    return choice(allWords)
        
@bot.message_handler(commands=['start'])
def start_message(messege):
    username = messege.from_user.username
    bot.send_message(
        messege.chat.id, f'Hello {username},\n давай учить английский',
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == stars:
        for i in range(10):
            bot_result = select_values()
            print(bot_result)
            bot.send_message(message.chat.id, f'{bot_result}'.replace('{', '').replace('}', '').replace("'", "").replace(":", ' - '))


if __name__ == "__main__":  
    bot.polling(none_stop=True)