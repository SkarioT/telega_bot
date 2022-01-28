# telega_bot
Telegram bot 4 networking test
1) ping [host]
2) tracert [host]
3) nslookup [host] [dns_server]
4) nmap [host]


If error:
AttributeError: 'TeleBot' object has no attribute 'message_handler'

Commad for fix:
pip3 uninstall telebot
pip3 uninstall PyTelegramBotAPI
pip3 install pyTelegramBotAPI
pip3 install --upgrade pyTelegramBotAPI