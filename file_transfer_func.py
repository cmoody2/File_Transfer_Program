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

import time
import shutil
import os
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import file_transfer_main
import file_transfer_gui


#---------------------------------
#   Window GUI Functions
#---------------------------------

def center_window(self, w, h):  # Pass in the tkinter frame (master) reference and the w and h
    # Get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # Calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

def onClear(self):
    self.txt_browse.delete(0,END)
    self.txt_browse2.delete(0,END)
    
#---------------------------------
#   Directory Button Function
#---------------------------------

# these are tied to the source and destination folder buttons respectively
# and returns the paths selected by the user.
def askdir(self):
    self.txt_browse.delete(0,END)
    folder = filedialog.askdirectory(initial="/")
    self.txt_browse.insert(0,folder)

def askdir2(self):
    self.txt_browse2.delete(0,END)
    folder2 = filedialog.askdirectory(initial="/")
    self.txt_browse2.insert(0,folder2)
    

#-----------------------------
#   FILE CHECK/COPY CLASS
#-----------------------------

class FileCheck:
    def __init__(self, file_path):
        self.file_path = file_path # gets filename
        
        
    def look(self):
        stamp = os.path.getmtime(self.file_path)
        # this assigns stamp a value of the given files modifiy time
        cur_time = time.time()
        # gets the current time in seconds since epoch
        if stamp > (cur_time - float(86400)):
            # cur_time - float(86400) is the current time minus 24hrs
            return True
        else:
            return False

fc = FileCheck('')

#------------------------------
#   Transfer Function
#------------------------------

# iterate through each file in src directory
# if FileCheck supplied with specified file returns True
# then copy to dst directory
def transfer(self):
    src_path = os.path.normpath(self.txt_browse.get()) # gets path from text entry and normalizes it
    src = src_path + '/'                               # adds a / to end of normalized path
    src_files = os.listdir(src)
    # return list of files in 'src'
    
    dst_path = os.path.normpath(self.txt_browse2.get())
    dst = dst_path + '/'
    if os.path.isabs(src_path) and os.path.isabs(dst_path):
    # determines whether the text in both text fields are absolute paths
        for i in src_files:
            fc.file_path = src + i
            if fc.look():
                shutil.copy2(src + i,dst)
                #copy file to destination folder
            else:
                continue
    else:
        messagebox.showinfo(title="Folder Selection Error", message="Please select a source and destination folder")


if __name__ == "__main__":
    pass

