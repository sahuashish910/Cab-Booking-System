import sqlite3
db=sqlite3.connect("cabdata.db")
ca=db.cursor()
ca.execute("""create table cabtable(name text,gender text,mobile text,email text,username text,password text,start text,end text,cab text,date text,time text,day text,fare text)""")
db.commit()
