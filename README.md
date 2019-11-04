# Python-bottle and Apache setup in a vagrant-box using Ansible
Setup python-bottle and apache using ansible and vagrant

# How to run
Clone this repository then
```
vagrant up
```
Once the vagrant ready, ssh to it:
```
vagrant ssh
```
Inside the guest-machine run 
```
python /vagrant/app/app.py
```
In the host-machine's browser go to: 
```
http://192.168.0.173:5002/hello
```
Note: Using directory `app` in this repo to edit projects files also possible.
