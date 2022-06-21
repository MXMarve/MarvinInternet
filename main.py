import os
os.system("clear")
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
  os.system("python3 icmp.py")
if method1 == "HTTP":
  os.system("clear")
  os.system("python3 http.py")
if method1 == "MEMCACHED":
  os.system("clear")
  os.system("python3 memcached.py")
if method1 == "SLOWLORIS":
  os.system("clear")
  os.system("python3 slowloris.py")
if method1 == "SYN":
  os.system("clear")
  os.system("python3 syn.py")
if method1 == "UDP":
  os.system("clear")
  os.system("python3 udp.py")