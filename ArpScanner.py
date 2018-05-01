#!/usr/bin/python
from scapy.all import *

addr_const = "192.168.1."

for addr in range(1,255):
    ans = sr1(ARP(pdst=addr_const+str(addr)) , timeout=2 , verbose=0)
    if ans:
        print("[+] Host Found  "+addr_const+str(addr) +"    mac address : " +ans[0][ARP].hwsrc)
