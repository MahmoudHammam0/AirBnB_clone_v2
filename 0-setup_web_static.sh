#!/usr/bin/env bash
#sets up my web servers for the deployment
apt-get update
apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -HR ubuntu:ubuntu /data/
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
echo "
server {
	listen 80;

	location /hbnb_static {
		alias /data/web_static/current/;
		index index.html;
	}
}" | sudo tee /etc/nginx/sites-available/hbnb_static > /dev/null
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -sf /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/
sudo service nginx restart
