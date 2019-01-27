import sqlite3
from tkinter import *
from tkinter import messagebox
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
data=Tk()
data.title('EDIT PROFILE - CAB BOOKING SYSTEM')
data.geometry('600x400')
data.resizable(False,False)
data['bg']='light goldenrod'

a=StringVar()
b=StringVar()
c=StringVar()

def lol():
    data.destroy()
    import navigation

def show():
    if(e4.get()==''):
        messagebox.showwarning("Alert","Please enter username")
    else:
        a.set((ca.execute('select name from cabtable where username=?',[(e4.get())])).fetchone())
        b.set((ca.execute('select gender from cabtable where username=?',[(e4.get())])).fetchone())
        c.set((ca.execute('select password from cabtable where username=?',[(e4.get())])).fetchone())

def done():
    z,t,k,u,d=0,0,0,0,0
    for i in e1.get():
        if i.isdigit():
            z=1
    for i in e3.get():
        if i.isupper():
            t=1
        if i.islower():
            u=1
        if i.isdigit():
            d=1
        if i in ('@'):
            k=1
    if(len(e1.get())<4 or len(e1.get())>20):
        messagebox.showwarning('Alert','Name length must be between 4 to 20')
    elif(a==1):
        messagebox.showwarning('Alert','Name must contain only characters')
    elif(e2.get() not in ('Male','Female')):
        messagebox.showwarning('Alert','Please enter Male or Female')
    elif(len(e3.get())<4 or len(e3.get())>15):
        messagebox.showwarning('Alert','Password length must be between 4 to 15')
    elif(t!=1 or u!=1 or d!=1 or k!=1):
        messagebox.showwarning("Alert","Password must contain atleast one in A-Z,a-z,0-9 and @")
    else:
        messagebox.showinfo("Done","Successfully updated")
        ca.execute("update cabtable set name=?, gender=?, password=? where username=?",(e1.get(),e2.get(),e3.get(),e4.get()))
        db.commit()
        data.destroy()
        import navigation
    


l4=Label(data,text="Username")
l4.grid(row=0,padx=(180,10),pady=(70,5),stick=W)
e4=Entry(data,bd=5,bg='powder blue')
e4.grid(row=0,column=1,pady=(70,5))
b3=Button(data,text="Edit",command=show,fg='red',bg='gray63')
b3.grid(row=1,column=1)
l1=Label(data,text="Name")
l1.grid(row=2,padx=(180,10),pady=8,stick=W)
e1=Entry(data,bd=5,textvariable=a,bg='powder blue')
e1.grid(row=2,column=1,pady=8)
l2=Label(data,text="Gender")
l2.grid(row=3,padx=(180,10),stick=W)
e2=Entry(data,bd=5,textvariable=b,bg='powder blue')
e2.grid(row=3,column=1)
l3=Label(data,text="Password")
l3.grid(row=4,padx=(180,10),pady=8,stick=W)
e3=Entry(data,bd=5,textvariable=c,bg='powder blue')
e3.grid(row=4,column=1,pady=8)

b1=Button(data,text="Submit",command=done,fg='red',bg='gray63')
b1.grid(row=5,columnspan=2,padx=(240,0))
b2=Button(data,text="Back",command=lol,fg='red',bg='gray63')
b2.grid(row=5,column=1,stick=E)

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
