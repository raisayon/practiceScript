# This block of code is saying that the package 'sudo' should be present on every computer where the rule gets applied. If this rule is applied on 100 computers, it would automatically install the package in all of them. This is a small and simple block but can already give us a basic impression of how rules are written in puppet. 
class sudo {
 
  package { 'sudo':
    ensure => present,
  }

}
