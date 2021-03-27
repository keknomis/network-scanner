"""
Single-threaded scanner
portScanner returns list of all open ports
"""
import sys
from socket import socket, gethostname, gethostbyname

def portIsOpen(host, port):
    """
    return True if {port} on {host} is open, otherwise return False
    """
    Socket = socket()
    try:
        Socket.connect((host, port))
    except ConnectionRefusedError:
        return False
    except:
        print("ERROR")
        return False
    return True

def portScanner(host=gethostbyname(gethostname()), startPort=1, endPort=65535):
    """
    scan ports in range {startPort}, {endPort} on host
    default {host} is local machine
    default {startPort} is 1
    default {endPort} is 65535
    """
    openPorts = []
    for port in range(startPort, endPort+1):
        if portIsOpen(host, port):
            openPorts.append(port)

    return openPorts
