from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
def fun():
    if len(bus_id.get())==0:
        showerror('Missing Value','Enter the Bus ID')
    elif len(date.get())==0:
        showerror('Missing Value','Enter the Date')
    elif len(seat.get())==0:
        showerror('Missing Value','Enter the Seat available')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute("""insert into runs values ({},"{}",{})""".format(int(bus_id.get()),date.get(),int(seat.get())))
            conn.commit()
            conn.close()
            showinfo('New run ','Route details added')
        except(mysql.connector.errors.IntegrityError):
            showerror('Error','Record already exists')
        except(ValueError):
            showerror('Error','Enter valid values')
def fun1():
    if len(bus_id.get())==0:
        showerror('Missing Value','Enter the Bus ID')
    elif len(date.get())==0:
        showerror('Missing Value','Enter the Date')
    elif len(seat.get())==0:
        showerror('Missing Value','Enter the Seat available')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute("""delete from runs where bid={} and date="{}" """.format(int(bus_id.get()),date.get()))
            conn.commit()
            conn.close()
            showinfo('Delete ','Run details deleted')
        except(ValueError):
            showerror('Error','Enter valid values')
def h():
    root.destroy()
    import home    
Label(root,image=img).grid(row=0,column=0,columnspan=11,pady=20,padx=w//2.5)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=11,padx=w//2.5)
Label(root,text='Add Bus Running Details',font='Arial 14 bold',fg='green4').grid(row=2,column=0,columnspan=11,pady=20,padx=w//2.5)
Label(root,text='Bus Id').grid(row=4,column=0,padx=(150,0),pady=40)
bus_id=Entry(root)
bus_id.grid(row=4,column=1,padx=10)
Label(root,text='Running Date').grid(row=4,column=2)
date=Entry(root)
date.grid(row=4,column=3,padx=10)
Label(root,text='Seat Available').grid(row=4,column=4)
seat=Entry(root)
seat.grid(row=4,column=5,padx=10)
Button(root,text='Add Run',bg='SpringGreen2',command=fun).grid(row=4,column=6)
Button(root,text='Delete Run',bg='SpringGreen2',command=fun1).grid(row=4,column=7,padx=10)
Button(root,image=home,command=h).grid(row=5,column=6)
