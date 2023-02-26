from tkinter import *
import mysql.connector
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
def fun():
    if len(bus_id.get())==0:
        showerror('Missing Value','Enter BUS ID')
    elif bus_type.get()=='select Bus Type':
        showerror('Missing Value','Select Bus Type')
    elif len(capacity.get())==0:
        showerror('Missing Value','Enter Capacity')
    elif len(fare.get())==0:
        showerror('Missing Value','Enter Fare')
    elif len(operator_id.get())==0:
        showerror('Missing Value','Enter operator ID')
    elif len(route_id.get())==0:
        showerror('Missing Value','Enter route ID')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute("""insert into bus values ({},"{}",{},{},{},{})""".format(int(bus_id.get()),bus_type.get(),int(capacity.get()),int(fare.get()),int(operator_id.get()),int(route_id.get())))
            conn.commit()
            conn.close()
            a=bus_id.get()
            Label(root,text=a).grid(row=5,column=3,pady=10)
            b=bus_type.get()
            Label(root,text=b).grid(row=5,column=4)
            c=capacity.get()
            Label(root,text=c).grid(row=5,column=5)
            d=fare.get()
            Label(root,text=d).grid(row=5,column=6)
            e=operator_id.get()
            Label(root,text=e).grid(row=5,column=7)
            f=route_id.get()
            Label(root,text=f).grid(row=5,column=8)
            showinfo('Bus Entry','Bus record added')
        
        except(ValueError):
            showerror('Error','Enter  valid values')
        
def fun1():
    if len(bus_id.get())==0:
        showerror('Missing Value','Enter BUS ID')
    elif bus_type.get()=='select Bus Type':
        showerror('Missing Value','Select Bus Type')
    elif len(capacity.get())==0:
        showerror('Missing Value','Enter Capacity')
    elif len(fare.get())==0:
        showerror('Missing Value','Enter Fare')
    elif len(operator_id.get())==0:
        showerror('Missing Value','Enter operator ID')
    elif len(route_id.get())==0:
        showerror('Missing Value','Enter route ID')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute("""update bus set bid={},type="{}",capacity={},fare={},opid={},rid={} where bid={}""".format(int(bus_id.get()),bus_type.get(),int(capacity.get()),int(fare.get()),int(operator_id.get()),int(route_id.get()),int(bus_id.get())))
            conn.commit()
            conn.close()
            a=bus_id.get()
            Label(root,text=a).grid(row=5,column=3,pady=10)
            b=bus_type.get()
            Label(root,text=b).grid(row=5,column=4)
            c=capacity.get()
            Label(root,text=c).grid(row=5,column=5)
            d=fare.get()
            Label(root,text=d).grid(row=5,column=6)
            e=operator_id.get()
            Label(root,text=e).grid(row=5,column=7)
            f=route_id.get()
            Label(root,text=f).grid(row=5,column=8)
            showinfo('Operator Entry Update','Operator details updated succesfully')
        except(ValueError):
            showerror('Error','Enter  valid values')
def h():
    root.destroy()
    import home
Label(root,image=img).grid(row=0,column=1,columnspan=11,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=1,columnspan=11)
Label(root,text='Add Bus Details',font='Arial 14 bold',fg='green4').grid(row=2,column=1,columnspan=11,pady=20)
Label(root,text='Bus ID').grid(row=4,column=0,padx=(150,0),pady=40)
bus_id=Entry(root)
bus_id.grid(row=4,column=1,padx=10)
Label(root,text='Bus Type').grid(row=4,column=2)
bus_type=StringVar()
bus_type.set('select Bus Type')
opt=["AC 2x2","AC 3x2","Non AC 2x2","Non AC 3x2","AC-Sleeper 2x1","Non AC-Sleeper 2x1"]
d_menu=OptionMenu(root,bus_type,*opt).grid(row=4,column=3,padx=10)
Label(root,text='Capacity').grid(row=4,column=4)
capacity=Entry(root) 
capacity.grid(row=4,column=5,padx=10)
Label(root,text='Fare Rs').grid(row=4,column=6)
fare=Entry(root)
fare.grid(row=4,column=7,padx=10)
Label(root,text='Operator ID').grid(row=4,column=8)
operator_id=Entry(root)
operator_id.grid(row=4,column=9,padx=10)
Label(root,text='Route ID').grid(row=4,column=10)
route_id=Entry(root)
route_id.grid(row=4,column=11,padx=10)
Button(root,text='Add Bus',bg='SpringGreen2',command=fun).grid(row=6,column=6)
Button(root,text='Edit Bus',bg='SpringGreen2',command=fun1).grid(row=6,column=7,padx=10)
Button(root,image=home,command=h).grid(row=6,column=8)
root.mainloop()
