
import paramiko
import getpass
import subprocess


def inputServer():
    return raw_input("Remote Server : "),raw_input("Enter UserName : "),getpass.getpass("Enter Password : ")
    #server = raw_input("Remote Server : ")
    #user = raw_input("Enter UserName : ")
    #password  = getpass.getpass("Enter Password : ")
    #return server,user, password

def inputCommand():
    return  raw_input("Enter commands : ")

def sshClient():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    server,user,passwd = inputServer()
    try:
        ssh.connect(server, username=user, password=passwd, timeout=10)
        while True:
           # cmd = inputCommand()
            stdin, stdout,stderr =  ssh.exec_command(inputCommand())
            print stdout.channel.recv('2024')

    except IOError as err:
        print err


#print inputServer()
#print inputCommands()

sshClient()


