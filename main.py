import telebot
import tokens
import getinfo
import topauto
from telebot import types

bot = telebot.TeleBot(tokens.Token)

print('started')


@bot.message_handler(commands=['start'])
def start_message(message):

    main_btns = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    one_btn = types.KeyboardButton('Меню')

    btns = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілі в 2023', callback_data='1')
    btns.add(btn1)
    main_btns.add(one_btn)

    bot.send_message(message.chat.id, "введіть номер у такій формі: AA7777AA", reply_markup=main_btns)




@bot.message_handler(commands=['info'])
def start_message(message):
    bot.send_message(message.chat.id, "Bласник @rerete13\nНа їжу:\n\n5375414131355314")


                
@bot.message_handler(content_types=['text'])
def creating(message):
    number = message.text.upper()

    if number == 'МЕНЮ':
        
        btns = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілі в 2023', callback_data='1')
        btn3 = types.InlineKeyboardButton(text='INFO', callback_data='3')
        btn4 = types.InlineKeyboardButton(text='Власник', callback_data='4')
        btns.add(btn1, btn3, btn4)


        bot.send_message(message.chat.id, "Меню", reply_markup=btns)
        return 0 

    try:
        car_info = getinfo.creat_info(number)

        bot.send_photo(message.chat.id, car_info[5], f'{car_info[1]}\n{car_info[0]}\n{car_info[3]} {number}\n{car_info[2]}\n{car_info[4]}')
    
    except IndexError:
        bot.send_message(message.chat.id, f'Машину з номерним знаком {number} не зеайдено')



@bot.callback_query_handler(func=lambda call: True)
def checck_callback(call):
    if call.data == '1':

        btns = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton(text='Топ-50 найпопулярніших нових автомобілі в 2023', callback_data='2')
        btns.add(btn2)

        arr_top10 = ''
        for i in range(10):
            arr_top10 += topauto.all_cars_out[i] + '\n'


        bot.send_message(call.message.chat.id, text=arr_top10, reply_markup=btns)

    if call.data == '2':
        
        arr_top50 = ''
        for i in range(50):
            arr_top50 += topauto.all_cars_out[i] + '\n'

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=arr_top50)

    if call.data == '3':
         bot.send_message(call.message.chat.id, text='Доступні команди:\n\n/info')

    
    if call.data == '4':
         bot.send_message(call.message.chat.id, text='/info')

bot.polling()