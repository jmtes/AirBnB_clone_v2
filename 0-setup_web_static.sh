#!/usr/bin/env bash
# Set up server for the deployment of the HBNB web static.
apt-get update && apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "pool's closed" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '/listen \[::\]:80 default_server ipv6only=on;/aadd_header X-Served-By $hostname;\nlocation /hbnb_static {\nalias /data/web_static/current/;\n}\nlocation /redirect_me {\nrewrite ^ https://www.youtube.com/watch?v=dJMVtwbriK0 permanent;\n}\n\nerror_page 404 /custom_404.html;\nlocation = /custom_404.html {\ninternal;\n}' /etc/nginx/sites-available/default
service nginx restart
