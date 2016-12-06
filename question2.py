from netaddr import *
import sys
import re
def validIPforScanning(range,input_list):
  valid = re.match( r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)[/]([1-9]$|[1-2][0-9]$|3[0-2])$',range)

  if(not valid):
    print("Invalid address range input")
    sys.exit()
  r= IPSet([IPNetwork(range)])  
  for i in input_list:
    if(not valid_ipv4(i)):
      print("Invalid IP addresses in the input set")
      return 
    if(i not in r):
      print("Input set contains values not in the given address range")
      return


  rangeiplist=[]
  outputlist=[]
  for ip in r:
    rangeiplist.append(ip)
  for i in input_list:
    if IPAddress(i) in rangeiplist:
      print("Removing the ip address")
      r.remove(i)

  for ip in r:
    outputlist.append(ip)

  return(outputlist)
