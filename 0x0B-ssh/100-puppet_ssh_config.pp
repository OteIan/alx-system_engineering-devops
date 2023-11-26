#!/usr/bin/pup
# Configure the SSH server to refuse authentication with a password
include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/sshd_config',
  line    => '	PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/sshd_config'
  line    => '	IdentityFile ~/.ssh/school'
  replace => true,
}
