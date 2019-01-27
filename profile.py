import sqlite3
from tkinter import *
from tkinter import messagebox
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
data=Tk()
data.title('PROFILE - CAB BOOKING SYSTEM')
data.geometry('600x400')
data.resizable(False,False)
data['bg']='light goldenrod'

a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
def show():
    if(e4.get()==''):
        messagebox.showwarning("Alert","Please enter username")
    else:
        a.set((ca.execute('select name from cabtable where username=?',[(e4.get())])).fetchone())
        b.set((ca.execute('select gender from cabtable where username=?',[(e4.get())])).fetchone())
        c.set((ca.execute('select mobile from cabtable where username=?',[(e4.get())])).fetchone())
        d.set((ca.execute('select email from cabtable where username=?',[(e4.get())])).fetchone())

def lol():
    data.destroy()
    import navigation

def book():
    data.destroy()
    import editprofile

l4=Label(data,text="Username")
l4.grid(row=0,padx=(180,5),pady=(70,5),stick=W)
e4=Entry(data,bd=5,bg='powder blue')
e4.grid(row=0,column=1,pady=(70,5))
b3=Button(data,text="View",command=show,fg='red',bg='gray63')
b3.grid(row=1,column=1)
l1=Label(data,text="Name")
l1.grid(row=2,padx=(180,5),pady=8,stick=W)
e1=Entry(data,bd=5,textvariable=a,state=DISABLED)
e1.grid(row=2,column=1,pady=8)
l7=Label(data,text="Gender")
l7.grid(row=3,padx=(180,5),stick=W)
e7=Entry(data,bd=5,textvariable=b,state=DISABLED)
e7.grid(row=3,column=1)
l2=Label(data,text="Mobile (+91)")
l2.grid(row=4,padx=(180,5),pady=8,stick=W)
e2=Entry(data,bd=5,textvariable=c,state=DISABLED)
e2.grid(row=4,column=1,pady=8)
l3=Label(data,text="Email")
l3.grid(row=5,padx=(180,5),stick=W)
e3=Entry(data,bd=5,textvariable=d,state=DISABLED)
e3.grid(row=5,column=1)

b1=Button(data,text="Edit",command=book,fg='red',bg='gray63')
b1.grid(row=6,column=1,stick=E,pady=8)
b2=Button(data,text="Back",command=lol,fg='red',bg='gray63')
b2.grid(row=6,columnspan=2,padx=(240,0))

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

