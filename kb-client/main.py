from tkinter import *
from PIL import Image, ImageTk


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
        edit.add_command(label="Settings", command=self.settings)
        edit.add_command(label="Help", command=self.showHelp)
        menu.add_cascade(label="Menu", menu=edit)

        # We are setting up the buttons and the visuals

        load = Image.open("assets/kb-title.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def connectLobby(self):
        load = Image.open("assets/kb-title.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showHelp(self):
        load = Image.open("assets/kb-title.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def settings(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()
        

    def client_exit(self):
        exit()

root = Tk()

root.geometry("1204x1024")

app = Window(root)

root.mainloop()  