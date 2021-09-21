import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('e933e0aebdfa5f6500850a1feeb5bcf8')
mgr = owm.weather_manager()
bot = telebot.TeleBot("2023281652:AAEYviPdv4V8MpTp8e75yEi7XY5qc5Vu4WM")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    answer = "В городе " + message.text + " сейчас в районе " + str(temp) + "\n"
    bot.send_message(message.chat.id, answer)    

bot.polling( none_stop = True )