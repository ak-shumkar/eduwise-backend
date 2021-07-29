FROM python:3.9
ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /backend

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --deploy --system

COPY . .