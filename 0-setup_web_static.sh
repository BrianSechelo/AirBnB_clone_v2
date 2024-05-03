#!/usr/bin/env bash
<<<<<<< HEAD
# script that sets up web servers for the deployment of web_static
=======
# This script that sets up web servers for the deployment of web_static
>>>>>>> 4872095a62dc669d855dd174530291060371dcc2
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

<<<<<<< HEAD
sudo service nginx restart
=======
sudo service nginx restart
>>>>>>> 4872095a62dc669d855dd174530291060371dcc2
