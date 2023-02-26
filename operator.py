from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun():
    try:
        
        p=int(phone.get())
        if len(opeid.get())==0:
            showerror('Missing Value','Enter the Operator ID')
        elif len(name.get())==0:
            showerror('Missing Value','Enter the Name')
        elif len(address.get())==0:
            showerror('Missing Value','Enter the Address')
        elif (p<1111111111 or p>9999999999):
            showerror('Value Error','Check Phone Number')
        elif len(email.get())==0:
            showerror('Missing Value','Enter the Email')
        else:
        
            try:    
                conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                cur=conn.cursor()
                cur.execute("""insert into operator values ({},"{}","{}","{}",{})""".format(int(opeid.get()),name.get(),address.get(),email.get(),int(phone.get())))
                conn.commit()
                conn.close()
                a=opeid.get()
                Label(root,text=a).grid(row=5,column=3,pady=10)
                b=name.get()
                Label(root,text=b).grid(row=5,column=4)
                c=address.get()
                Label(root,text=c).grid(row=5,column=5)
                d=phone.get()
                Label(root,text=d).grid(row=5,column=6)
                e=email.get()
                Label(root,text=e).grid(row=5,column=7)
                showinfo('Operator Entry ','Operator details added')
            except(mysql.connector.errors.IntegrityError):
                showerror('Error','Record already exists')
            except(ValueError):
                showerror('Error','Enter valid values')
    except(ValueError):
        showerror('Error','Enter valid values')
def fun1():
    if len(opeid.get())==0:
        showerror('Missing Value','Enter the Operator ID')
    elif len(name.get())==0:
        showerror('Missing Value','Enter the Name')
    elif len(address.get())==0:
        showerror('Missing Value','Enter the Address')
    elif len(phone.get())==0:
        showerror('Missing Value','Enter the Phone')
    elif len(email.get())==0:
        showerror('Missing Value','Enter the Email')
    else:
        try:
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute("""update operator set opid={},name="{}",address="{}",email="{}",phone={} where opid={}""".format(int(opeid.get()),name.get(),address.get(),email.get(),int(phone.get()),int(opeid.get())))
            conn.commit()
            conn.close()
            a=opeid.get()
            Label(root,text=a).grid(row=5,column=3,pady=10)
            b=name.get()
            Label(root,text=b).grid(row=5,column=4)
            c=address.get()
            Label(root,text=c).grid(row=5,column=5)
            d=phone.get()
            Label(root,text=d).grid(row=5,column=6)
            e=email.get()
            Label(root,text=e).grid(row=5,column=7)
            showinfo('Operator Entry Update','Operator details updated succesfully')
        except(ValueError):
            showerror('Error','Enter  valid values')
def h():
    root.destroy()
    import home
img=PhotoImage(file=".\\Bus_for_project.png")
home=PhotoImage(file='home.png')
Label(root,image=img).grid(row=0,column=0,columnspan=11,pady=20,padx=w//3)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=11,padx=w//3)
Label(root,text='Add Bus Operator Details',font='Arial 14 bold',fg='green4').grid(row=2,column=0,columnspan=11,pady=20,padx=w//3)
Label(root,text='Operator id').grid(row=4,column=0)
opeid=Entry(root)
opeid.grid(row=4,column=1,padx=10)
Label(root,text='Name').grid(row=4,column=2)
name=Entry(root)
name.grid(row=4,column=3,padx=10)
Label(root,text='Address').grid(row=4,column=4)
address=Entry(root)
address.grid(row=4,column=5,padx=10)
Label(root,text='Phone').grid(row=4,column=6)
phone=Entry(root)
phone.grid(row=4,column=7,padx=10)
Label(root,text='Email').grid(row=4,column=8)
email=Entry(root)
email.grid(row=4,column=9,padx=10)
Button(root,text='Add',bg='SpringGreen2',command=fun).grid(row=4,column=10)
Button(root,text='Edit',bg='SpringGreen2',command=fun1).grid(row=4,column=11,padx=10)
Button(root,image=home,command=h).grid(row=6,column=8,pady=20)
root.mainloop()
