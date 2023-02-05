import telebot
import tokens
import getinfo
import topauto
from telebot import types
import city as where




bot = telebot.TeleBot(tokens.Token)


print('started')

   
@bot.message_handler(commands=['start'])
def start_message(message):

    main_btns = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    one_btn = types.KeyboardButton('Меню')

    btns = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілі в 2023', callback_data='top10')
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
        btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілі в 2023', callback_data='top10')
        btn3 = types.InlineKeyboardButton(text='Автосервіси', callback_data='4')
        btn4 = types.InlineKeyboardButton(text='INFO', callback_data='3')
        btn5 = types.InlineKeyboardButton(text='Власник', callback_data='owner')
        btns.add(btn1, btn3, btn4, btn5)


        bot.send_message(message.chat.id, "Меню", reply_markup=btns)
        return 0 

    file_a = open('info.txt', 'a')
    with file_a as f:
        f.write(f'{message.from_user.username} {message.from_user.first_name}\n')

    try:
        car_info = getinfo.creat_info(number)

        bot.send_photo(message.chat.id, car_info[5], f'{car_info[1]}\n{car_info[0]}\n{car_info[3]} {number}\n{car_info[2]}\n{car_info[4]}')
    
    except IndexError:
        bot.send_message(message.chat.id, f'Машину з номерним знаком {number} не зеайдено')



@bot.callback_query_handler(func=lambda call: True)
def checck_callback(call):

    city = topauto.all_citys
    city_link = topauto.all_citys_link

    if call.data == 'top10':

        btns = types.InlineKeyboardMarkup(row_width=1)
        btn2 = types.InlineKeyboardButton(text='Топ-50 найпопулярніших нових автомобілі в 2023', callback_data='top50')
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')

        btns.add(btn2, back)

        arr_top10 = ''
        for i in range(10):
            arr_top10 += topauto.all_cars_out[i] + '\n'

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=arr_top10, reply_markup=btns)

        
    if call.data == 'top50':
        
        arr_top50 = ''
        for i in range(50):
            arr_top50 += topauto.all_cars_out[i] + '\n'

        btns = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        btns.add(back)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=arr_top50, reply_markup=btns)

    if call.data == '3':

        btns = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        btns.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Доступні команди:\n\n/info', reply_markup=btns)


    if call.data == '4':

        

        btns = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text=city[0], callback_data='kyiv')
        btn2 = types.InlineKeyboardButton(text=city[1], callback_data='kyiv-ob')
        btn3 = types.InlineKeyboardButton(text=city[2], callback_data='vinnycia')
        btn4 = types.InlineKeyboardButton(text=city[4], callback_data='dnipro')
        btn5 = types.InlineKeyboardButton(text=city[10], callback_data='frankivsk')
        btn6 = types.InlineKeyboardButton(text=city[13], callback_data='lviv')
        btn7 = types.InlineKeyboardButton(text=city[15], callback_data='odesa')
        btn8 = types.InlineKeyboardButton(text=city[16], callback_data='poltava')
        btn9 = types.InlineKeyboardButton(text=city[21], callback_data='harkiv')
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        btns.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, back)


        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Виберіть місто', reply_markup=btns)


    if call.data == 'owner':

        btns = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        btns.add(back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Bласник @rerete13\nНа їжу:\n\n5375414131355314", reply_markup=btns)


    def bot_out_city(x):

        btns = types.InlineKeyboardMarkup(row_width=1)
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        btns.add(back)

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"Це може зайняти деякий час...")

        out = f'{city[x]}\n\n'

        for i in range(len(where.getcity(city_link[x])[0])):
            out += f'{where.getcity(city_link[x])[0][i]}\n\n'


        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"{out}", reply_markup=btns)


    if call.data == 'kyiv':
        bot_out_city(0)

    if call.data == 'kyiv-ob':
        bot_out_city(1)

    if call.data == 'vinnycia':
        bot_out_city(2)

    if call.data == 'dnipro':
        bot_out_city(4)

    if call.data == 'frankivsk':
        bot_out_city(10)


    if call.data == 'lviv':
        bot_out_city(13)

    if call.data == 'odesa':
        bot_out_city(15)

    if call.data == 'poltava':
        bot_out_city(16)

    if call.data == 'harkiv':
        bot_out_city(21)

    
    if call.data == 'back':
    

        btns = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton(text='Топ-10 найпопулярніших нових автомобілі в 2023', callback_data='top10')
        btn3 = types.InlineKeyboardButton(text='Автосервіси', callback_data='4')
        btn4 = types.InlineKeyboardButton(text='INFO', callback_data='3')
        btn5 = types.InlineKeyboardButton(text='Власник', callback_data='owner')
        btns.add(btn1, btn3, btn4, btn5)
        
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Меню', reply_markup=btns)



bot.polling()