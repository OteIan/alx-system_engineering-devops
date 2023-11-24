# Execute a command
exec { 'Kill_process' :
  command => 'usr/bin/pkill killmenow',
  onlyif  => 'usr/bin/pgrep killmenow',
  }
