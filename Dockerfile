FROM python:3

ENV PYTHONUNBUFFERED 1
ENV NODE_OPTIONS=--openssl-legacy-provider

RUN mkdir /code
WORKDIR /code

#python dependancy installation
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update

RUN python -m pip install gunicorn

#node and angular cli installation
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash
RUN apt install -y nodejs
RUN npm install -g @angular/cli

COPY . /code/

#nginix installation
RUN apt update && apt install -y nginx 
RUN service nginx stop && \
    rm /etc/nginx/sites-available/default  && \
    ln -s /code/docker/nginx/nginx_config /etc/nginx/sites-available/default
                