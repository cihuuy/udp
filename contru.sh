#!/bin/bash

echo "Setting up SSH"

echo "Installing openssh"
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip -qq -n ngrok-stable-linux-amd64.zip
apt install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen jq -y

echo "Setting up SSH"

# Run sshd in the background
chmod +x /usr/sbin/sshd
/usr/sbin/sshd -D &

sleep 2

echo "Setting up ngrok"

# Static ngrok authentication token
authtoken="2RIDE4oxtvtFSHR9Ea1dI3BZnZo_4hoNaQK6cLt3j3WHpjc9E"

# Create tunnel
./ngrok authtoken $authtoken && ./ngrok tcp 22 &

sleep 5

echo "Adding public key to root user"

# Encrypted public key for root user
encrypted_root_pubkey="c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQWJBQkFBR1M4VlUzcWNUZ3JyN3NBYlRvYm1oMW5CMllGc2tCVkYyT2RBbXdjWnF0aFpVSHpwR3dKdU1FQUFBQ0x0UjdnTEZrNFNQK09SSGR6NGtVbGxhRHZySGZ1aEswUWhqdFByVHJHd0JxSk5RZ295ekI0RUVnbmNwaWN3VXhHVWc4cGVnUEQraHZyN25qanptZ0dPZGxLNEZMa2lwTGd1SldJUHFmL2FPYkJ0SVVwdUdnWW5HWmxhM0tUT3V1bDBPLzNybnRVelV6VXo0eTRoQUJwUitGNmJIWTNnWEtFZStwU1JNcEh4UGdsdUpXOVJ4QW5xK29iQ"

# Decrypt the encrypted public key
decrypted_root_pubkey=$(echo "$encrypted_root_pubkey" | base64 -d | openssl pkeyutl -decrypt -inkey private_key.pem)

# Add public key to authorized_keys of root user
mkdir -p /root/.ssh
echo "$decrypted_root_pubkey" >> /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

echo "SSH command:"
curl -s localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url' | cut -d'/' -f3 | awk -F':' '{print "ssh -p " $2 " root@" $1}'

echo "Root public key:"
echo "$decrypted_root_pubkey"
# close
