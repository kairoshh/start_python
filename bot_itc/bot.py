import telebot
from config import TOKEN

from telebot import types

from random import choice



bot = telebot.TeleBot(TOKEN)

keyboard = types.ReplyKeyboardMarkup(True)

stone = '👊'
paper = '🫱'
soccer = '🤟'



keyboard.add(stone, paper, soccer)

def select_values():
    bot_answer = ['👊', '🤟', '🫱']
    return choice(bot_answer)

@bot.message_handler(commands = ['start'])
def start_message(message):
    username = message.from_user.username
    bot.send_message(
        message.chat.id,f'Hello {username}',
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['text'])
def check(message):
    if message.text == stone:
        bot_result = select_values()
        bot.send_message(message.chat.id, bot_result)
        if bot_result == stone:
            bot.send_message(message.chat.id, 'Ничья')
        elif bot_result == paper:
            bot.send_message(message.chat.id, 'Бот выйграл')
        elif bot_result == soccer:
            bot.send_message(message.chat.id, 'Вы выйграли')

    elif message.text == paper:
        bot_result = select_values()
        bot.send_message(message.chat.id, bot_result)
        if bot_result == paper:
            bot.send_message(message.chat.id, 'Ничья')
        elif bot_result == soccer:
            bot.send_message(message.chat.id, 'Бот выйграл')
        elif bot_result == stone:
            bot.send_message(message.chat.id, 'Вы выйграли')

    elif message.text == soccer:
        bot_result = select_values()
        bot.send_message(message.chat.id, bot_result)
        if bot_result == soccer:
            bot.send_message(message.chat.id, 'Ничья')
        elif bot_result == stone:
            bot.send_message(message.chat.id, 'Бот выйграл')
        elif bot_result == paper:
            bot.send_message(message.chat.id, 'Вы выйграли')

    else:
        bot.send_message(message.chat.id, 'играй нормально')


if __name__ == "__main__":
    bot.polling(none_stop=True)