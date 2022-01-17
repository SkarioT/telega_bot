import requests
from auth_data import token
from datetime import datetime
import telebot
import platform
import subprocess

# from requests.exceptions import SSLError

def get_ETH_price ():
    url = f'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'

    respons =requests.get(url).json()
    cdt = datetime.now()
    USD_price = respons.get("USD")
    print(f"Курс ETH {USD_price} на {cdt}")
    return f"Курс ETH {USD_price} на {cdt}"

def pinger(host='8.8.8.8'):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '3', host]
    response = subprocess.check_output(command)

    print(response.decode('Windows-1251'))
    return response.decode('Windows-1251')

def tracert(host='8.8.8.8'):


    command = ['tracert', host]
    response = subprocess.check_output(command)

    print(response.decode('Windows-1251'))
    return response.decode('Windows-1251')


def telega_bot (token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands="start")
    def start_bot(message):
        # bot.send_message(message.chat.id,f"{get_ETH_price()}")
        bot.send_message(message.chat.id,f"Здароу")
    
    @bot.message_handler(content_types=["text"])    
    def send_message(message):
        if message.text.lower()=="price":
            bot.send_message(message.chat.id,f"{get_ETH_price()}")
        
        elif str(message.text.lower()).startswith("ping"):
            get_msg = str(message.text.lower()).split(" ")
            print(get_msg)
            bot.send_message(message.chat.id,f"Выполняю команду {message.text.lower()}")

            bot.send_message(message.chat.id,f"{pinger(get_msg[1])}")
        elif str(message.text.lower()).startswith("tracert"):
            get_msg = str(message.text.lower()).split(" ")
            print(get_msg)
            bot.send_message(message.chat.id,f"Выполняю команду {message.text.lower()}")

            bot.send_message(message.chat.id,f"{tracert(get_msg[1])}")
        else:
            bot.send_message(message.chat.id,f"Чё надо, хозяин?")
        
        
    bot.polling()
# 
while True:
    telega_bot(token)