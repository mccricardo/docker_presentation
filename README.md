Docker Presentation
===============

Vagrant setup to build a VM for our presentation.

# Dependencies

 * [VirtualBox](https://www.virtualbox.org/)
 * [Vagrant](http://www.vagrantup.com/)

# How to setup

Create folder to host setup:

    mkdir /path/to/host/files


Clone repository:

    cd /path/to/host/files
    git clone https://github.com/mccricardo/docker_presentation.git


Start you VM and install dependencies:

	vagrant up

# Notes
 * The first time you run **vagrant up** all the setup up and provision will be done. This might take a while. Please be patient. If possible, perform the setup before the presentation.
