#!/bin/bash

nginx -g "daemon off;" | uwsgi --ini /opt/rest_api/uwsgi.ini
