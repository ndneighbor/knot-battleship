import tkinter as tk

class BaseDialog(tk.Toplevel):

    def __init__(self, parent, title = None):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent) # associate this dialog with parent window

        if title:
            self.title(title)

        self.parent = parent
        self.result = None

        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        """
        createa an ok and cancel button and also binds the return and escape key.
        """
        self.buttonbox()

        self.grab_set() # makes the dialog modal.

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        # position the dialog relative to the parent window
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        # move the keyboard focus to the appropriate widget.
        self.initial_focus.focus_set()

        self.wait_window(self)
        

    def body(self, master):
        # create dialog body. return widget that should have initial focus.
        # This method is meant to be overriden.
        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the standard buttons.

        box = tk.Frame(self)

        button = tk.Button(box, text="OK", width=10, bg="#CACACA", activebackground="#CACACA", command=self.ok, default=tk.ACTIVE)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button = tk.Button(box, text="Cancel", width=10, bg="#CACACA", activebackground="#CACACA", command=self.cancel)
        button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def ok(self, event=None):
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()
        
        self.cancel()

    def cancel(self, event=None):
        self.parent.focus_set() # puts focus back to the parent window.
        self.destroy()

    def validate(self):
        return True # override if necessary

    def apply(self):
        pass # override if necessary
