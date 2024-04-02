import ctypes
import os
from tkinter import *
from tkinter import ttk

window = Tk()
window.title("my window")
window.geometry("1000x700")


# Changing the Task bar icon and window icon
app_id="comp-500-character-viewer"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)



abs_path = os.path.abspath(__file__)
dir_name = os.path.dirname(abs_path)

icon_path = os.path.join(dir_name,"image.ico")
window.iconbitmap(icon_path)

img_path = os.path.join(dir_name,'spongebob.png')
img = PhotoImage(file=img_path)


# Event handler method for the combobox
def option_selected(event):
    character_list = ("spongebob.png","squidward.png")
    character_index = com_box.current()
    img['file'] = character_list[character_index]



window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

frame1 = Frame(window)
frame1.grid(row=0, column=0)

# label1 = Label(frame1, text="my label-1", bg="blue", fg="white")
# label1.grid(row=0, column=0)

# Combobox 
character_list = ("spongebob","squidward")

com_box = ttk.Combobox(frame1, values=character_list)
# com_box.set("spongebob")
com_box.bind("<<ComboboxSelected>>", option_selected)
com_box.grid(row=0, column=0)


frame2 = Frame(window)
frame2.grid(row=0, column=1)

# Label for displaying the image
label2 = Label(frame2, text="my label-2", bg="blue", fg="white",image=img)
label2.grid(row=0, column=0)



# main code

window.mainloop()