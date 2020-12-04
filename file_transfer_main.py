#!/usr/bin/python
# -*- coding: utf-8 -*-
#   Python ver:     3.9.0
#
#   Author:         Christopher A. Moody
#
#   Purpose:        A comapany branch needs to transfer new and/or modified
#                   files to the home office each day and they need a script that can decide
#                   which files are valid candidates for transfering. Create a program that
#                   can decide whether not a file is new or modified and add it to a directory
#                   that will be sent to the home office.
#
#   Tested OS:      Written and tested with Windows 10.

from tkinter import *
import os
import tkinter as tk

import file_transfer_func
import file_transfer_gui

class Window(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,170) #width,height
        self.master.maxsize(500,170)

        file_transfer_func.center_window(self, 500, 170)
        self.master.title("File Transfer Plus")
        self.master.configure(bg='blue')

        self.master.protocol("WM_DELETE_WINDOW", lambda: file_transfer_func.ask_quit(self))
        arg = self.master
        file_transfer_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()





