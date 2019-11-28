FROM python:3.7-alpine
MAINTAINER Philip Winnigton

WORKDIR /usr/src/app

COPY . .

RUN pip install pytest

RUN pytest

