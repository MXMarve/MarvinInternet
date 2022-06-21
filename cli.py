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
import time
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
print(Fore.MAGENTA + helpmenu + Fore.WHITE)

method1 = input("Method (CAPS MATTER): ")

if method1 == "ICMP":
    exec(open("icmp.py").read())
    os.system("clear")
if method1 == "HTTP":
    exec(open("http.py").read())
    os.system("clear")
if method1 == "MEMCACHED":
    exec(open("memcached.py").read())
    os.system("clear")
if method1 == "SLOWLORIS":
    exec(open("slowloris.py").read())
    os.system("clear")
if method1 == "SYN":
    exec(open("syn.py").read())
    os.system("clear")
if method1 == "UDP":
    exec(open("udp.py").read())
    os.system("clear")