from tkinter import *
from PIL import Image, ImageTk
data=Tk()
data.title("MAP - CAB BOOKING SYSTEM")
data.geometry('800x650')
data.resizable(False,False)

image=Image.open("road.jpg")
image=image.resize((800,650))
img=ImageTk.PhotoImage(image)
panel=Label(data,image=img)
panel.pack(side='bottom', fill='both', expand='yes')

menubar=Menu(data)

def hz():
   data.destroy()
   import navigation
homemenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Home", command=hz)

def lz():
   data.destroy()
   import login
logmenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Login", command=lz)

def rz():
   data.destroy()
   import registration
signmenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Sign Up", command=rz)

def bz():
   data.destroy()
   import booking
bookmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Book Cab", command=bz)

def pz():
   data.destroy()
   import profile
def ez():
   data.destroy()
   import editprofile
def jz():
   data.destroy()
   import rides
accountmenu=Menu(menubar,tearoff=0)
accountmenu.add_command(label="Profile",command=pz)
accountmenu.add_command(label="Edit Profile",command=ez)
accountmenu.add_command(label="Rides",command=jz)

menubar.add_cascade(label="Account", menu=accountmenu)

def cz():
   data.destroy()
   import cabs
cabmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Cabs", command=cz)

def tz():
   data.destroy()
   import maps
routemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Map", command=tz)

data.config(menu = menubar)
data.mainloop()
