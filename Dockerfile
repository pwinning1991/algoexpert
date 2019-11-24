FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install pytest

RUN pytest

