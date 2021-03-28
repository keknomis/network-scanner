knownPorts = {
21 : "FTP",
22 : "SSH, check that root access is disabled",
23 : "telnet",
25 : "SMTP",
53 : "DNS",
443 : "http, https",
110 : "POP3",
135 : "Windows RPC",
136 : "Windows NetBIOS",
137 : "Windows NetBIOS",
138 : "Windows NetBios",
1433 : "Windows SQL Server",
1434 : "Windows SQL Server",
}

def portAnalyzer(port):
    return knownPorts.get(port, "")

