from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import scanner
import portAnalyzer

A = scanner.PortScanner()
window = Tk()
window.title("ScannerGUI")
window.geometry('1320x900')
window.option_add("*Font", '16')
window.configure(background='#0e1111')
window.resizable(0, 0)
lbl = Label(window, text="Ports", bg='#0e1111', fg='blue')
lbl.grid(column=0, row=0)
txt = Entry(window, width=100, bg='#0e1111', fg='yellow', insertbackground='white')
txt.grid(column=1, row=0)
curr = scrolledtext.ScrolledText(window, bg='#0e1111', fg='green', height=0)
statusWindow = Text(window, bg='#0e1111', fg='green', height=0)
statusWindow2 = Text(window, bg='#0e1111', fg='green', height=0)
curr.config(height=40, width=100)
curr.grid(column=1, row=2)



lbl3 = Label(window, text="Usage: \n "
                          "- To scan ALL ports simply \n"
                          " press Start scanning button \n"
                          "\n"
                          "- To scan SINGLE port \n"
                          "type in the port number \n "
                          "\n"
                          "- To scan RANGE of ports \n"
                          "Type the start port number \n"
                          "insert - (minus) as a delimiter \n"
                          "and type the end port number", bg='#0e1111', fg='blue')

lbl3.grid(column=2, row=2)


def clicked():
    global counter, curr
    ports =  txt.get().strip()
    port = None
    selected = None
    startPort = None
    if len(ports) == 0:
        A.scan()
    elif "," in ports:
        selected = ports.split(",")
        selected = [int(sel.strip()) for sel in selected]
        A.scan(selected=selected)
    elif "-" in ports:
        startPort, endPort = int(ports.split("-")[0]), int(ports.split("-")[1])
        A.scan(startPort=startPort, endPort=endPort)
    else:
        port = int(ports.strip())
        A.scan(selected=[port])

    openPorts = A.openPorts

    statusWindow.config(height = 1, width = 62)
    statusWindow.grid(column = 1, row = 1)
    statusWindow2.config(height = 1, width = 62)
    statusWindow2.grid(column = 1, row = 2)

    if selected or startPort or port:
        if startPort:
            selected = list(range(startPort, endPort+1))
        if port:
            selected = [port]
        for port in selected:
            status = openPorts[port]
            curr.config(state=NORMAL)
            if status == "open":
                service = portAnalyzer.portAnalyzer(port)
                if service:
                    curr.insert(END, f"port {port} is open -> running {service}\n")
                else:
                    curr.insert(END, f"port {port} is open -> unknown service\n")
            else:
                curr.insert(END, f"port {port} is {status}\n")
            curr.config(state = DISABLED)
    else:
        for port, status in openPorts.items():
            links = {"", ""}
            statusWindow.config(state = NORMAL)
            statusWindow.insert(END, f" scanning")
            statusWindow.config(state = DISABLED)
            window.update()
            statusWindow.config(state = NORMAL)
            statusWindow.delete('1.0', END)
            statusWindow.config(state = DISABLED)
            counter = 0
            if status == "open":
                curr.config(state = NORMAL)
                service = portAnalyzer.portAnalyzer(port)
                if service:
                    curr.insert(END, f"port {port} is open -> running {service}\n")
                else:
                    curr.insert(END, f"port {port} is open -> unknown service\n")
                curr.config(state = DISABLED)

    statusWindow.config(state = NORMAL)
    statusWindow.delete('1.0', END)
    statusWindow.insert(END, 'DONE')
    statusWindow.config(state = DISABLED)
    messagebox.showwarning('DONE', 'DONE')

btn = Button(window, text="Start scanning", command=clicked, bg = 'black', fg = 'blue', activebackground = 'red')
btn.grid(column=2, row=0)
window.mainloop()
