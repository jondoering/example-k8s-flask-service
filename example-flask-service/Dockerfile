#https://github.com/tiangolo/uwsgi-nginx-flask-docker
FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install flask-restful

#change port from 80 to 5000 -> does not work
#ENV LISTEN_PORT 5000
#EXPOSE 5000

#set uwsgi.ini path
ENV UWSGI_INI /app/uwsgi.ini

#set min=2 processes, max 16
ENV UWSGI_CHEAPER 2
ENV UWSGI_PROCESSES 16

COPY ./app /app
