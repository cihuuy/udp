import os
import subprocess
import getpass
import json
import urllib.request
import time

#@title **Create User**
#@markdown Enter Username and Password

username = "zoy" #@param {type:"string"}
password = "wiro212" #@param {type:"string"}

print("Creating User and Setting it up")

# Creation of user
os.system(f"useradd -m {username}")

# Add user to sudo group
os.system(f"adduser {username} sudo")
    
# Set password of user
os.system(f"echo '{username}:{password}' | sudo chpasswd")

# Change default shell from sh to bash
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

print("User Created and Configured")

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
    
# Set root password
os.system(f"echo root:{password} | chpasswd")
os.system("mkdir -p /var/run/sshd")
os.system("echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config")
os.system("echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config")
os.system("echo 'LD_LIBRARY_PATH=/usr/lib64-nvidia' >> /root/.bashrc")
os.system("echo 'export LD_LIBRARY_PATH' >> /root/.bashrc")
 
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
 
# Print root password
print(f'Root password: {password}')
