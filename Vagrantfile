# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "debian/jessie64"

  config.vm.network "forwarded_port", guest: 5000, host:5000
  config.vm.network "forwarded_port", guest: 27017, host:27017

  config.vm.provider :virtualbox do |vb|
      vb.name = "docker_vm_tutorial"
      config.vm.provision :shell, path: "bootstrap.sh"
      vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
end
