#!/usr/bin/python3

#importing required libraries
import argparse, socket

#our tool description
parser=argparse.ArgumentParser(description="nws tool")


#compulsary to provide domain name or ip
parser.add_argument("-host",type=str,required=True,help="type pass host name or ip")

#adding the arguments
parser.add_argument("-s",type=str,required=False,help="type pass the port number")
parser.add_argument("-m",type=str,required=False,help="type port numbers ex 22,28,30")
parser.add_argument("-r",type=str,required=False,help="type port range ex 21-30")
parser.add_argument("-l",type=str,required=False,help=" provide port list file ex list.txt")

a=parser.parse_args()

#function to check the port is open or closed
def run(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((a.host,port))
        sock.close()
        return True
    except:
        return False
#for single port number
try:
    b=a.s.split()
    for i in b:
        if run (int(i)):
            print("port {} is open".format(i))
        else:
            print("port {} is closed".format(i))
except:
    pass
#for multiple port numbers
try:
    c=a.m.split(",")
    for i in c:
        if run (int(i)):
            print("port {} is open".format(i))
        else:
            print("port {} is closed".format(i))
except:
    pass
#for the range of port numbers
try:
    d=a.r.split("-")
    x=int(d[0])
    y=int(d[1])+1
    e=range(x,y)
    for i in e:
        if run (int(i)):
            print("port {} is open".format(i))
        else:
            print("port {} is closed".format(i))
except:
    pass

#for file containing list of port numbers
try:
    f=open(a.l,"r")
    g=f.readlines()
    for i in g:
        if run (int(i.strip())):
            print("port {} is open".format(i.strip()))
        else:
            print("port {} is closed".format(i.strip()))
            
except:
    pass
