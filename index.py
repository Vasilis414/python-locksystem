from tkinter import *
from tkinter import ttk
import pyautogui
import time
import keyboard 
from PIL import ImageTk, Image
from config import password
keyboard.block_key('Win')
keyboard.block_key('Alt')
root = Tk();
root.geometry("1920x1080");
root.configure(bg='#a62626')
import os
os.system("displayswitch.exe /clone")
pyautogui.moveTo(1744,338)
pyautogui.click();
pressed_f4 = False  
frame = Frame(root, width=300, height=200)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("lock.png").resize((667, 834), Image.ANTIALIAS))

label = Label(frame, image = img, bg="#a62626")
label.pack()
label = Label(root, image = "", bg="#a62626")
label.pack()

style = ttk.Style()

style.configure("ModernEntry.TEntry",
                foreground="#333333",  # Text color
                background="#a62626",  # Background color
                fieldbackground="#a62626",  # Field background color
                bordercolor="#a62626",  # Border color
                borderwidth=2,  # Border width
                relief="solid",  # Border style
                padding=5,  # Internal padding
                font=("Helvetica", 12),  # Font settings
                height=10  # Set the height of the Entry widget
                )

# Create an Entry widget with the modern style
entry = ttk.Entry(root, style="ModernEntry.TEntry", show="*"    )
entry.pack(padx=10, pady=1)

def do_exit():
    global pressed_f4
    print('Trying to close application')
    if pressed_f4:  
        print('Denied!')
        pressed_f4 = False 
    else:
        close()    

def alt_f4(event):  
    global pressed_f4
    print('Alt-F4 pressed')
    pressed_f4 = True

def close(*event): 
    root.destroy()

root.bind('<Alt-F4>', alt_f4)
root.protocol("WM_DELETE_WINDOW",do_exit)
root.attributes('-topmost',True)
root.attributes('-fullscreen', True)

def unlock(event):
    global entry
    if str(entry.get()) == password:
        os.system("displayswitch.exe /extend")
        root.destroy();



def close_win():
   root.destroy()
def disable_event():
   pass

root.protocol("WM_DELETE_WINDOW", disable_event)
root.bind('<Return>', unlock)


root.mainloop();
