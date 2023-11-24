#Using Puppet, install flask from pip3
#ensure pip3 package installed
package { 'python3-pip':
  ensure    => installed,
}

package { 'flask':
  ensure    => '2.1.0',
  provideri => 'pip3',
}
