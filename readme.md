# Online Transpot Management Platform

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

## Login to the  web_app conatiner
```
sudo docker exec -it <contaner_name bash   
```
in this case container will be otmp_web_1

## Django create APP

``` bash
python manage.py createapp <app_name>
```

## To update the file permissions

Once you create a app in the docker conatiner, you will not be able to edit the fiels since docker conatiners are running as root. so you can use following commandto update file permission.

```bash
sudo chown -R $USER:$USER .
```
