# Flask - Nginx - Docker
Flask - Nginx - Docker

# Docker Install
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
https://www.hostinger.web.tr/rehberler/ubuntu-docker-kurulumu

sudo apt-get update
sudo apt-get install docker-ce
sudo systemctl status docker

# Docker Command
### Build 
docker-compose build

### Up
docker-compose up -d

### Image Prune
docker image prune -a -f

### Log
dockor-compose logs

### Image Delete
docker rmi con_id

### Image Conteiner Delete
docker rm con_id

# Project Build

git clone git_repo_url

cd project_name

docker-compose build

docker-compose up -d

# Github Setup

Go to Settings -> Secrets -> Actions and add a new repository secret.

Add the following secrets one by one:

VPS_SSH_HOST — this the host IP address of your server.

VPS_SSH_USERNAME — this is the username from your user@ipaddress login.

VPS_SSH_SECRET — this is the private SSH key that you set up for GitHub access on your server.

VPS_SSH_PORT — this is the port number for SSH access. Typically, it’s port 22.

SSH_PASSPHRASE — this is the passphrase if you supplied any during creation of your SSH key.

PROJECT_PATH — This is the entire project path of your project’s root directory. For example, /home/username/path/to/your/projectrootdirectory