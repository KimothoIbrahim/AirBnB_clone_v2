#!/usr/bin/env bash
# provision a server

sudo apt-get update

ngx=$(which nginx)

if [ ! -e "$ngx" ]
then
    sudo apt-get install nginx -y
else
    sudo echo "nginx already installed"
fi

if [ ! -d "/data/web_static/releases/test/" ]; 
then
    sudo mkdir -p /data/web_static/releases/test/
fi

if [ ! -d "/data/web_static/shared" ];
then
    sudo mkdir -p /data/web_static/shared/
fi

echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]
then
    echo "deleting old symlink '/data/web_static/current'"
    sudo rm "/data/web_static/current"
fi 

echo "creating new symlink '/data/web_static/current'"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
echo "link created"

sudo chown -R ubuntu:ubuntu /data/

str="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

#sudo sed -i /^"\tserver_name _"/a\ "${str}" /etc/nginx/sites-available/default
sudo sed -i '13i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo nginx -t

sudo service nginx reload
