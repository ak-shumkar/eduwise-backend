FROM python:3.9-alpine

RUN mkdir /api
RUN mkdir /api/staticfiles
WORKDIR /api

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# install psycopg2, pillow, cffi dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev libffi-dev

RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN sed -i 's/\r$//g' /api/entrypoint.sh
RUN chmod +x /api/entrypoint.sh

COPY .. .

# See https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/