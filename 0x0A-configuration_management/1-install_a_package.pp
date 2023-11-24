#Using Puppet, install flask from pip3
#it must be version 2.1.0

package { 'flask':
  ensure    => '2.1.0',
  provideri => 'pip3',
}
