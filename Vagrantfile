# -*- mode: ruby -*-
# vi: set ft=ruby :

# load machines configs
require 'yaml'
current_dir    = File.dirname(File.expand_path(__FILE__))
configs        = YAML.load_file("#{current_dir}/machines_configs.yml")
machines_configs = configs['configs']

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = machines_configs['server']['memory']
    vb.cpus = machines_configs['server']['cpus']
  end

  config.vm.synced_folder "app", "/vagrant/app"
  config.vm.network "private_network", ip: machines_configs['server']['ip']
  config.vm.network "forwarded_port", guest: 5002, host: 5002
  config.vm.hostname = machines_configs['server']['domain']
  
  # Run Ansible Roles
  config.vm.provision "ansible_local" do |ansible|
    ansible.install = true
    ansible.install_mode = :default
    ansible.playbook = "ansible/site.yml"
  end

  # config.vm.provision :shell, :inline => "python /vagrant/app/myapp.py", :privileged => false
  vagrant_synced_folder_default_type = ""
end

puts "-------------------------------------------------"
puts "Demo URL : http://#{machines_configs['server']['ip']}:5002/hello"
puts "-------------------------------------------------"
