# Fix high amount of requests
file { '/etc/default/nginx':
  ensure  => file,
  content => "#This file is managed by puppet\n\nULIMIT=\"-n 4096\"\n",
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
}
