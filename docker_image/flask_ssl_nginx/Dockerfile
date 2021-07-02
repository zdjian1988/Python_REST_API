FROM nginx:latest

MAINTAINER Ardur <zdjian@wingene.com.tw>

COPY nginx.conf /etc/nginx/
COPY my_nginx.conf /etc/nginx/sites-available/
COPY ssl.csr /etc/nginx/
COPY ssl.key /etc/nginx/

RUN mkdir -p /etc/nginx/sites-enabled/ \
    && ln -s /etc/nginx/sites-available/my_nginx.conf /etc/nginx/sites-enabled/
