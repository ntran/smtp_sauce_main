'''
Connect to ipv4 / ipv6 
'''

# Python libraries
from socket import *

windowsize = 1024

## Connect to the ipv4 / ipv6 port
## Params:	ipv4 - (boolean) ipv4 address
##		ipv6 - (boolean) ipv6 address
## Indicate the connection info
def connect_ip(ipv4, ipv6, host, port):

	if (ipv4) and (ipv6):
		raise Exception("Dupliate Value: '-4' cannot be used with '-6'")

	elif (ipv4):
		addr = getaddrinfo(host, port, AF_INET, SOCK_STREAM)
		(family, socktype, proto, canonname, sockaddr) = addr[0]
		ip, port = sockaddr
		
		return ip, port
	
	elif (ipv6):
		conn = has_ipv6
		if not conn:
			raise Exception("ERROR: IPv6 not supported")
		addr = getaddrinfo(host, port, AF_INET6, SOCK_STREAM)
		(family, socktype, proto, canonname, sockaddr) = addr[0]
		ip, port, flow_info, scope_id = sockaddr 
		return ip, port
	
	else:
		return host, port
	 