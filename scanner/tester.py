import threadedScanner

if __name__=="__main__":
    Scanner = threadedScanner.PortScanner()
    Scanner.scan()
    print(Scanner.openPorts)
