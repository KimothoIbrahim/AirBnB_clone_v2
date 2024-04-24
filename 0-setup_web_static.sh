#!/usr/bin/env bash
# provision a server

apt-get update

ngx=$(which nginx)

if [ ! -e "$ngx" ]
then
    apt-get install nginx -y
else
    echo "nginx already installed"
fi

if [ ! -d "/data/web_static/releases/test/" ]; 
then
    mkdir -p /data/web_static/releases/test/
fi

if [ ! -d "/data/web_static/shared" ];
then
    mkdir -p /data/web_static/shared/
fi

echo "my simple static website" > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]
then
    echo "deleting old symlink '/data/web_static/current'"
    rm "/data/web_static/current"
fi 

echo "creating new symlink '/data/web_static/current'"
ln --symbol "/data/web_static/releases/test/" "/data/web_static/current"
echo "link created"

chown -R ubuntu:ubuntu /data/

str="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"

sed -i /^"\tserver_name _"/a\ "${str}" /etc/nginx/sites-available/default

nginx -t

service nginx reload
