import sys
from socket import socket, gethostname, gethostbyname
import threading

class PortScanner():
    """
    PortScanner class
    init with host, startPort, endPort, threads
    host -> host address to scan
    startPort -> port to start scanning at
    endPort -> port to stop scanning at
    threads -> number of threads for port scanning
    """
    def __init__(self, **args):
        if "host" in args:
            self.host = host
        else:
            self.host = gethostbyname(gethostname())

        if "startPort" in args:
            self.startPort = args["startPort"]
        else:
            self.startPort = 1

        if "endPort" in args:
            self.endPort = args["endPort"]
        else:
            self.endPort = 65535

        if "threads" in args:
            self.threads = args["threads"]
        else:
            self.threads = 32

        self.openPorts = dict()
        self._portStatus = {"open": 1, "closed" : 0, "error": -1, "unknown": None}
        for i in range(1, 65535):
            self.openPorts[i] = self._portStatus["unknown"]

    def portIsOpen(self, host, port):
        """
        return True if {port} on {host} is open, otherwise return False
        """
        Socket = socket()
        try:
            Socket.connect((host, port))
        except ConnectionRefusedError:
            return "closed"
        except:
            return "error"
        return "open"

    # helper function for multithreading
    def portScan(self, host, ports):
        while ports:
            port = ports.pop(0)
            status = self.portIsOpen(host, port)
            self.openPorts[port] = self._portStatus[status]

    # scans ports in range, uses multithreading
    def portScanner(self, host, startPort, endPort, threads):
        ports = list(range(startPort, endPort+1))
        threads = [threading.Thread(target=self.portScan, args = (host, ports)) for _ in range(threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    # def scan(self, host=self.host, startPort=self.startPort, endPort=self.endPort, threads=self.threads):
    def scan(self, host=None, startPort=None, endPort=None, threads=None):
        """
        scan ports in range {startPort}, {endPort} on host
        default {host} is local machine
        default {startPort} is 1
        default {endPort} is 65535
        """
        if host is None:
            host = self.host
        if startPort is None:
            startPort = self.startPort
        if endPort is None:
            endPort = self.endPort
        if threads is None:
            threads = self.threads
        self.portScanner(host, startPort, endPort, threads)
        return self.openPorts
