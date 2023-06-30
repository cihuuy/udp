import os
import subprocess
import getpass
import json
import urllib.request
import time

#@title **RDP**
#@markdown It takes 4-5 minutes for installation
    
class CRD:
    def __init__(self):
        os.system("apt update")
        self.installSSH()

    @staticmethod
    def installSSH():
        print("Installing openssh")
        subprocess.run(['wget', 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip'], stdout=subprocess.PIPE)
        subprocess.run(['unzip', '-qq', '-n', 'ngrok-stable-linux-amd64.zip'], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '-qq', '-o=Dpkg::Use-Pty=0', 'openssh-server', 'pwgen'], stdout=subprocess.PIPE)   

# Run sshd in the background
os.system('/usr/sbin/sshd -D &')
time.sleep(2)  # Add a small delay to ensure SSH is fully started

# Static ngrok authentication token
authtoken = "2RIDE4oxtvtFSHR9Ea1dI3BZnZo_4hoNaQK6cLt3j3WHpjc9E"

# Create tunnel
os.system(f'./ngrok authtoken {authtoken} && ./ngrok tcp 22 &')
 
# Get public address and print connect command
time.sleep(5)  # Add a delay to allow ngrok to establish the tunnel
with urllib.request.urlopen('http://localhost:4040/api/tunnels') as response:
    data = json.loads(response.read().decode())
    host, port = data['tunnels'][0]['public_url'][6:].split(':')
    print(f'SSH command: ssh -p{port} root@{host}')

