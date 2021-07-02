FROM ubuntu:latest

MAINTAINER Ardur <zdjian@wingene.com.tw>

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y build-essential git htop vim python3 python3-dev python3-pip curl openssl \
    && apt-get autoremove -y 

RUN ln -fs /usr/share/zoneinfo/Asia/Taipei /etc/localtime \
    && DEBAIN_FRONTEND=noninteractive apt-get -y install nginx

EXPOSE 443

COPY . /root/

RUN mkdir /mnt/socket \
    && mkdir /mnt/logs \
    && mv /root/rest_api /opt/ \
    && mv /root/nginx/nginx.conf /etc/nginx/ \
    && mv /root/nginx/my_nginx.conf /etc/nginx/sites-available/ \
    && mv /root/nginx/ssl.csr /etc/nginx/ \
    && mv /root/nginx/ssl.key /etc/nginx/ \
    && mkdir -p /etc/nginx/sites-enabled/ \
    && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/ \
    && service nginx restart \
    && python3 -m pip install -r /opt/rest_api/requirements.txt

WORKDIR /opt/rest_api

CMD ["/bin/bash", "-c", "/opt/rest_api/start_up.sh"]
