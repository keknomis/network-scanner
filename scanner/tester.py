import scanner

if __name__=="__main__":
    Scanner = scanner.PortScanner()
    Scanner.scan(startPort=10, endPort=500)
    a = Scanner.openPorts
    for i in range(10, 100):
        #print(i, a[i])
        if(a[i] == 'open'):
            print(i)
        #print(port, Scanner.openPorts[port])
        #pass

