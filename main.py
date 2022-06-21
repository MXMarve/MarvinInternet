import os
os.system("clear")
# -------------------------------------------- 
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
try:
  import colorama
except:
  print("Installing Dependency: Colorama")
  os.system("pip3.9 install colorama 1>/dev/null")


# --------------------------------------------

import time
from colorama import Fore
os.system("clear")
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
print(Fore.LIGHTYELLOW_EX + helpmenu + Fore.BLUE)
method1 = input("Method (CAPS MATTER): ")
if method1 == "ICMP":
  os.system("clear")
  os.system("python3.9 icmp.py")
if method1 == "HTTP":
  os.system("clear")
  os.system("python3.9 http.py")
if method1 == "MEMCACHED":
  os.system("clear")
  os.system("python3.9 memcached.py")
if method1 == "SLOWLORIS":
  os.system("clear")
  os.system("python3.9 slowloris.py")
if method1 == "SYN":
  os.system("clear")
  os.system("python3.9 syn.py")
if method1 == "UDP":
  os.system("clear")
  os.system("python3.9 udp.py")