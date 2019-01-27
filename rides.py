import sqlite3
from tkinter import *
from tkinter import messagebox
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
data=Tk()
data.title('RIDES - CAB BOOKING SYSTEM')
data.geometry('600x400')
data.resizable(False,False)
data['bg']='light goldenrod'

def ok():
    data.destroy()
    import navigation
    
a=StringVar()
b=StringVar()
c=StringVar()
d=StringVar()
e=StringVar()
f=StringVar()
g=StringVar()
def show():
    a.set((ca.execute('select start from cabtable where username=?',[(e1.get())])).fetchone())
    b.set((ca.execute('select end from cabtable where username=?',[(e1.get())])).fetchone())
    c.set((ca.execute('select cab from cabtable where username=?',[(e1.get())])).fetchone())
    d.set((ca.execute('select date from cabtable where username=?',[(e1.get())])).fetchone())
    e.set((ca.execute('select time from cabtable where username=?',[(e1.get())])).fetchone())
    f.set((ca.execute('select day from cabtable where username=?',[(e1.get())])).fetchone())
    g.set((ca.execute('select fare from cabtable where username=?',[(e1.get())])).fetchone())

def ko():
    messagebox.showinfo("Done","Successfully deleted")
    ca.execute('update cabtable set start=null,end=null,cab=null,date=null,time=null,day=null,fare=null where username=?',[(e1.get())])
    db.commit()
    data.destroy()
    import navigation

l1=Label(data,text="Username")
l1.grid(row=0,padx=(180,10),pady=(30,5),stick=W)
e1=Entry(data,bd=5,bg='powder blue')
e1.grid(row=0,column=1,pady=(30,5))
b1=Button(data,text="View",fg='red',bg='gray63',command=show)
b1.grid(row=1,column=1)
l2=Label(data,text="From")
l2.grid(row=2,padx=(180,10),pady=8,stick=W)
e2=Entry(data,bd=5,textvariable=a,state=DISABLED)
e2.grid(row=2,column=1,pady=8)
l3=Label(data,text="To")
l3.grid(row=3,padx=(180,10),stick=W)
e3=Entry(data,bd=5,textvariable=b,state=DISABLED)
e3.grid(row=3,column=1)
l4=Label(data,text="Cab")
l4.grid(row=4,padx=(180,10),pady=8,stick=W)
e4=Entry(data,bd=5,textvariable=c,state=DISABLED)
e4.grid(row=4,column=1,pady=8)
l5=Label(data,text="Date")
l5.grid(row=5,padx=(180,10),stick=W)
e5=Entry(data,bd=5,textvariable=d,state=DISABLED)
e5.grid(row=5,column=1)
l6=Label(data,text="Time")
l6.grid(row=6,padx=(180,10),pady=8,stick=W)
e6=Entry(data,bd=5,textvariable=e,state=DISABLED)
e6.grid(row=6,column=1,pady=8)
l7=Label(data,text="Day")
l7.grid(row=7,padx=(180,10),stick=W)
e7=Entry(data,bd=5,textvariable=f,state=DISABLED)
e7.grid(row=7,column=1)
l8=Label(data,text="Total Fare")
l8.grid(row=8,padx=(180,10),pady=8,stick=W)
e8=Entry(data,bd=5,textvariable=g,state=DISABLED)
e8.grid(row=8,column=1,pady=8)

b2=Button(data,text="OK",fg='red',bg='gray63',command=ok)
b2.grid(row=9,columnspan=2,padx=(240,0))
b3=Button(data,text="Delete",fg='red',bg='gray63',command=ko)
b3.grid(row=9,column=1,stick=E)

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

