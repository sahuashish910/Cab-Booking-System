import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime
import time
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
data=Tk()
data.title('BOOKING - CAB BOOKING SYSTEM')
data.geometry('600x400')
data.resizable(False,False)
data['bg']='light goldenrod'

def lol():
    data.destroy()
    import navigation

def dates():
    if(e5.get()=='' or e6.get()==''):
        messagebox.showwarning('ALERT','Please fill out date and time')
    elif(len(e5.get())!=10 or e5.get()[2]!='/' or e5.get()[5]!='/'):
        messagebox.showwarning('ALERT','Input date is not valid')
    elif(len(e6.get())!=5 or e6.get()[2]!=':'):
        messagebox.showwarning('ALERT','Input time is not valid')
    else:
        day,month,year=(e5.get()).split('/')
        valid=True
        try:
            (datetime.datetime(int(year),int(month),int(day)))
        except ValueError:
            valid=False
        ho,mi=(e6.get()).split(':')
        val=True
        try:
            (datetime.datetime(int(year),int(month),int(day),int(ho),int(mi)))
        except ValueError:
            val=False
        r=datetime.datetime.today()
        if(valid==False or (datetime.datetime(int(year),int(month),int(day),int(23),int(59),int(59)))<datetime.datetime.today() or (datetime.datetime(int(year),int(month),int(day)))>datetime.datetime(2050, 12, 31)):
            messagebox.showwarning('ALERT','Input date is not valid')
        else:
            if(valid==True and r.strftime('%d')==day and r.strftime('%m')==month):
                if(val==False or (datetime.datetime(int(year),int(month),int(day),int(ho),int(mi),int(59)))<datetime.datetime.today()):
                    messagebox.showwarning('ALERT','Input time is not valid')
                else:
                    a=(datetime.datetime(int(year),int(month),int(day))).strftime('%A')
                    s.set(a)
            else:
                if(val==False):
                    messagebox.showwarning('ALERT','Input time is not valid')
                else:
                    a=(datetime.datetime(int(year),int(month),int(day))).strftime('%A')
                    s.set(a)

def book():
    if(e1.get()=='' or e5.get()=='' or e6.get()=='' or e7.get()=='' or e8.get()=='0'):
        messagebox.showwarning('ALERT','Please fill out all the field')
    elif(len(e1.get())!=10 or e1.get().isdigit()==False):
        messagebox.showwarning('ALERT','Mobile no. is not valid')
    elif(var1.get()==var2.get()):
        messagebox.showwarning('ALERT','Source & destination are same')
    else:
        ca.execute('select * from cabtable where mobile=?',[(e1.get())])
        if ca.fetchall():
            messagebox.showinfo('DONE','Booking Done')
            ca.execute("update cabtable set start=?,end=?,cab=?,date=?,time=?,day=?,fare=? where mobile=?",(var1.get(),var2.get(),var3.get(),e5.get(),e6.get(),e7.get(),e8.get(),e1.get()))
            db.commit()
            data.destroy()
            import navigation
        else:
            messagebox.showwarning('ALERT','Mobile no. is not registered')
            data.destroy()
            import registration

def fares():
    if(var3.get()=='Auto'):
        var.set(50)
    elif(var3.get()=='E-Rickshaw'):
        var.set(100)
    elif(var3.get()=='Micro'):
        var.set(150)
    elif(var3.get()=='Mini'):
        var.set(200)
    else:
        var.set(300)
            
s=StringVar()    

var1=StringVar(data)
var1.set('Boys Hostel 1')

var2=StringVar(data)
var2.set('Main Gate')

var3=StringVar(data)
var3.set('Auto')

var=IntVar()

l1=Label(data,text="Mobile (+91)")
l1.grid(row=0,column=0,padx=(180,5),pady=(40,8),stick=W)
e1=Entry(data,bd=5,bg='powder blue')
e1.grid(row=0,column=1,pady=(40,8))

l2=Label(data,text="From")
l2.grid(row=1,column=0,padx=(180,5),stick=W)
optionfrom=OptionMenu(data,var1,'Main Gate','Uni Hospital','School of Pharmacy','Business Block','Admission Block','Boys Hostel 1','Boys Hostel 2','Boys Hostel 3,4','Boys Hostel 5,6','School of ME','Girls Hostel 1,2,3,4','Girls Hostel 5,6')
optionfrom.grid(row=1,column=1)

l3=Label(data,text="To")
l3.grid(row=2,column=0,padx=(180,5),pady=8,stick=W)
optionto=OptionMenu(data,var2,'Main Gate','Uni Hospital','School of Pharmacy','Business Block','Admission Block','Boys Hostel 1','Boys Hostel 2','Boys Hostel 3,4','Boys Hostel 5,6','School of ME','Girls Hostel 1,2,3,4','Girls Hostel 5,6')
optionto.grid(row=2,column=1,pady=8)

l4=Label(data,text="Cab")
l4.grid(row=3,column=0,padx=(180,5),stick=W)
optioncab=OptionMenu(data,var3,'Auto','E-Rickshaw','Micro','Mini','Bike','Scooty')
optioncab.grid(row=3,column=1)

l5=Label(data,text="Date[dd/mm/year]")
l5.grid(row=4,column=0,padx=(180,5),pady=8,stick=W)
e5=Entry(data,bd=5,bg='powder blue')
e5.grid(row=4,column=1,pady=8)

l6=Label(data,text="Time(24hr)[hh:mm]")
l6.grid(row=5,column=0,padx=(180,5),stick=W)
e6=Entry(data,bd=5,bg='powder blue')
e6.grid(row=5,column=1)

b3=Button(data,text="Calculate Day",command=dates,fg='red',bg='gray63')
b3.grid(row=6,column=0,padx=(180,5),pady=8,stick=W)
e7=Entry(data,bd=5,textvariable=s,state=DISABLED)
e7.grid(row=6,column=1,pady=8)

b4=Button(data,text="Fare Rs",command=fares,fg='red',bg='gray63')
b4.grid(row=7,column=0,padx=(180,5),stick=W)
e8=Entry(data,bd=5,text=var,state=DISABLED)
e8.grid(row=7,column=1)

b1=Button(data,text="Book",command=book,fg='red',bg='gray63')
b1.grid(row=8,columnspan=2,padx=(240,0),pady=8)
b2=Button(data,text="Cancel",command=lol,fg='red',bg='gray63')
b2.grid(row=8,column=1,stick=E)

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
