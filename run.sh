#!/bin/sh
sudo apt install python3-wget python3-humanfriendly -y 1>/dev/null
pip3 install -r requirements.txt 1>/dev/null
python3 main.py