#!/bin/sh
sudo apt install python3.9
echo Updating...
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
echo Updating Dependencies...
python3.9 get-pip.py
sudo rm get-pip.py
pip3.9 install -r requirements.txt
echo Starting...
python3.9 main.py