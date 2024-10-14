FROM python:3.11
WORKDIR /usr/src/app/backend
COPY . .
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Команда запуска контейнера
ENTRYPOINT ["/entrypoint.sh"]
