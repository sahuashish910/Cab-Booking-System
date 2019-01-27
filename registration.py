import sqlite3
from tkinter import *
import re
from tkinter import messagebox
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
data=Tk()
data.geometry('600x400')
data.resizable(False,False)
data.title('REGISTRATION - CAB BOOKING SYSTEM')
data['bg']='light goldenrod'

va=StringVar()
def back():
    a,t,k,u,d=0,0,0,0,0
    for i in e1.get():
        if i.isdigit():
            a=1
    for i in e5.get():
        if i.isupper():
            t=1
        if i.islower():
            u=1
        if i.isdigit():
            d=1
        if i in ('@'):
            k=1
    if(e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()=='' or e5.get()=='' or e6.get()==''):
        messagebox.showwarning('Alert','Please fill out all the particulars')
    elif(len(e1.get())<4 or len(e1.get())>20):
        messagebox.showwarning('Alert','Name length must be between 4 to 20')
    elif(a==1):
        messagebox.showwarning('Alert','Name must contain only characters')
    elif(e2.get().isdigit()==False):
        messagebox.showwarning('Alert','Mobile number must contain only digits')
    elif(len(e2.get())!=10):
        messagebox.showwarning('Alert','Mobile number must contain 10 digits')
    elif(re.search('\w+\.*\w+@+(gmail|rdiffmail|yahoo)+\.+(com|edu|org|in)',e3.get())==None):
        messagebox.showwarning('Alert','Email is not in proper format')
    elif(len(e4.get())<5 or len(e4.get())>15):
        messagebox.showwarning('Alert','Username length must be between 5 to 15')
    elif(e4.get().isalnum()==False):
        messagebox.showwarning('Alert','Username can only contain digits or characters')
    elif(len(e5.get())<4 or len(e5.get())>15):
        messagebox.showwarning('Alert','Password length must be between 4 to 15')
    elif(t!=1 or u!=1 or d!=1 or k!=1):
        messagebox.showwarning("Alert","Password must contain atleast one in A-Z,a-z,0-9 and @")
    elif(e6.get()!=e5.get()):
        messagebox.showwarning("Alert","Passwords are not matching")
    else:
        ca.execute('select * from cabtable where mobile=?',[(e2.get())])
        if ca.fetchall():
            messagebox.showwarning("Alert","Mobile no. already registered")
        else:
            messagebox.showinfo("Done","Successfully registered")
            ca.execute("insert into cabtable (name,gender,mobile,email,username,password) values(?,?,?,?,?,?)",(e1.get(),va.get(),e2.get(),e3.get(),e4.get(),e5.get()))
            db.commit()
            data.destroy()
            import login
        
def cancel():
    data.destroy()
    import navigation
    

l1=Label(data,text="Name")
l1.grid(row=0,padx=(180,5),pady=(70,5),stick=W)
e1=Entry(data,bd=5,bg='powder blue')
e1.grid(row=0,column=1,pady=(70,5))
l11=Label(data,text="Gender")
l11.grid(row=1,padx=(180,5),stick=W)
R1=Radiobutton(data,text="Male",variable=va,value='Male')
R1.grid(row=1,column=1,stick=W)
R2=Radiobutton(data,text="Female",variable=va,value='Female')
R2.grid(row=1,column=1,stick=E)
l2=Label(data,text="Mobile (+91)")
l2.grid(row=2,padx=(180,5),pady=8,stick=W)
e2=Entry(data,bd=5,bg='powder blue')
e2.grid(row=2,column=1,pady=8)
l3=Label(data,text="Email")
l3.grid(row=3,padx=(180,5),stick=W)
e3=Entry(data,bd=5,bg='powder blue')
e3.grid(row=3,column=1)
l4=Label(data,text="Username")
l4.grid(row=4,padx=(180,5),pady=8,stick=W)
e4=Entry(data,bd=5,bg='powder blue')
e4.grid(row=4,column=1,pady=8)
l5=Label(data,text="Password")
l5.grid(row=5,padx=(180,5),stick=W)
e5=Entry(data,bd=5,show='+',bg='powder blue')
e5.grid(row=5,column=1)
l6=Label(data,text="Retype\nPassword")
l6.grid(row=6,padx=(180,5),pady=8,stick=W)
e6=Entry(data,bd=5,show='+',bg='powder blue')
e6.grid(row=6,column=1,pady=8)
b1=Button(data,text="Cancel",command=cancel,bg='gray63',fg='red')
b1.grid(row=7,column=1,stick=E)
b=Button(data,text="Submit",command=back,bg='gray63',fg='red')
b.grid(row=7,columnspan=2,padx=(200,0))


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


