#!/usr/bin/env bash

echo "Update repos"
sudo apt-get update

echo "Install Git"
sudo apt-get install git

echo "Get the latest Docker package"
curl -sSL https://get.docker.com/ | sh

echo "Create the docker group and add your user"
sudo usermod -aG docker vagrant

echo "Get Docker Compose"
curl -L https://github.com/docker/compose/releases/download/1.4.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose

echo "Apply executable permissions to the binary"
chmod +x /usr/local/bin/docker-compose

echo "Clone repository"
git clone repo.git
