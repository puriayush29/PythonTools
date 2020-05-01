#!/usr/bin/env python

from socket import *
import sys,time
from datetime import datetime
from colorama import init,Fore
host = ''
max_port = 100
min_port = 1

init()

GREEN = Fore.GREEN
RESET = Fore.RESET
def scan_host(host,port,r_code =1):
	try:
		sock = socket(AF_INET,SOCK_STREAM)

		code = sock.connect_ex((host,port))

		if code == 0:
			r_code = code
		sock.close()
	except KeyboardInterrupt:
	    print("\n\n[*] User Requested an Interrupt.")
	    print("[*] Application Shutting Down.")
	    sys.exit()
	except Exception as e:
		pass
	except socket.gaierror:
		print("Hostname could not be resolved.Exiting...")
		sys.exit()
	except socket.error:
		print("couldn't connect to the server..")
		sys.exit()
	return r_code

try:
	host = input("\n[*] Enter Target Host Address: ")
except KeyboardInterrupt:
	print("\n\n[*] User Requested an Interrupt.")
	print("[*] Application Shutting Down.")
	sys.exit()

hostip = gethostbyname(host);

print("\n[*] HOST:{0} IP:{1}".format(host,hostip))
print("\n[*] Scanning Started at:{0}".format(time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port,max_port):
	try:
		response = scan_host(host,port)
		
		if response == 0:
			print("PORT {0}:OPEN".format(port))
		else:
			print("PORT {0}:CLOSED".format(port))
	except Exception as e:
		pass
stop_time = datetime.now()
total_time = start_time - stop_time
print("\n[*] Scanning Finished at:{0}".format(stop_time))
print("\n[*] Scanning Duration is:{0}".format(total_time))
print("\n[*] HACKTHEWORLD......")
