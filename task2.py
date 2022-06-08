import sys
from scapy.all import *

def step1(address, time):
	packet = IP(dst = address, ttl = time)/ICMP()/"xxxx"
	if (address == "128.255.96.68"):
		print "Uiowa"
	elif (address == "8.8.8.8"):
		print "Google"
	else:
		print "UNSW - Sydney"
	packet.show()

def step2():
	step1("128.255.96.68",100)
	step1("8.8.8.8",100)
	step1("129.94.124.115",100)
	

def main():
	step2()

if __name__ == "__main__":
	main()
