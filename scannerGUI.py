from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import scanner
import portAnalyzer

A = scanner.PortScanner()
window = Tk()
window.title("ScannerGUI")
window.geometry('1200x800')
window.configure(background='black')
window.resizable(0,0)
lbl = Label(window, text="Ports", bg = 'black', fg = 'blue')
lbl.grid(column=0, row=0)
txt = Entry(window,width=100, bg = 'black', fg = 'yellow', insertbackground = 'white')
txt.grid(column = 1, row=0)
curr = scrolledtext.ScrolledText(window, bg = 'black', fg = 'green', height = 0)
statusWindow = Text(window, bg = 'black', fg = 'green', height = 0)
statusWindow2 = Text(window, bg = 'black', fg = 'green', height = 0)


def clicked():
    global counter, curr
    ports =  txt.get().strip()
    if len(ports) == 0:
        A.scan()
    elif "," in ports:
        selected = ports.split(",")
        A.scan(selected=selected)
    else:
        startPort, endPort = int(ports.split("-")[0]), int(ports.split("-")[1])
        A.scan(startPort=startPort, endPort=endPort)

    openPorts = A.openPorts

    curr.config(height = 30, width = 60)
    curr.grid(column=1, row=3)
    statusWindow.config(height = 1, width = 62)
    statusWindow.grid(column = 1, row = 1)
    statusWindow2.config(height = 1, width = 62)
    statusWindow2.grid(column = 1, row = 2)

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
            if service:=portAnalyzer.portAnalyzer(port):
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
