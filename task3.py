import sys
from scapy.all import *

def craft_task2_packets(address,time):
	return IP(dst = address, ttl = time)/ICMP()/"xxxx"

def step1(packet):
	infoList = sr(packet, timeout = 10)
	check = infoList[0]
	try:
		output = check[0]
		print(output)
		print("\n")
	except:
		print "Error! No responses!\n"

def step2():
	packet1 = craft_task2_packets("128.255.96.68",100)
	packet2 = craft_task2_packets("8.8.8.8",100)
	packet3 = craft_task2_packets("129.94.124.115",100)
	step1(packet1)
	step1(packet2)
	step1(packet3)

def generate_icmp_packet(add, number):
	numLoop = number
	while(numLoop > 0):
		pack = craft_task2_packets(add, numLoop)
		send_and_receive_packets(pack, numLoop)
		numLoop = numLoop - 1
		

def send_and_receive_packets(pack, status):
	info_Collection = sr(pack, timeout = 10)
	report = info_Collection[0]
	try:
		confirm = report[0]
		print("TTL value: " + str(confirm[0].ttl) + 
		" | Source IP in response: " + str(confirm[1].src))
		print("\n")
	except:
		print "No responses at TTL value: " + str(status)+ " !\n"

def step3():
	loopSet = 10
	generate_icmp_packet("8.8.8.8",loopSet)


def main():
	step2()
	step3()

if __name__ == "__main__":
	main()
