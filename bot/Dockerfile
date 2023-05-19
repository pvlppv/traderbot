FROM python:slim
COPY . /trader-bot
COPY ../.env /trader-bot
WORKDIR /trader-bot/
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r requirements.txt