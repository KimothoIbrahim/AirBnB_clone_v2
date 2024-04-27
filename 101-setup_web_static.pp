#setup server for deployment

package { 'nginx':
  ensure => 'installed'
}

file { '/data':
  ensure => 'directory',
  owner  => 'kimotho',
  group  => 'kimotho'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "This is my Website\n",
  require => File['/data']
}

file { '/data/web_static/shared/':
  ensure  => 'directory',
  require => File['/data']
}

file { '/data/web_static/current/':
  target  => '/data/web_static/releases/test/',
  require => File['/data']
}

exec { 'update_config':
  command => '/usr/bin/sed -i /^"\tserver_name _"/a\ "\\ \n\tlocation\
 /hbnb_static{\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default',
  notify  => Service['nginx'],
  require => Package['nginx']
}

service { 'nginx':
  ensure => 'running',
  enable => true
}
