FROM python:3.10
EXPOSE 5002

# Создаем директории и копируем файлы
RUN mkdir -p /opt/services/bot/work-bot
WORKDIR /opt/services/bot/work-bot

RUN mkdir -p /opt/services/bot/work-bot/requirements
ADD requirements.txt /opt/services/bot/work-bot/

COPY . /opt/services/bot/work-bot/

# Устанавливаем зависимости, включая aiopg
RUN pip install -r requirements.txt

# Добавляем переменные окружения для конфигурации aiopg
ENV POSTGRES_DB your_database
ENV POSTGRES_USER your_user
ENV POSTGRES_PASSWORD your_password
ENV POSTGRES_HOST db
ENV POSTGRES_PORT 5432

# Команда для запуска приложения
CMD ["python", "/opt/services/bot/work-bot/main.py"]
