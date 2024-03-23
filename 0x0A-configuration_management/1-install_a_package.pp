#instaaling flask verios 2.1.0 using puppet

package { 'python3':
  ensure   => '3.8.10',
  provider => 'apt',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
