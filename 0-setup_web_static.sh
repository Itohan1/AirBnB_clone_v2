#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment

nginx_path="/etc/nginx"
if [ ! -e "$nginx_path" ]; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data
html_content='<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>'
echo "$html_content" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo sed -i '/server_name_;/a \\tlocation /hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

