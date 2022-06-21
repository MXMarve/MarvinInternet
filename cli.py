import os

# -------------------------------------------- 

try:
  import Colorama
except:
  print("Installing Dependency: Colorama")
  os.system("pip3.9 install colorama 1>/dev/null")

try:
  import time
except:
  print("Installing Dependency: Time")
  os.system("pip3.9 install time 1>/dev/null")
try:
  import requests
except:
  print("Installing Dependency: Requests")
  os.system("pip3.9 install requests 1>/dev/null")
try:
  import scapy
except:
  print("Installing Dependency: Scapy")
  os.system("pip3.9 install scapy 1>/dev/null")
try:
  import wget
except:
  print("Installing Dependency: Wget")
  os.system("pip3.9 install wget 1>/dev/null")
try:
  import argparse
except:
  print("Installing Dependency: Argparse")
  os.system("pip3.9 install argparse 1>/dev/null")
try:
  import humanfriendly
except:
  print("Installing Dependency: HumanFriendly")
  os.system("pip3.9 install humanfriendly 1>/dev/null")

# --------------------------------------------
import threading
import time
import colorama
import requests
import scapy
import wget
import argparse
import colorama
import humanfriendly
from colorama import Fore
from signal import signal, SIGINT
from sys import exit

os.system("clear")
time.sleep(1)
logo = """
  ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
  ████╗ ████║██╔══██╗██╔══██╗██║   ██║██║████╗  ██║
  ██╔████╔██║███████║██████╔╝██║   ██║██║██╔██╗ ██║
  ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██║██║╚██╗██║
  ██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ██║██║ ╚████║
  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝
  DDoS v2                                               
"""

helpmenu = """
  HTTP URL
  ICMP IPV4
  SLOWLORIS IPV4/URL
  MEMCACHED IPV4/URL
  UDP IPV4

  If any methods give a shit ton of errors, and it says Name or service not known,
  try IPv4, if that didn't work, the ip doesn't work.

"""
print(Fore.RED + logo + Fore.BLUE)
print(Fore.MAGENTA+helpmenu+Fore.WHITE)

targetmethod = input("Method (CAPS MATTER): ")

if targetmethod == "ICMP":
    exec(open("icmp.py"()))
if targetmethod == "HTTP":
    exec(open("http.py"()))
if targetmethod == "MEMCACHED":
    exec(open("memcached.py"()))
if targetmethod == "SLOWLORIS":
    exec(open("slowloris.py"()))
if targetmethod == "SYN":
    exec(open("syn.py"()))
if targetmethod == "UDP":
    exec(open("udp.py"()))