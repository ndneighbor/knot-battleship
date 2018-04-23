from tkinter import *
from PIL import Image, ImageTk
import BaseDialog as dialog
import BaseEntry as entry
import threading
import socket
import sys
import logging


class Window(Frame):

    def __init__(self, master=None):
        
        Frame.__init__(self, master)   
        self.master = master
        self.init_window()


    def init_window(self):     
        self.master.title("Knot-Battleship")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Lobby Play", command=self.connectLobby)
        edit.add_command(label="Quick Play", command=self.qCLobby)
        edit.add_command(label="Settings", command=self.settings)
        edit.add_command(label="Help", command=self.showHelp)
        menu.add_cascade(label="Menu", menu=edit)

        # Header IMG

        load = Image.open("assets/kb-title.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        # Buttons

        lB = Button(self, text="Join a match", 
                                command=self.connectLobby)
        setB = Button(self, text="Settings", 
                        command=self.settings)
        tB = Button(self, text="Tutorial", 
                        command=self.showHelp)
        lB.place(relx=.5, rely=.6, anchor="c")
        setB.place(relx=.5, rely=.7, anchor="c")
        tB.place(relx=.5, rely=.8, anchor="c")

    def connectLobby(self):
        t = Toplevel(self)
        Label(t, text="Enter host:").grid(row=0, sticky="w")
        Label(t, text="Enter port:").grid(row=1, sticky="w")
        Label(t, text="Enter name:").grid(row=2, sticky="w")

        self.hostEntryField = Entry(t)
        self.portEntryField = Entry(t)
        self.nameEntryField = Entry(t)

        self.hostEntryField.grid(row=0, column=1)
        self.portEntryField.grid(row=1, column=1)
        self.nameEntryField.grid(row=2, column=1)

        return self.hostEntryField

    def showHelp(self):
        t = Toplevel(self)
        t.wm_title("Settings")
        l = Label(t, text="This is the help.")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def qCLobby(self):
        load = Image.open("assets/kb-title.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def settings(self):
        t = Toplevel(self)
        t.wm_title("Settings")
        l = Label(t, text="Settings")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        

    def client_exit(self):
        exit()

root = Tk()

root.geometry("1029x768")

app = Window(root)

root.mainloop()  

