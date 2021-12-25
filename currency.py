import requests
from datetime import datetime
import telebot

token = '5002831327:AAG4VH6-IyYhYe_18fLWVmL2vEHiqScwOE4'
bot=telebot.TeleBot(token)


keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row("BTC/USD", "ETH/USD")




def send(chat_id, text):
    bot.send_message(chat_id, text, reply_markup = keyboard)


    
@bot.message_handler(commands=['start'])
def start(message):
    send(message.chat.id, "Привет, я бот, который может быстро предоставить тебе информацию о курсе основных криптовалют с обновлением в 24 часа ")





@bot.message_handler(content_types = ['text'])
def text(message):
    chat_id = message.chat.id
    msg = message.text

    if msg =="BTC/USD":
        time_now = datetime.now().strftime('%d.%m.%Y  %H:%M')
        req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
        response = req.json()
        average_price = response["btc_usd"]["avg"]
        
        average_price_and_time_now=str(round(average_price, 3)) + "                    " + time_now
        send(message.chat.id, average_price_and_time_now)
    
        
    if msg =="ETH/USD":
        time_now = datetime.now().strftime('%d.%m.%Y  %H:%M')
        req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
        response = req.json()
        average_price = response["eth_usd"]["avg"]
        
        average_price_and_time_now=str(round(average_price, 3)) + "                    " + time_now
        send(message.chat.id, average_price_and_time_now)

    if msg !="ETH/USD" and msg !="BTC/USD":
        send(message.chat.id, "Не знаю...")
        

bot.polling(none_stop = True)
    
