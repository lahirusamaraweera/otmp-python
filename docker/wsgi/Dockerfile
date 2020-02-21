FROM ubuntu:bionic

ENV DEBIAN_FRONTEND=noninteractive

RUN mkdir /code
WORKDIR /code

RUN apt update && \
    apt install -y apt-utils software-properties-common --fix-missing

# install phalcon 2.x
LABEL version.phalcon="2.0.9"
RUN apt install -y git \
                   libpcre3-dev \
                   gcc \
                   make \
                   npm \
                   python3-pip \
                   apache2 \ 
                   libapache2-mod-wsgi

RUN npm install npm@latest -g
RUN npm install -g @angular/cli

ADD ./apache.conf /docker/
RUN service apache2 stop && \
    rm /etc/apache2/sites-available/000-default.conf && \
    ln -s /docker/app/apache.conf /etc/apache2/sites-available/000-default.conf && \
    a2enmod rewrite wsgi

# #python dependancy installation
# COPY ../requirements.txt /docker/
# RUN pip install -r requirements.txt
