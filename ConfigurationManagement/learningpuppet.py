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

#This code block includes a class with three resources, a package, a file, and a service. All of them are related to the Network Time Protocol, or NTP, the mechanism our computers use to synchronize the clocks. This code ensures that the NTP package is always upgraded to the latest version. We're setting the contents of the configuration file using the source attribute, which means that the agent will read the required contents from the specified location. And we're saying that we want the NTP service to be enabled and running. By grouping all of the resources related to NTP in the same class, we only need a quick glance to understand how the service is configured and how it's supposed to work. This would make it easier to make changes in the future since we have all the related resources together. It makes sense to use this technique whenever we want to group related resources. 
class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => 'puppet:///modules/ntp/ntp.conf'
    replace => true,
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
  }
}

# Puppet Resources
# https://puppet.com/docs/puppet/latest/lang_resources.html
# https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/

class AutoConfig {
  package { 'Executable':
    ensure => latest,
  }
  file { 'executable.cfg':
    source => 'puppet:///modules/executable/Autoconfig/executable.cfg'
    replace => true,
  }
  service { 'executable.exe':
    enable  => true,
    ensure  => running,
  }
}

# This code block is a Puppet manifest, which is a configuration file used to manage systems using the Puppet automation framework.
# The code you provided is an if statement. An if statement is a conditional statement that executes a block of code if a certain condition is met. In this case, the condition is whether the is_virtual fact is set to true. The is_virtual fact is a built-in fact that Puppet uses to determine if the node is a virtual machine.
# If the is_virtual fact is set to true, then the code in the if statement block will be executed. This code will purge the smartmontools package. The smartmontools package is a software package that provides tools for monitoring and managing hard drives. Purging the smartmontools package on a virtual machine is typically done to improve performance.

# If the is_virtual fact is set to false, then the code in the else statement block will be executed. This code will install the smartmontools package.

# In this code block, the value of the is_virtual fact is true, so the code in the if statement block will be executed. This means that the smartmontools package will be purged.
if $facts['is_virtual'] {
  package { 'smartmontools':
    ensure => purged,

  }
} else {
  package { 'smartmontools':
    ensure => installed,
  }
}

#This resource ensures that the /etc/issue file has a set of permissions and a specific line in it. Fulfilling this requirement is an idempotent operation. If the file already exists and has the desired content, then Puppet will understand that no action has to be taken. If the file doesn't exist, then puppet will create it. If the contents or permissions don't match, Puppet will fix them. No matter how many times the agent applies the rule, the end result is that this file will have the requested contents and permissions. 
file { '/etc/issue':
  mode    => '0644',
  content => "Internal system \l \n",
}


