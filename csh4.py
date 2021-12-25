#@title **Create User**
#@markdown Enter Username and Password

username = "zoy" #@param {type:"string"}
password = "wiro212" #@param {type:"string"}

print("Creating User and Setting it up")

# Creation of user
os.system(f"useradd -m {username}")

# Add user to sudo group
os.system(f"adduser {username} sudo")
    
# Set password of user to 'root'
os.system(f"echo '{username}:{password}' | sudo chpasswd")

# Change default shell from sh to bash
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

print("User Created and Configured")
 
    #@title **RDP**
#@markdown  It takes 4-5 minutes for installation
    
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
    
 
#Set root password
echo root:$password | chpasswd
mkdir -p /var/run/sshd
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc
echo "export LD_LIBRARY_PATH" >> /root/.bashrc
 
#Run sshd
get_ipython().system_raw('/usr/sbin/sshd -D &')
 
#Ask token
print("Copy authtoken from https://dashboard.ngrok.com/auth")
authtoken = getpass.getpass()
 
#Create tunnel
get_ipython().system_raw('./ngrok authtoken $authtoken && ./ngrok tcp 22 &')
 
#Get public address and print connect command
with urllib.request.urlopen('http://localhost:4040/api/tunnels') as response:
  data = json.loads(response.read().decode())
  (host, port) = data['tunnels'][0]['public_url'][6:].split(':')
  print(f'SSH command: ssh -p{port} root@{host}')
 
#Print root password
print(f'Root password: {password}')
