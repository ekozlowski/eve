# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider "virtualbox" do |v|
  v.customize ["modifyvm", :id, "--cpus", "2", "--memory", "2048"]
end
  config.vm.define "eve" do |eve|
    eve.vm.network "private_network", ip: "192.168.50.10"
    #eve.vm.network "forwarded_port", guest: 8080, host: 8080
    #eve.vm.network "forwarded_port", guest: 15672, host: 15672
    eve.vm.hostname = "eve.khome"
    eve.vm.box = "trusty64"
    eve.vm.box_url = "http://files.vagrantup.com/trusty64.box"
  end


  # -------- Enable provisioning with Ansible.  --------
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    # Uncomment below to see debug output.
    ansible.verbose = 'v'
    ansible.groups = {
        "eveservers" => ["eve"]
    }
  end
end