#!/bin/bash
sudo apt-get update -y
sudo apt-get install xfce4 xfce4-terminal -y
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
sudo dpkg -i chrome*
sudo apt-get install -f
