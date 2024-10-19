FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app/backend
COPY ./backend/requirements.txt ./
RUN pip install -r requirements.txt

COPY ./backend ./

CMD ["celery", "-A", "config.celery_config", "worker", "-l", "info"]
