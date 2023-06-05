# pull official base image
FROM python:3.8.3-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
# set work directory
WORKDIR /django
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
COPY . .

CMD python manage.py migrate --noinput