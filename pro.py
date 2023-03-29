from tkinter import *
from tkinter import messagebox
from functools import partial
import tkinter as tk
import subprocess as sp
import pymysql


m=tk.Tk()
m.title("book")
m.geometry("950x625")


db_connection=pymysql.connect(
    host="localhost",
    user="root",
    passwd="vinoth18",
    database="projcet"
    )
my_database=db_connection.cursor()
print("connecter")


def of ():
    f = Frame(m, width='1100', height='1000', bg='purple')
    f.pack()
    def fp():
        f1 = Frame(f, width='1100', height='1000', bg='orange')
        f1.pack()
        l=Label(f1,text="SIGN UP:",font=("harem",30,"bold"))
        l.place(x=35,y=10) #f1
        l1=Label(f1,text="First name:",font=("arial",15)).place(x=110,y=80)
        e1=Entry(f1,width=20,font=("arial",15))#,height=2
        e1.place(x=110,y=120)
        l2=Label(f1,text="Last name:",font=("arial",15)).place(x=110,y=160)
        e2=Entry(f1,width=20,font=("arial",15))
        e2.place(x=110,y=200)
        l3=Label(f1,text="Age:",font=("arial",15)).place(x=110,y=240)
        e3=Entry(f1,width=20,font=("arial",15))
        e3.place(x=110,y=280)
        l4=Label(f1,text="Gender:",font=("arial",15)).place(x=110,y=320)
        e4=Entry(f1,width=20,font=("arial",15))
        e4.place(x=110,y=360)
        l5=Label(f1,text="Phone number:",font=("arial",15)).place(x=650,y=80)
        e5=Entry(f1,width=20,font=("arial",15))
        e5.place(x=650,y=120)
        l6=Label(f1,text="Email:",font=("arial",15)).place(x=650,y=160)
        e6=Entry(f1,width=20,font=("arial",15))
        e6.place(x=650,y=200)
        l7=Label(f1,text="Password:",font=("arial",15)).place(x=650,y=240)
        e7=Entry(f1,width=20,font=("arial",15))
        e7.place(x=650,y=280)
        l8=Label(f1,text="Confirm Password:",font=("arial",15)).place(x=650,y=320)
        e8=Entry(f1,width=20,font=("arial",15))
        e8.place(x=650,y=360)
        l9=Label(f1,text="OR",font=("harem",25,"bold")).place(x=435,y=485)
        def sign ():
            gmail=e6.get()
            Passwd=e7.get()
            conpasswd=e8.get()
            
            sql_statement="INSERT INTO login(gmail,Passwd,conpasswd)value(%s,%s,%s)"
            values=(e6.get(),e7.get(),e8.get())
            my_database.execute(sql_statement,values)
            db_connection.commit()
            print ("success")
            if(e6.get() and e7.get() and e8.get() and e7.get()==e8.get()):
                messagebox.showinfo("showinfo","registered successfully")
            elif(e7.get()!=e8.get()):
                messagebox.showinfo("showinfo","mis match")
            else:
                 messagebox.showinfo("showinfo","pls fill the details")
                
            
            
            
            
        
        bu=Button(f1,text="REGISTER",width=25,font=("arial",15),command=sign  ,bg="pink",fg="white")
        bu.place(x=325,y=420)
        
        def sp():
            f3 = Frame(f1, width='1100', height='1000', bg='indigo')
            f3.pack()
            l1=Label(f3,text="Email:",font=("arial",15))
            l1.place(x=400,y=200)
            e1=Entry(f3,width=20,font=("arial",15))
            e1.place(x=400,y=230)
            l2=Label(f3,text="Password:",font=("arial",15))
            l2.place(x=400,y=260)
            e2=Entry(f3,width=20,font=("arial",15))
            e2.place(x=400,y=290)
            def read ():
                gmail=e1.get()
                passwd=e2.get()
                sql_statement="SELECT*FROM login where gmail=%s and passwd=%s"
                my_database.execute(sql_statement,[(gmail),(passwd)])
                result=my_database.fetchall()
                print(result)

                if(result):
                    messagebox.showinfo("showinfo","login successful")
                else:
                    messagebox.showinfo("showinfo","Wrong Details Entered")
            def author ():
                f4=Frame(f3, width='1100', height='1000', bg='linen')
                f4.pack()
                def booksname1 ():
                    f5=Frame(f4, width='1100', height='1000', bg='peach puff')
                    f5.pack()
                    
                    bu=Button(f5,text="அழகின் சிரிப்பு",width=30,font=("arial",15),command =book1,bg="red",fg="white")
                    bu.place(x=320,y=100)
                    bu=Button(f5,text="பாண்டியன் பரிசு",width=30,font=("arial",15),command=book2,bg="red",fg="white")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                    bu.place(x=320,y=200)
                    bu=Button(f5,text="குடும்ப விளக்கு ",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=300)
                    bu=Button(f5,text="இருண்ட வீடு",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=400)
                    bu=Button(f5,text="எதிர்பாராத முத்தம",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=500)
                bu=Button(f4,text="Bharati_Dasan",width=30,font=("arial",15),command = booksname1 ,bg="salmon",fg="white")
                bu.place(x=320,y=500)                               
                def booksname2 ():
                    f6=Frame(f4, width='1100', height='1000', bg='peach puff')
                    f6.pack()  
                    bu=Button(f6,text="வாடிவாசல்",width=30,font=("arial",15),command =book3,bg="red",fg="white")
                    bu.place(x=320,y=125)
                    bu=Button(f6,text="ஜீவனாம்சம்",width=30,font=("arial",15),command=book4,bg="red",fg="white")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                    bu.place(x=320,y=250)
                    bu=Button(f6,text="சுதந்திர தாகம்",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=375)
                    bu=Button(f6,text="புதுக்குரல்",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=500)
                bu=Button(f4,text="C.S.Chellappa",width=30,font=("arial",15),command=booksname2,bg="salmon",fg="white")
                bu.place(x=320,y=200)
                def booksname3 ():
                    f7=Frame(f4, width='1100', height='1000', bg='peach puff')
                    f7.pack()  
                    bu=Button(f7,text="கம்பராமாயணம் ",width=30,font=("arial",15),command =book5,bg="red",fg="white")
                    bu.place(x=320,y=100)
                    bu=Button(f7,text="ஏரெழுபது",width=30,font=("arial",15),command=book6,bg="red",fg="white")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                    bu.place(x=320,y=200)
                    bu=Button(f7,text="சடகோபர் அந்தாதி",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=300)
                    bu=Button(f7,text="சரஸ்வதி அந்தாதி ",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=400)
                    bu=Button(f7,text="சிலையெழுபது",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=500)
                bu=Button(f4,text="Kamban",width=30,font=("arial",15),command=booksname3,bg="salmon",fg="white")
                bu.place(x=320,y=300)
                def booksname4 ():
                    f8=Frame(f4, width='1100', height='1000', bg='peach puff')
                    f8.pack()  
                    bu=Button(f8,text="முதற்கனல் ",width=30,font=("arial",15),command =book7,bg="red",fg="white")
                    bu.place(x=320,y=100)
                    bu=Button(f8,text="ரப்பர்",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                    bu.place(x=320,y=200)
                    bu=Button(f8,text="பனிமனிதன்",width=30,font=("arial",15),command=book8,bg="red",fg="white")
                    bu.place(x=320,y=300)
                    bu=Button(f8,text="வெண்முரசு",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=400)
                    bu=Button(f8,text="விஷ்ணுபுரம்",width=30,font=("arial",15),command=m.destroy,bg="red",fg="white")
                    bu.place(x=320,y=500)
                bu=Button(f4,text="Jayamohan",width=30,font=("arial",15),command=booksname4,bg="salmon",fg="white")
                bu.place(x=320,y=400)
                def booksname5 ():
                    f9=Frame(f4, width='1100', height='1000', bg='peach puff')
                    f9.pack()  
                    bu=Button(f9,text="சிலப்பதிகாரம்",width=30,font=("arial",15),command=book9,bg="red",fg="white")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
                    bu.place(x=320,y=225)
                    bu=Button(f9,text="மணி மேகலை",width=30,font=("arial",15),command=book10,bg="red",fg="white")
                    bu.place(x=320,y=350)
                bu=Button(f4,text="Ilango Adigal",width=30,font=("arial",15),command=booksname5,bg="salmon",fg="white")
                bu.place(x=320,y=100)
                 
                
            bu=Button(f3,text="CONFIRM",width=30,font=("arial",15),command = read ,bg="pink",fg="white")
            bu.place(x=325,y=360)            
            bu=Button(f3,text="OPEN",width=30,font=("arial",15),command = author ,bg="pink",fg="white")
            bu.place(x=325,y=460)
        
        
        bu=Button(f1,text="LOGIN",width=25,font=("arial",15),command = sp ,bg="pink",fg="white")
        bu.place(x=325,y=550)
    bu=Button(f,text="SIGN IN",width=30,font=("arial",15),command=fp,bg="gold",fg="white")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    bu.place(x=320,y=300)
    
def book1 ():
    pro="notepad.exe"
    filename="a.txt"
    sp.Popen([pro,filename])
def book2 ():
    pro="notepad.exe"
    filename="பாண்டியன் பரிசு.txt"
    sp.Popen([pro,filename])
def book3 ():
    pro="notepad.exe"
    filename="வாடிவாசல்.txt"
    sp.Popen([pro,filename])
def book4 ():
    pro="notepad.exe"
    filename="ஜீவனாம்சம்.txt"
    sp.Popen([pro,filename]) 
def book5 ():
    pro="notepad.exe"
    filename="கம்பராமாயணம் .txt"
    sp.Popen([pro,filename])
def book6 ():
    pro="notepad.exe"
    filename="ஏரெழுபது .txt"
    sp.Popen([pro,filename])    
def book7 ():
    pro="notepad.exe"
    filename="முதற்கனல் .txt"
    sp.Popen([pro,filename])
def book8 ():
    pro="notepad.exe"
    filename="பனிமனிதன் .txt"
    sp.Popen([pro,filename])
def book9 ():
    pro="notepad.exe"
    filename="சிலப்பதிகாரம்.txt"
    sp.Popen([pro,filename])
def book10 ():
    pro="notepad.exe"
    filename="மணி மேகலை.txt"
    sp.Popen([pro,filename])    
def App ():
    bu=Button(m,text="Vbook",width=25,font=("arial",15),command =of,bg="sky blue",fg="white")
    bu.place(x=325,y=300)
App ()
