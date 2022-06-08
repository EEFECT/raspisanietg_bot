import config
from telebot import types
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) # Приветствие
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Какое рассписание")
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот для того чтобы скидывать тебе рассписание!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text']) 
def func(message):

    menu1 = telebot.types.InlineKeyboardMarkup()
    menu1.add(telebot.types.InlineKeyboardButton(text = 'АСУ РСО', callback_data ='first', url="https://asurso.ru/"))

    if(message.text == "Какое рассписание"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Понедельник")
        btn2 = types.KeyboardButton("Вторник")
        btn3 = types.KeyboardButton("Среда")
        btn4 = types.KeyboardButton("Четверг")
        btn5 = types.KeyboardButton("Пятница")
        btn6 = types.KeyboardButton("Суббота")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text="Выбери день недели)", reply_markup=markup)
    
    elif(message.text == "Понедельник"):
        bot.send_message(message.chat.id, "Литература\nФран/нем яз\nХимия\nАлгебра\nФизкультура\nАнглийский язык", reply_markup = menu1)
    
    elif message.text == "Вторник":
        bot.send_message(message.chat.id, text="История\nАнглийский язык\nГеография\nФизика\nАлгебра\nГеометрия", reply_markup = menu1)
    
    elif message.text == "Среда":
        bot.send_message(message.chat.id, text="Физика\nФран/нем яз\nФизкультура\nИнформатика\nБиология\nАнглийский язык", reply_markup = menu1)

    elif message.text == "Четверг":
        bot.send_message(message.chat.id, text="Английский язык\nИстория\nРусский язык\nРусский язык\nФизика\nОбществознание", reply_markup = menu1)

    elif message.text == "Пятница":
        bot.send_message(message.chat.id, text="Литература\nАлгебра\nИстория\nАнглийский язык\nГеометрия\nФизкультура", reply_markup = menu1)
    
    elif message.text == "Суббота":
        bot.send_message(message.chat.id, text="Химия\nГеография\nБиология\nРусский язык\nЛитература\nОБЖ", reply_markup = menu1)
    
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)