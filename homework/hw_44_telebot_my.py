#5321791887:AAEIHFG6Kyn-JzTcZN4o_cLJp_lRVD0oH2c
# @WeekendTravel_bot

import telebot
from telebot import types

token = "5321791887:AAEIHFG6Kyn-JzTcZN4o_cLJp_lRVD0oH2c"
bot = telebot.TeleBot(token)

def create_menu():
    menu = types.InlineKeyboardMarkup()
    vitebsk_btn = types.InlineKeyboardButton(text="Витебщина",callback_data="vitebsk")
    menu.add(vitebsk_btn)
    grodno_btn = types.InlineKeyboardButton(text="Гродненщина",callback_data='grodno')
    menu.add(grodno_btn)
    brest_btn = types.InlineKeyboardButton(text="Брестщина", callback_data='brest')
    menu.add(brest_btn)
    gomel_btn = types.InlineKeyboardButton(text="Гомельщина", callback_data="gomel")
    menu.add(gomel_btn)
    mogilev_btn = types.InlineKeyboardButton(text="Могилевщина", callback_data="mogilev")
    menu.add(mogilev_btn)
    return menu

def make_choice_1():
    choice = types.InlineKeyboardMarkup()
    nature_btn = types.InlineKeyboardButton(text='Люблю смотреть на природные красоты.',
                                            callback_data='nature_1')
    history_btn = types.InlineKeyboardButton(text='Меня очень занимают исторические места.',
                                            callback_data='history_1')
    choice.add(nature_btn)
    choice.add(history_btn)
    return choice

def make_choice_2():
    choice = types.InlineKeyboardMarkup()
    nature_btn = types.InlineKeyboardButton(text='Люблю смотреть на природные красоты.',
                                            callback_data='nature_2')
    history_btn = types.InlineKeyboardButton(text='Меня очень занимают исторические места.',
                                            callback_data='history_2')
    choice.add(nature_btn)
    choice.add(history_btn)
    return choice

def make_choice_3():
    choice = types.InlineKeyboardMarkup()
    nature_btn = types.InlineKeyboardButton(text='Люблю смотреть на природные красоты.',
                                            callback_data='nature_3')
    history_btn = types.InlineKeyboardButton(text='Меня очень занимают исторические места.',
                                            callback_data='history_3')
    choice.add(nature_btn)
    choice.add(history_btn)
    return choice

def make_choice_4():
    choice = types.InlineKeyboardMarkup()
    nature_btn = types.InlineKeyboardButton(text='Люблю смотреть на природные красоты.',
                                            callback_data='nature_4')
    history_btn = types.InlineKeyboardButton(text='Меня очень занимают исторические места.',
                                            callback_data='history_4')
    choice.add(nature_btn)
    choice.add(history_btn)
    return choice

def make_choice_5():
    choice = types.InlineKeyboardMarkup()
    nature_btn = types.InlineKeyboardButton(text='Люблю смотреть на природные красоты.',
                                            callback_data='nature_5')
    history_btn = types.InlineKeyboardButton(text='Меня очень занимают исторические места.',
                                            callback_data='history_5')
    choice.add(nature_btn)
    choice.add(history_btn)
    return choice

def to_back_menu():
    back_menu = types.InlineKeyboardMarkup()
    back_menu_btn = types.InlineKeyboardButton(text="Вернуться в основное меню",
                                               callback_data="back_menu")
    back_menu.add(back_menu_btn)
    return back_menu


@bot.message_handler(commands=['start'])
def start_bot(message):
    audio = open('aria.mp3', 'rb')
    bot.send_audio(
        message.chat.id,
        audio=audio
    )
    audio.close()
    menu = create_menu()
    bot.send_message(
        message.chat.id,
        "Выбирай направление куда поедешь:",
        reply_markup= menu
    )


@bot.message_handler(commands=['whoami'])
def who_bot(message):
    img = open('weekend_trip.jpg', 'rb')
    menu = create_menu()
    bot.send_photo(
        message.chat.id,
        photo= img,)
    img.close()
    bot.send_message(
        message.chat.id,
        "Привет👋 Наверняка приближаются выходные и ты думаешь куда поехать🧐."
        "Давай я помогу тебе с этим, нажимай /start \n"
        "Just Do It"
    )

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    menu = create_menu()
    back_menu = to_back_menu()

    if call.message:
        if call.data=='vitebsk':
            bot.send_message(
                chat_id=call.message.chat.id,
                text='Выбирай что по душе:',
                reply_markup=make_choice_1()

            )
        if call.data == 'grodno':
            bot.send_message(
                chat_id=call.message.chat.id,
                text='Выбирай что по душе:',
                reply_markup=make_choice_2()

            )


        if call.data=='history_1':
            img = open('polock.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo = img,
                caption="https://34travel.me/gotobelarus/post/polock-mts-rus",
                reply_markup=back_menu
            )
            img.close()

        if call.data=='nature_1':
            img = open('elnya.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo = img,
                caption="https://34travel.me/gotobelarus/post/kia-elnya",
                reply_markup=back_menu
            )
            img.close()

        if call.data=='history_2':
            img = open('jeludok.jfif','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo = img,
                caption="https://34travel.me/gotobelarus/post/marshrut-po-doroge-v-grodno",
                reply_markup=back_menu
            )
            img.close()

        if call.data=='nature_2':
            img = open('karier.jpg','rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo = img,
                caption="https://34travel.me/gotobelarus/post/5-melovyh-karerov-belarusi",
                reply_markup=back_menu
            )
            img.close()

        if call.data == 'brest':
            bot.send_message(
                chat_id=call.message.chat.id,
                text='Выбирай что по душе:',
                reply_markup=make_choice_3()

            )

        if call.data == 'history_3':
            img = open('kosovo.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://34travel.me/gotobelarus/post/podcast-puslovskije",
                reply_markup=back_menu
            )
            img.close()

        if call.data == 'nature_3':
            img = open('puscha.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://34travel.me/gotobelarus/post/belovezha-podcast",
                reply_markup=back_menu
            )
            img.close()

        if call.data == 'gomel':
            bot.send_message(
                chat_id=call.message.chat.id,
                text='Выбирай что по душе:',
                reply_markup=make_choice_4()

            )

        if call.data == 'history_4':
            img = open('rogachev.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://34travel.me/gotobelarus/post/aroundhomel",
                reply_markup=back_menu
            )
            img.close()

        if call.data == 'nature_4':
            img = open('gomel.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://34travel.me/gotobelarus/post/gomel-mts-rus",
                reply_markup=back_menu
            )
            img.close()

        if call.data == 'mogilev':
            bot.send_message(
                chat_id=call.message.chat.id,
                text='Выбирай что по душе:',
                reply_markup=make_choice_5()

            )

        if call.data == 'history_5':
            img = open('mogilev.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://34travel.me/gotobelarus/post/marshrut-kia-mogilevskaya-oblast",
                reply_markup=back_menu
            )
            img.close()

        if call.data == 'nature_5':
            img = open('bobruisk.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption="https://34travel.me/gotobelarus/post/bobrujsk-mts-rus",
                reply_markup=back_menu
            )
            img.close()



        if call.data=="back_menu":
            bot.send_message(
                chat_id=call.message.chat.id,
                text="Не понравилось? Попробуй выбрать другое направление:",
                reply_markup=menu
            )



if __name__=="__main__":
    bot.polling(none_stop=True)