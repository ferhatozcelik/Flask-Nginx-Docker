# Face-Compare
Face Compare API

# Docker Install
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
https://www.hostinger.web.tr/rehberler/ubuntu-docker-kurulumu

sudo apt-get update
sudo apt-get install docker-ce
udo systemctl status docker

## Build 
docker-compose build

## Up
docker-compose up -d

## Image Prune
docker image prune -a -f

## Log
dockor-compose logs

## Image Delete
docker rmi con_id

## Image Conteiner Delete
docker rm con_id