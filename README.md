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


# ________________________________
Auto-run bot:
      1)sudo vi /etc/systemd/system/telegabot.service

      2):
      [Unit]
      # After=network.service
      Description=My App

      [Service]
      Type=simple
      # WorkingDirectory=/code/python/myapp
      ExecStart=/home/ubuntu/telega_bot/telegabot.sh


      [Install]
      WantedBy=multi-user.target
      # WantedBy=default.target

      3)vi /home/ubuntu/telega_bot/telegabot.sh

      #!/bin/bash

      source /home/ubuntu/telega_bot/env/bin/activate
      python3 /home/ubuntu/telega_bot/main_bot.py >> /home/ubuntu/telega_bot/logs/telegabot.log 2>&1


      4) mkdir /home/ubuntu/telega_bot/logs

      5) sudo chmod 777 /home/ubuntu/telega_bot/telegabot.sh
         sudo chmod 777 /etc/systemd/system/telegabot.service

      6)
      sudo systemctl daemon-reload
      sudo systemctl enable telegabot.service

      sudo systemctl start telegabot.service

      sudo systemctl status telegabot.service

      #original guide https://code.luasoftware.com/tutorials/linux/auto-start-python-script-on-boot-systemd/

      #alias telega='sudo systemctl status telegabot.service'

      #alias telega.log='cat ./telega_bot/logs/telegabot.log'


or Auto-run on docker:
   1) docker build -t telega_skariot_net-tools_bot .
   2) docker push telega_skariot_net-tools_bot
   3) docker-compose up -d