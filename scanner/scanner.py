import sys
from socket import socket, gethostname, gethostbyname
import threading
from datetime import datetime
import os

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
            self.host = args["host"]
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
        for i in range(1, 65535+1):
            self.openPorts[i] = "unknown"
        self.changes = []
        self.logfile = ".logfile.log"
        if not os.path.isfile(self.logfile):
            open(self.logfile, "a").close()

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
            oldStatus = self.openPorts[port]
            if status != oldStatus and (oldStatus != "unknown" or status != "closed"):
                self.changes.append(f"{datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3].ljust(23, '0')} Port {port:5} changed from {oldStatus} to {status}")
            self.openPorts[port] = status

    # scans ports in range, uses multithreading
    def portScanner(self, host, startPort, endPort, threads, selected=None):
        if selected is not None:
            ports = selected
        else:
            ports = list(range(startPort, endPort+1))
        threads = [threading.Thread(target=self.portScan, args = (host, ports)) for _ in range(threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    # def scan(self, host=self.host, startPort=self.startPort, endPort=self.endPort, threads=self.threads):
    def scan(self, host=None, startPort=None, endPort=None, threads=None, selected=None):
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
        if selected is not None:
            self.changes.append(f"{datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3].ljust(23, '0')} Started port scanning on {selected}")
        else:
            self.changes.append(f"{datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3].ljust(23, '0')} Started port scanning on range {startPort} - {endPort}")

        self.portScanner(host, startPort, endPort, threads, selected=selected)
        self.changes.append(f"{datetime.utcnow().strftime('%Y/%m/%d %H:%M:%S.%f')[:-3].ljust(23, '0')} Ended port scanning")
        # update log
        # get previous log
        oldlines = []
        with open(self.logfile, "r") as log:
            oldlines = []
            for line in log:
                oldlines.append(line)
        # clear the log, write the changes first, previous log after that
        with open(self.logfile, "w") as log:
            for line in self.changes[::-1]:
                log.write(line)
                log.write("\n")
            for line in oldlines:
                log.write(line)

        return self.openPorts
