FROM python:3.10
EXPOSE 5012

# Создаем директории и копируем файлы
RUN mkdir -p /opt/services/bot/work-bot
WORKDIR /opt/services/bot/work-bot

RUN mkdir -p /opt/services/bot/work-bot/requirements
ADD requirements.txt /opt/services/bot/work-bot/

COPY . /opt/services/bot/work-bot/

# Устанавливаем зависимости, включая asyncpg
RUN pip install -r requirements.txt

# Удаляем предыдущие переменные окружения для PostgreSQL, они теперь задаются в Docker Compose
ENV POSTGRES_DB "OSOR_DB"
ENV POSTGRES_USER "postgres"
ENV POSTGRES_PASSWORD "238484"
ENV POSTGRES_HOST "localhost"
ENV POSTGRES_PORT "5432"

# Команда для запуска приложения
CMD ["python", "/opt/services/bot/work-bot/main.py"]
