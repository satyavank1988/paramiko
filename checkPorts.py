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
        print " you need to pass a file whihc contains ip, port protocol(tcp/udp)  list as below format"
        print "ip  port tcp/udp"
        sys.exit("1")

def sshCleint():tcp/udp
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
                with open("servers-port-status.txt",'rb') as serverlist:
                    for line in serverlist:
                        lines = line.split(' ')
                        ip = lines[0]
                        port = lines[1]
                        protocol = lines[2]
                        if protocol.upper() == 'TCP':
                            cmd = 'nc -vz -w 2 ' + ip + ' -p ' + port
                            stdin,stdout,stderr = ssh.exec_command(cmd)
                             port
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


