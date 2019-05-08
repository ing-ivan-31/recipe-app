# base image
FROM python:3.7-alpine
MAINTAINER Ivan Sanchez

# postgres extension needed it
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

#show logs in docker
ENV PYTHONUNBUFFERED 1

# add and install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# set working directory
RUN mkdir -p /app
WORKDIR /app

# Copy app to docker container
COPY ./app /app

