# POC - Django Docker MYSQL CURD Application

## Installation

We need docker and docker compose installed. So let's install them first.

```bash
sudo apt-get update
sudo apt install docker.io

sudo curl -L "https://github.com/docker/compose/releases/download/1.25.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Build the images

``` bash
sudo docker-compose build
```
## Run docker containers

``` bash
sudo docker-compose up
```
Note : django app will automatically starts with this. you can access by visiting http://localhost:8000

## Login to the web_app conatiner
```bash
sudo docker exec -it <contaner_name> bash   
```
in this case container will be otmp_web_1

## Django create APP

``` bash
python manage.py createapp <app_name>
```

## To update the file permissions

Once you create a django app in the docker conatiner, you will not be able to edit the fiels since docker conatiners are running as root. so you can use following commandto update file permission.

```bash
sudo chown -R $USER:$USER .
```


## How to run angular application

To run front end angular application

1. Login to the container
```bash
sudo docker exec -it <contaner_name> bash 
# in our case container name will be otmp_web_1 , accordingly command will be as follows
sudo docker exec -it otmp_web_1 bash  
```
2. change the path to /front
```bash
cd front
```
3. run the app
```bash
ng serve --host 0.0.0.0
```
4. now you can visit the anguar app in http://localhost:4201


# Running the django app using Gunicorn - PROD

```bash
cd /code
gunicorn -b 0.0.0.0:80 otmp.wsgi:application
```