#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment

if ! [ -x "$(command -v nginx)" ]; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi
sudo service nginx start
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server_name_;/a \n\tlocation /hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

