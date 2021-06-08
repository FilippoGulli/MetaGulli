import os
import source as sc
import multi as m
from termcolor import colored
import socket
from urllib2 import urlopen


#setup
#start

if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
else:
 sc.banner_init()
 sc.cho()





#print the quest
 choi = input("Enter the payload type number:")
#control if it is valid
 if choi > 4 or choi < 1:
        while (choi > 3 or choi < 1):
         sc.cho()
         choi = input("Enter the payload type number:")


#start the long elif or use a function

 if choi == 1:
     sc.plat(sc.final[0])

 if choi == 2:
     sc.plat(sc.final[1])

 if choi == 3:
     m.plat()

 if choi == 4:
     sc.plat(sc.final[3])








