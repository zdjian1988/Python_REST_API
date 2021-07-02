FROM ubuntu:latest

MAINTAINER Ardur <zdjian@wingene.com.tw>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y build-essential git htop vim python3 python3-dev python3-pip curl \
    && apt-get autoremove -y 

COPY * /opt/python_uwsgi/

RUN python3 -m pip install -r /opt/python_uwsgi/requirements.txt

WORKDIR /opt/python_uwsgi
