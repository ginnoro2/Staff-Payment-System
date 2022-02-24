import unittest

def Exit():
    wayOut = tkinter.messagebox.askyesno("Staff Payment Record System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
