# create a file.

file { '/tmp/school':
ensure  => 'present',
content => 'I love Pupper',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}
