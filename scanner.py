from socket import socket, gethostname, gethostbyname

def portIsOpen(host, port):
    Socket = socket()
    try:
        Socket.connect((host, port))
    except ConnectionRefusedError:
        return False
    except:
        print("ERROR")
        return False
    return True

if __name__ == "__main__":
    host = gethostbyname(gethostname())
    for port in range(1, 65536):
        if portIsOpen(host, port):
            print(f"Port {port} is open.")
