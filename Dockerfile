FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev postgresql-client

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./app ./app
COPY ./entrypoint.sh ./entrypoint.sh

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]