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
    for port in range(startPort, endPort+1):
        if portIsOpen(host, port):
            print(f"Port {port} is open.")

if __name__ == "__main__":
    host = gethostbyname(gethostname())
    args = sys.argv[1:]
    inputArgs = {"host":host}
    if len(args) == 2:
        inputArgs["startPort"] = int(args[0])
        inputArgs["endPort"] = int(args[1])
    if len(args) == 3:
        inputArgs["host"] = args[2]

    portScanner(**inputArgs)

