from netaddr import *
import sys
import re
def validIPforScanning(range,exclude_list):
#range = '192.128.1.0/24'
#set = ['192.128.1.17','192.128.1.4','172.32.113.1']
# regex to check if the network range is valid or not
valid = re.match( r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[/]([1-9]$|[1-2][0-9]$|3[0-2])$',range)
if(not valid):
  print("Invalid address range input")
  return()
# list of IP addresses in the network range
r= IPSet([IPNetwork(range)])  
# error check for valid ip address in the given set and also if the ip addresses in the set are in the given range or not
for i in set:
  if(not valid_ipv4(i)):
    print("Invalid IP addresses in the input set")
    return() 
  if(i not in r):
    print("Input set contains values not in the given address range")
    sys.exit()
    
rangeiplist=[]
outputlist=[]
for ip in r:
  rangeiplist.append(ip)
#removing a IP address not required to use in the scanning tool
for i in set:
  if IPAddress(i) in rangeiplist:
    print("Removing the ip address")
    r.remove(i)

for ip in r:
  outputlist.append(ip)
  
return(outputlist)
