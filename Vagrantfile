# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "ubuntu/14.04"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  # Networking
  config.vm.hostname = "api.sitrep.com"
  config.vm.network "private_network", ip: "192.168.93.10"
  config.vm.network :forwarded_port, guest: 80, host: 8080

  # Chef
  config.vm.provision :chef_solo do |chef|
      chef.cookbooks_path = "./cookbooks"
      chef.add_recipe("sitrep")
  end

  config.vm.synced_folder ".", "/repo", id: "repo-folder", owner: "vagrant", group: "vagrant"
end
