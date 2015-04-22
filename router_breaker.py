#!/usr/bin/env python
# @author: Yosi Dahan

import urllib2
import re
import os
import time
from netaddr import *
import sys

print ''
startIp = raw_input('>> Start IP address in format like 10.0.0.0/20 : ')
ip = IPNetwork(startIp)

print '\n[*] Generated', len(ip) ,'IP addresses.'
print '>> First IP address:', ip[0]
print '>> Last IP address:', ip[len(ip)-1] ,'\n'

print 'Started scanning routers with admin:admin credentials...\n\n'

for ipadd in ip:
 	print '>> Checking', ipadd,'...'
 	urlt = 'http://'+str(ipadd)

	username = 'admin'
	password = 'admin'
	
	try:

		passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
		passman.add_password(None, urlt, username, password)
		authhandler = urllib2.HTTPBasicAuthHandler(passman)
		opener = urllib2.build_opener(authhandler)
		urllib2.install_opener(opener)
		response = urllib2.urlopen(urlt,timeout=3)

	except urllib2.URLError:
		print "\033[91m[!] Timeout or not a router\033[0m\n"
		continue
	
	print "\033[94m[*]",response.getcode(),"Found a router\033[0m\n"
	 