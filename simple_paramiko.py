import paramiko
import getpass
import logging
import sys
import os



def getArgument():
    try:
        if len(sys.argv[1]) >  0:
            return sys.argv[1]
    except:
        print "Argument not passed"
        sys.exit("1")

def sshCleint():
    server = getArgument()
    password = getpass.getpass("Enter Password : ")
    while True:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username='satyavak', password=password)
        stdin, stdout, stderr = ssh.exec_command('uptime')
        tmp = stdout.channel.recv('1024')
        print tmp
        ssh.close()


print getArgument()
sshCleint()


