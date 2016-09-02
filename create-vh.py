#! /usr/bin/env python3

import sys
import os

sitename = sys.argv[1]
root = ''
user = os.getenv('SUDO_USER')

if len(sys.argv) == 3:
	root = '/' + sys.argv[2]

string = """
    <VirtualHost 127.0.0.1:80>
        ServerAdmin admin@{0}
        DocumentRoot "/home/{2}/www/{0}{1}
        ServerName {0}
        ServerAlias www.{0}
        ErrorLog "/opt/lampp/logs/{0}-error_log"
        CustomLog "logs/{0}-access_log" common
        <Directory />
        AllowOverride All
        Require all granted
        </Directory>
    </VirtualHost>\n""".format(sitename, root, user)

print('Creating a virtual host ...')
try:
    f = open('/opt/lampp/etc/extra/httpd-vhosts.conf', 'a')
    f.write(string)
finally:
    f.close()

print('Add the virtual host to hosts file ...')

try:    
    f = open('/etc/hosts', 'a')
    f.write('\n127.0.0.1\t' + sitename)
finally: 
    f.close()

print('Virtual host \'' + sitename + '\' successfully created.')
