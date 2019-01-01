import paramiko
import getpass
import logging
import sys
import os
import socket


def getArgument():
    try:
        if len(sys.argv[1]) >  0:
            return sys.argv[1]
    except:
        print "Argument not passed"
        sys.exit("1")

def sshCleint():
    server = getArgument()
    user = raw_input("Enter user Name : ")
    password = getpass.getpass("Enter Password : ")
    with open(server, 'rb') as file:
        for host in file:
            host = str(host).replace('\n','')
            ssh = paramiko.SSHClient()
#               print host,user,password
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(host, username=user, password=password, timeout=15)
                stdin, stdout, stderr = ssh.exec_command('uptime')
                tmp = stdout.channel.recv('1024')
                print tmp
                ssh.close()
            except paramiko.AuthenticationEixception as error:
                print "Error while authenticating", error
            except IOError as error:
                print "Error hostname ",error
            except socket.timeout as error:
                print "Unable to conect ", error
   #         stdin, stdout, stderr = ssh.exec_command('uptime')
   #         tmp = stdout.channel.recv('1024')
   #         print tmp
   #         ssh.close()


#print getArgument()
sshCleint()


