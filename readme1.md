# Readme file for task 1

**Author: Yiqing Gu**

+ There are 4 functions in this file.
  - step1()
  - step2(ip, i_f, steps)
  - step3()
  - main()

### step1()
This a function for implementing task1 step1 in the assignment.

It will generate a interface list and print all interfaces on this devices.

It will call get_if_list() and conf.route in scapy.

get_if_list() will print the all interface names on this devices.

conf.route will print the all interface names and detailed information on this devices.

No parameters are needed here.

### step2(ip, i_f, steps)

This is a function for sniffing packets on specific addresses and printing packet information.

It will call sniff() in scapy.

There are three parameters needed here:

**ip:** An IP address or multiple IP addresses which user wants to use on sniffing packets.

**i_f:** The interface which user wants to use for sniffing.

**steps:** How many packets which user wants to sniff. The maximum value.

### step3()

This a function for implementing task1 step3 in the assignment.

Two IP addresses 128.255.96.68 and 2620:0:e50:6810::80ff:6044 are used here.

The number of packets needed here is 10**3.

The interface is the one which user is using while browsing specific IP addresses.

step3() will call step2(ip, i_f, steps) in order to implement task1 step3.

No parameters are needed here.

### main()

This is the main function.

It will call functions which can get something printed as what assignment requires.

The sequence of calls follows the sequences of steps in assignment.

No parameters are needed here.


