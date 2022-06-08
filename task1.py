import sys
from scapy.all import *

def step1():
	interface_list = get_if_list()
	route_info = conf.route
	print ("Interface list:")
	print interface_list
	print ("Router interface list:")
	print route_info

def step2(ip, i_f, steps):
	counter = 1
	packets = sniff(filter = ip, iface = i_f, count = steps)
	for packet in packets:
		print("Packet #" + str(counter))
		print("Link layer: " + str(packet.src) + " (src link address) -> " 
		+ str(packet.dst) + " (dst link address) ")
		print("Network layer: " + str(packet[1].src) + " (src IPv" + str(packet.version) 
		+ " address) -> " + str(packet[1].dst) + " (dst IPv" + str(packet.version) 
		+ " address) ")
		print("Transport layer: " + str(packet.sport) + " -> " + 
		str(packet.dport) + " (dst port)")
		counter = counter + 1
		

def step3():
	ip_1 = "host 128.255.96.68 or host 2620:0:e50:6810::80ff:6044"
	max_count = 10**3
	interface = conf.iface
	step2(ip_1, interface, max_count)
	

def main():
	step1()
	step3()

if __name__ == "__main__":
	main()
