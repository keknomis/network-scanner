import scanner

if __name__=="__main__":
    Scanner = scanner.PortScanner()
    Scanner.scan()
    for port in Scanner.openPorts:
        # print(port, Scanner.openPorts[port])
        pass
