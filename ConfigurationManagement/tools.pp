#installation sudo apt install puppet-master(ubuntu) , puppetserver (debian)
#sudo nano /etc/default/puppetserver for memory allocation JAVA_ARGS="-Xms2g -Xmx2g -Djruby.logger.class=com.puppetlabs.jruby_utils.jruby.Slf4jLogger"
package { 'htop':
  ensure => present,
}
#sudo puppet apply -v tools.pp
