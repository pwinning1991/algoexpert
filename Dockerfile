FROM python:3.7

WORKDIR /usr/src/app

COPY . .

RUN pip install pytest

RUN pytest

