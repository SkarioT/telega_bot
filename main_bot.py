import requests
from auth_data import token
from datetime import datetime
import telebot
import platform
import subprocess
import platform

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
    try:
        response = subprocess.check_output(command)
    #добавить проверку статус кода \\ returned non-zero exit status 1
    except subprocess.CalledProcessError as e:
        response = e.output
        # return response
    print(response.decode('Windows-1251'))
    return response.decode('Windows-1251')

def tracert(host='8.8.8.8'):

    p_sys = platform.system()
    if p_sys == "Windows":
        command = ['tracert', host]
    else:
        command = ['traceroute', host]

    try:
        response = subprocess.check_output(command)
    #добавить проверку статус кода \\ returned non-zero exit status 1
    except subprocess.CalledProcessError as e:
        response = e.output
        # return response
    print(response.decode('Windows-1251'))
    return response.decode('Windows-1251')

def nslookup(host='8.8.8.8',server='8.8.8.8'):
    
    p_sys = platform.system()
    if p_sys == "Windows":
        command = ['nslookup', host,server]
    else:
        command = ['nslookup', host,server]

    try:
        response = subprocess.check_output(command)
    #добавить проверку статус кода \\ returned non-zero exit status 1
    except subprocess.CalledProcessError as e:
        response = e.output
        # return response
    print(response.decode('Windows-1251'))
    return response.decode('Windows-1251')

def nmap(host='8.8.8.8'):
    
    p_sys = platform.system()
    if p_sys == "Windows":
        command = ['tracert', host]
    else:
        command = ['nmap', host]

    try:
        response = subprocess.check_output(command)
    #добавить проверку статус кода \\ returned non-zero exit status 1
    except subprocess.CalledProcessError as e:
        response = e.output
        # return response
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
        if message.text.lower()=="/price":
            bot.send_message(message.chat.id,f"{get_ETH_price()}")
        
        elif str(message.text.lower()).startswith("/ping"):
            get_msg = str(message.text.lower()).split(" ")
            print(get_msg)
            if len(get_msg)==1:
                bot.send_message(message.chat.id,f"Так а что то?")
            else:
                bot.send_message(message.chat.id,f"Выполняю команду {message.text.lower()}")
                bot.send_message(message.chat.id,f"{pinger(get_msg[1])}")
        elif str(message.text.lower()).startswith("/tracert") or str(message.text.lower()).startswith("/traceroute"):
            get_msg = str(message.text.lower()).split(" ")
            print(get_msg)
            if len(get_msg)==1:
                bot.send_message(message.chat.id,f"Так а куда трассировка то?")
            else:
                bot.send_message(message.chat.id,f"Выполняю команду {message.text.lower()}")
                bot.send_message(message.chat.id,f"{tracert(get_msg[1])}")

        elif str(message.text.lower()).startswith("/nslookup") :
            get_msg = str(message.text.lower()).split(" ")
            print(get_msg)
            bot.send_message(message.chat.id,f"Выполняю команду {message.text.lower()}")
            print(len(get_msg))
            if len(get_msg)==1:
                bot.send_message(message.chat.id,f"Так а что резолвим то?")
            elif len(get_msg)==3:
                bot.send_message(message.chat.id,f"{nslookup(get_msg[1],get_msg[2])}")
            else:
                bot.send_message(message.chat.id,f"{nslookup(get_msg[1])}")

        elif str(message.text.lower()).startswith("/nmap"):
            get_msg = str(message.text.lower()).split(" ")
            print(get_msg)
            if len(get_msg)==1:
                bot.send_message(message.chat.id,f"Так а где смотрим порты то?")
            else:
                bot.send_message(message.chat.id,f"Выполняю команду {message.text.lower()}")
                bot.send_message(message.chat.id,f"{nmap(get_msg[1])}")
        else:
            bot.send_message(message.chat.id,f"Чё надо, хозяин?")
            bot.send_message(message.chat.id,f"Я умею делать трассировку:\n/tracert 8.8.8.8\nПинг:\n/ping 8.8.8.8\nNsLookUp:\n/nslookup host [ipdns,default 8.8.8.8]\nnmap:\nnmap 8.8.8.8")
        
        
    bot.polling()
# 
while True:
    telega_bot(token)