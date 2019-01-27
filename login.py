import sqlite3
from tkinter import *
from tkinter import messagebox
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
data=Tk()
data.geometry('600x400')
data.resizable(False,False)
data.title('LOGIN - CAB BOOKING SYSTEM')
data['bg']='light goldenrod'

def backs():
    if(e1.get()=='' or e2.get()==''):
        messagebox.showwarning('Alert','Please fill out all the particulars')
    elif(len(e1.get())>15):
        messagebox.showwarning('Alert',"Username's max length is 15")
    elif(len(e2.get())>15):
        messagebox.showwarning('Alert',"Password's max length is 15")
    else:
        ca.execute('select * from cabtable where username=? and password=?',[(e1.get()),(e2.get())])
        if ca.fetchall():
            me=''.join((ca.execute('select name from cabtable where username=?',[(e1.get())])).fetchone())
            messagebox.showinfo('Done',"Successfully logged in\nWelcome "+me+' to LPU CAB BOOKING SYSTEM')
            trail=(ca.execute('select name from cabtable where username=?',[(e1.get())])).fetchone()
            data.destroy()
            import booking
        else:
            messagebox.showwarning("Alert","Invalid username or password")

def lol():
    data.destroy()
    import registration
    
def edit():
    data.destroy()
    import editprofile



l1=Label(data,text="Username")
l1.grid(row=0,padx=(180,10),pady=(100,5))
e1=Entry(data,bd=5,bg='powder blue')
e1.grid(row=0,column=1,pady=(100,5))
l2=Label(data,text="Password")
l2.grid(row=1,padx=(180,10))
e2=Entry(data,bd=5,bg='powder blue',show='+')
e2.grid(row=1,column=1)
b=Button(data,text="Submit",command=backs,bg='gray63',fg='red')
b.grid(row=2,column=1,pady=5)
b1=Button(data,text="New",command=lol,bg='gray63',fg='red')
b1.grid(row=2,column=1,stick=E)
b2=Button(data,text="Forgot Password",command=edit,bg='gray63',fg='red')
b2.grid(row=3,columnspan=2,sticky=E)


menubar=Menu(data)

def hz():
   data.destroy()
   import navigation
homemenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Home", command=hz)

def log():
   data.destroy()
   import login
logmenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Login", command=log)

def sign():
   data.destroy()
   import registration
signmenu=Menu(menubar,tearoff=0)
menubar.add_command(label="Sign Up", command=sign)

def book():
   data.destroy()
   import booking
bookmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Book Cab", command=book)

def prof():
   data.destroy()
   import profile
def edit():
   data.destroy()
   import editprofile
def ride():
   data.destroy()
   import rides
accountmenu=Menu(menubar,tearoff=0)
accountmenu.add_command(label="Profile",command=prof)
accountmenu.add_command(label="Edit Profile",command=edit)
accountmenu.add_command(label="Rides",command=ride)

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
