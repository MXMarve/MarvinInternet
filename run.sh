#!/bin/sh
echo Updating Requirements...
sudo apt install python3-wget python3-humanfriendly 1>/dev/null
pip3 install -r requirements.txt 1>/dev/null
echo Done
python3 main.py