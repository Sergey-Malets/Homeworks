# 5375000057:AAEVwVX9UqzbrHL1zI4tHMpOavM4j8JMOXg
# @qwertypalets_bot
import telebot
from telebot import types

token = "5375000057:AAEVwVX9UqzbrHL1zI4tHMpOavM4j8JMOXg"
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text="Hochu pit`",callback_data="1")
    eat_btn = types.InlineKeyboardButton(text="Hochu est`",callback_data="2")
    walk_btn = types.InlineKeyboardButton(text="I want to walk", callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text="I want to sleep", callback_data='4')
    joke_btn = types.InlineKeyboardButton(text="I want haha", callback_data="5")
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard

def are_you_sure():
    choice = types.InlineKeyboardMarkup()
    y_btn = types.InlineKeyboardButton(text='YES!',callback_data='y')
    n_btn = types.InlineKeyboardButton(text='OK,no', callback_data='n')
    choice.add(y_btn)
    choice.add(n_btn)
    return choice

def exit_bot():
    exit_b = types.InlineKeyboardMarkup()
    ex_btn = types.InlineKeyboardButton(text='STOP BOT',callback_data='exit')
    exit_b.add(ex_btn)
    return exit_b

@bot.message_handler(commands=['start'])
def srart_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Hello! Make choice:",
        reply_markup = keyboard
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    choice = are_you_sure()
    exit_b = exit_bot()
    if call.message:
        if call.data=='1':
            img = open('1.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="I am just bot. This water.",
                reply_markup = keyboard
            )
            img.close()
        if call.data=='2':
            img = open('2.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="I am just bot. This eat.",
                reply_markup = keyboard
            )
            img.close()
        if call.data=='3':
            img = open('3.jpeg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Stay home!",
                reply_markup = keyboard
            )
            img.close()
        if call.data=='4':
            img = open('4.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="Drink energy!",
                reply_markup = keyboard
            )
            img.close()
        if call.data=='5':

            bot.send_message(
                chat_id=call.message.chat.id,
                text='Are you sure?',
                reply_markup= choice

            )
            # choice = are_you_sure()
        if call.data == 'y':
            img = open('5.jpg', 'rb')
            bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="mem",
            reply_markup=keyboard

            )
            img.close()
        if call.data == 'n':
            bot.send_message(
                chat_id=call.message.chat.id,
                text='OK TAK OK',
                reply_markup=exit_b
            )
            bot.send_message(
                chat_id=call.message.chat.id,
                text='or',
                reply_markup=keyboard
            )
        if call.data == 'exit':

            bot.send_message(
                chat_id=call.message.chat.id,
                text='by-by'

            )
            bot.polling(none_stop=False) # осуществляет выход


if __name__=="__main__":
    bot.polling(none_stop=True)