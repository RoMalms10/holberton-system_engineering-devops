# Script that creates a manifest and kills a process named killmenow
exec { 'kill_the_things':
  path     => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command  => 'pkill killmenow',
  provider => 'shell',
}
