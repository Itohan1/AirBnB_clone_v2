#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment

nginx_path="/etc/nginx"
data_folder="/data"
data_static="$data_folder/web_static"
data_releases="$data_static/releases"
#data_shared="$data_static/shared"
#data_test="$data_releases/test"
fake_html="$data_test/index.html"
data_current="$data_static/current"

if [ ! -e "$nginx_path" ]; then
        sudo apt-get update
        sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo chown -R ubuntu:ubuntu "$data_folder"
html_content='<html>
        <head>
        </head>
        <body>
                Holberton School
        </body>
</html>'
echo "$html_content" | sudo tee "$fake_html"
sudo ln -sf "$data_test" "$data_current"

sudo sed -i '/server_name_;/a \\tlocation /hbnb_static/ {\n\t\t alias '"$data_current"';\n\t}' /etc/nginx/sites-available/default

sudo service nginx restart

