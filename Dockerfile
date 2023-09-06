FROM python:3.10
EXPOSE 5002
RUN mkdir -p /opt/services/bot/work-bot
WORKDIR /opt/services/bot/work-bot

RUN mkdir -p /opt/services/bot/work-bot/requirements
ADD requirements.txt /opt/services/bot/work-bot/

COPY . /opt/services/bot/work-bot/

RUN pip install -r requirements.txt
CMD ["python", "/opt/services/bot/work-bot/main.py"]