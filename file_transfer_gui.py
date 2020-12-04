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
import tkinter as tk

import file_transfer_func
import file_transfer_main


def load_gui(self):
    # gui buttons
    self.btn_browse = tk.Button(self.master, width=14, height=1, text='Source Folder', command=lambda: file_transfer_func.askdir(self))
    self.btn_browse.grid(row=3, column=1, padx=(10,10), pady=(45,0), sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=14, height=1, text='Destination Folder', command=lambda: file_transfer_func.askdir2(self))
    self.btn_browse2.grid(row=4, column=1, padx=(10,10), pady=(8,0), sticky=W)
    self.btn_transfer = tk.Button(self.master, width=12, height=2, text='Transfer Files', command=lambda: file_transfer_func.transfer(self))
    self.btn_transfer.grid(row=5, column=2, padx=(15,10), pady=(8,0), sticky=W)
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close Program', command=lambda: file_transfer_func.ask_quit(self))
    self.btn_close.grid(row=5, column=4, padx=(3,0), pady=(8,0), sticky=E)
    self.btn_clear = tk.Button(self.master, width=12, height=2, text='Clear Fields', command=lambda: file_transfer_func.onClear(self))
    self.btn_clear.grid(row=5, column=3, padx=(5,0), pady=(8,0), sticky=W)


    # gui text fields
    self.txt_browse = tk.Entry(self.master, width=55, text='')
    self.txt_browse.grid(row=3, column=2, rowspan=1, columnspan=6, padx=(14,40), pady=(45,0), sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master, text='')
    self.txt_browse2.grid(row=4, column=2, rowspan=1, columnspan=6, padx=(14,40), pady=(8,0), sticky=N+E+W)


if __name__ == "__main__":
    pass
