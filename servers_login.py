#!/usr/bin/env python
import pexpect


with open('server_list.txt','r') as file:
	for line in file:
		

def connection(host,pass):
	ssh_newkey = 'Are you sure you want to continue connecting'
	# my ssh command line
	cmd = 'ssh ' + 'satyavak@'+host
	pass = 'System!23'
	p=pexpect.spawn('ssh satyavak@ops-dev2.sv4.ironport.com uname -a')
	i=p.expect([ssh_newkey,'password:',pexpect.EOF])
	if i==0:
	    print "I say yes"
	    p.sendline('yes')
	    i=p.expect([ssh_newkey,'password:',pexpect.EOF])
	if i==1:
	   # print "I give password",
	    p.sendline(pass)
	    p.expect('~]$')
	    out = p.sendline('cat /etc/*ele*')
	    print "version",out
	
	    p.expect(pexpect.EOF)    
	elif i==2:
	    print "I either got key or connection timeout"
	    pass
	print p.before # print out the result
	print p.after


with open('server_list.txt','r') as file:
	for line in file:
		host = 
