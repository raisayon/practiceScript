# This block of code is saying that the package 'sudo' should be present on every computer where the rule gets applied. If this rule is applied on 100 computers, it would automatically install the package in all of them. This is a small and simple block but can already give us a basic impression of how rules are written in puppet. 
#puppet agent (client), puppet master (server)
class sudo {
 
  package { 'sudo':
    ensure => present,
  }

}

#Here a file resource is defined. This is used for managing files and directories. This block of code ensures that  /etc/sysctl.d exists and is a directory.
class sysctl {

  # Make sure the directory exists, some distros don't have it
  file { '/etc/sysctl.d':
    ensure => directory,
  }

}

# In this code block, we are configuring the contents of /etc/timezone.This will be a file, and the contents of the file will be set to the UTC timezone. We also set the replace attribute to true which means even if the contents of the file already exist, they will  be replaced.
class timezone {

      file { '/etc/timezone':
        ensure  => file,
        content => "UTC\n",
        replace => true,
      }

}
