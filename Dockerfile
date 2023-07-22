FROM python:3.9-slim
# FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/


EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
