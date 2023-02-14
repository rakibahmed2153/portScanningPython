#!/bin/python

import sys
import socket
from datetime import datetime

#Define a target
if len(sys.argv) == 2:
    #Translate host name to IPV4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Amount Of Arguments")
    print("Syntex: python3 scanner.py <IP>")
    
#Add a Banner    
print("-" * 50)
print("Scanning target - " + target)
print("Time started - " + str(datetime.now()))
print("-" * 50)

try:
    print("-" * 50)
    for port in range(50, 85):
        print("-" * 50)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port)) # return error 
        print(result)
        if result == 0:
            print("Port {} is Open".format(port))
        else:
            print("Port {} is Closed".format(port))
        s.close()    
        
except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()
except socket.gaierror:
    print("Host name could not be resolved")
    sys.exit()
except socket.error:
    print("Couldn't connect to the server")
    sys.exit()    
    
