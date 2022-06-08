# Readme file for task 2

**Author: Yiqing Gu**

+ There are 3 functions in this file.
  - step1(address ,time)
  - step2()
  - main()

### step1(address ,time)

This is a fuction for creating packets user needs and printing detailed packet information

The way of structuring packets is from scapy. Base structure: IP()/ICMP()/......

.show() in scapy is used here for printing packet information.

There are two parameters needed here:

**address:** The address user wants to be packed into packets.

**time:** The value of TTL. It is "Time To Live" of packets.

Some print functions are used here for typeset. Making it as same as samples in assignment file.

### step2()

This a function for implementing task2 step2 in the assignment.

It will call step1(address ,time) 

There are three addressed used here:

"128.255.96.68"

"8.8.8.8"

"129.94.124.115"

The value of TTL is 100, as required.

No parameters are needed here.

### main()

This is the main function.

It will call functions which can get something printed as what assignment requires.

The sequence of calls follows the sequences of steps in assignment.

No parameters are needed here.
