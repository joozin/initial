#!/usr/bin/env python

import socket
import sys
import ipaddress

# Variables declaration
host_ip = sys.argv[1]
str(host_ip)
exist = 0
new_port = 0
# Create unicode string - important for ipaddress resolution
uhost_ip = unicode(host_ip, "utf-8")
# Create a file is doesn't exist yet
file = open('notes_IP.txt', 'a')
file.close()

# Get an IP host or network
IPs = ipaddress.ip_network(uhost_ip, strict=False)
# Check how many host are in network
hosts_count = IPs.num_addresses


if (IPs.version != 4): 
    print("Not an IPv4 address!")

print("Scan of: "+ host_ip)

with open('notes_IP.txt', 'r+') as file:
#    old_data = file.read()
#    for line in file:
#        print(line)
# scan each point_ip of snaced network
    for upoint_ip in IPs.hosts():
        # Convert unicode IP@ to python string
        point_ip = str(upoint_ip)
        print ("*Target - " + point_ip + ": Full scan results:*")
        new_port = 0
        for port in range(1,100):
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((point_ip, port))
            sock.close()
            if (result == 0):
                string1 = point_ip + " " + str(port)+"\n"
                string2 = point_ip + " " + str(port)
                for line in file:
#                    print("som tu",port)
                    if((line == string1) or (line == string2)):
                        exist = 1
                if (exist != 1):
                    print("Host: " + point_ip + "\t\tPort:\t"+ str(port)+"\tOpen")
                    file.write(point_ip + " " + str(port)+"\n")
                    exist = 0
                    new_port = 1
        if (new_port == 0):
            print("*Target - " + point_ip + ": No new records found in the last scan.*")


