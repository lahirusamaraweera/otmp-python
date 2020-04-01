FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

#python dependancy installation
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN apt-get update

RUN python -m pip install gunicorn

#npm an angular-cli installation
RUN apt-get install -y npm
RUN npm install npm@latest -g
RUN npm install -g @angular/cli
COPY . /code/
