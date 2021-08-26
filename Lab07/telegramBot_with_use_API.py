import telebot 
import pyowm

bot = telebot.TeleBot('1830389722:AAEi2gOF8N2pjFnxmlXvrfTrqKrDRYD248E')
owm_token = 'pypi-AgEIcHlwaS5vcmcCJDI0OTY4NDgxLWJmNmMtNDNlNS05MjNhLTEyODA5YmRhNWUwYwACJXsicGVybWlzc2lvbnMiOiAidXNlciIsICJ2ZXJzaW9uIjogMX0AAAYgadguy4szx2ijNc233VQRLFTGFmjwJnu4w7sH24xDIcI'
owm = pyowm.OWM(owm_token)
owm = pyowm.OWM(owm_token)

@bot.message_handler(commands=['start']) 
def start_message(message):
    bot.send_message(message.chat.id, 'Ваше повідомлення /start')

@bot.message_handler(commands=['city']) #команда для отримання початкових даних
def cmd_city(message):
    send = bot.send_message(message.chat.id, 'Введи місто')
    bot.register_next_step_handler(send, city)

def city(message): #основна робота з декількома варіантами в залежності від результату
    bot.send_message(message.chat.id, 'Дізнаюсь погодні умови в місті {city}'.format(city=message.text))

    data = message.text
    observation = owm.weather_at_place(data)
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']

    answer = f"В місті {message.text} зараз {w.get_detailed_status()} \n"
    answer += f"Приблизна температура {round(temp)} градусів\n\n"

    if temp < 0:
        answer += 'Зараз температура нижче нуля, одягайся тепліше!'
        sti = open('static/ice.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti)
    elif temp < 15:
        answer += 'Зараз прохолодно, варто одягнутися тепліше!'
        sti = open('static/socold.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti)
    else:
        answer += 'Зараз досить тепло, можна одягнутися легше'
        sti = open('static/hot.tgs', 'rb')
        bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)