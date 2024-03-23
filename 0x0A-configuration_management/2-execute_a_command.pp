exec { 'killmenow':
  command     => '/usr/bin/pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}
