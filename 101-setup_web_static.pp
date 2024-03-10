#sets up your web servers for the deployment
-> exec {'sudo apt-get -y update':
  provider => shell,
}

-> exec {'sudo apt-get -y install nginx':
  provider => shell,
}

-> file { '/data':
  ensure => 'directory',
}

-> file { '/data/web_static':
  ensure => 'directory',
}

-> file { '/data/web_static/releases':
  ensure => 'directory',
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory',
}

-> file { '/data/web_static/shared':
  ensure => 'directory',
}

-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Holberton School\n",
}

-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
}

-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}

-> file { '/var/www':
  ensure => 'directory'
}

-> file { '/var/www/html':
  ensure => 'directory'
}

-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "Hello World!"
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page"
}

-> exec {'/etc/nginx/sites-available/default':
  ensure => 'present',
  command  => "sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;} /etc/nginx/sites-enabled/default",
}

-> exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
