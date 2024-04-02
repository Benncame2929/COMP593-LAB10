"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk
import os
from ctypes import *
from tkinter import tk, ttk PhotoImage

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# TODO: Create the images directory if it does not exist.
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
#root.minsize(500, 500)

# TODO: Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("COMP593.PokeImageViewer")
root.iconbitmap(os.path.join(script_dir, "image.ico"))

# TODO: Create frames
frm = ttk.Frame(root)
frm.grid(sticky="new")

# TODO: Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, "spongbob.png")
photo = PhotoImage(file = image_path)

image_lbl = ttk.Label(frm, image=photo)
image_lbl.grid(row=0 ,column=0 ,padx=10 ,pady= 10)

root.mainloop()