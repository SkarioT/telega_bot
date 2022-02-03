FROM python:3.9
WORKDIR /app
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install iputils-ping -y
RUN apt-get install traceroute -y
RUN apt-get install nmap -y
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD python main_bot.py