from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun():
    if len(route_id.get())==0:
        showerror('Missing Value','Enter route ID')
    
    elif len(station_id.get())==0:
        showerror('Missing Value','Enter station ID')
    elif len(station_name.get())==0:
        showerror('Missing Value','Enter station name')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute("""insert into route values ({},{},"{}")""".format(int(route_id.get()),int(station_id.get()),station_name.get()))
            conn.commit()
            conn.close()
            showinfo('Route Entry ','Route details added')
        except(mysql.connector.errors.IntegrityError):
            showerror('Error','Record already exists')
        except(ValueError):
            showerror('Error','Enter valid values')    
def fun1():
     if len(route_id.get())==0:
        showerror('Missing Value','Enter route ID')
    
     elif len(station_id.get())==0:
        showerror('Missing Value','Enter station ID')
        
     elif len(station_name.get())==0:
        showerror('Missing Value','Enter station name')
        
     else:
         try:
             conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
             cur=conn.cursor()
             cur.execute("""delete from route where rid={} and sid={} and sname="{}" """.format(int(route_id.get()),int(station_id.get()),station_name.get()))
             conn.commit()
             conn.close()
             showinfo('Delete ','Route details deleted')
         except(ValueError):
            showerror('Error','Enter  valid values')
def h():
    root.destroy()
    import home
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
Label(root,image=img).grid(row=0,column=0,columnspan=11,pady=20,padx=w//3)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=11,padx=w//3)
Label(root,text='Add Bus Route Details',font='Arial 14 bold',fg='green4').grid(row=2,column=0,columnspan=11,pady=20,padx=w//3)
Label(root,text='Route Id').grid(row=4,column=0,padx=(250,0),pady=40)
route_id=Entry(root)
route_id.grid(row=4,column=1,padx=10)
Label(root,text='Station ID').grid(row=4,column=2)
station_id=Entry(root)
station_id.grid(row=4,column=3,padx=10)
Label(root,text='Station Name').grid(row=4,column=4)
station_name=Entry(root)
station_name.grid(row=4,column=5,padx=10)
Label(root,text='').grid(row=4,column=6)
Label(root,text='').grid(row=4,column=7,padx=10)
Button(root,text='Add Route',bg='SpringGreen2',command=fun).grid(row=4,column=8)
Button(root,text='Delete Route',bg='SpringGreen2',fg='red',command=fun1).grid(row=4,column=9,padx=10)
Button(root,image=home,command=h).grid(row=5,column=7)
