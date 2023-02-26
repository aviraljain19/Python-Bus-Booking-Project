from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun():
    try:
        t1=int(check.get())
        if (t1<1111111111 or t1>9999999999):
            showerror('Error Value','Check Mobile Mobile Number')
        else:
            try:
            
                conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                cur=conn.cursor()
                cur.execute("""select pname,gender,age,no_of_seats,mobile,dot,bto,reference_no,bfrom,fare from booking_history where mobile={}""".format(int(check.get())))
                res=cur.fetchall()
                
               
                Label(root,text=res[0][0]).grid(row=5,column=0,padx=(w//11,0))
                Label(root,text='Passengers :').grid(row=5,column=0)
                Label(root,text='Gender :').grid(row=5,column=0,padx=(w//4,0))
                Label(root,text=res[0][1]).grid(row=5,column=0,padx=(w//3.2,0))
                Label(root,text='No. of seats :').grid(row=6,column=0)
                Label(root,text=res[0][3]).grid(row=6,column=0,padx=(w//11,0))
                Label(root,text='Phone :').grid(row=6,column=0,padx=(w//4,0))
                Label(root,text=res[0][4]).grid(row=6,column=0,padx=(w//3,0))
                Label(root,text='Age :').grid(row=7,column=0)
                Label(root,text=res[0][2]).grid(row=7,column=0,padx=(w//11,0))
                Label(root,text='Fare rs. :').grid(row=7,column=0,padx=(w//4,0))
                Label(root,text=(res[0][9]*res[0][3])).grid(row=7,column=0,padx=(w//3.2,0))
                Label(root,text='Booking ref. :').grid(row=8,column=0)
                Label(root,text=res[0][7]).grid(row=8,column=0,padx=(w//11,0))
                Label(root,text='Boarding Point :').grid(row=8,column=0,padx=(w//4,0))
                Label(root,text=res[0][8]).grid(row=8,column=0,padx=(w//3,0))
                Label(root,text='Travel on :').grid(row=9,column=0)
                Label(root,text=res[0][5]).grid(row=9,column=0,padx=(w//11,0))
                Label(root,text='Destination Point :').grid(row=9,column=0,padx=(w//4,0))
                Label(root,text=res[0][6]).grid(row=9,column=0,padx=(w//2.9,0))
                conn.commit()
                conn.close()
            except(ValueError):
                showerror('Error','Enter valid values')
            except(IndexError):
                r=askquestion('Record not found','Do you want to book ticket now?')
                if r=='yes':
                    root.destroy()
                    import journey_details
    except(ValueError):
                showerror('Error','Enter valid values')
                
def b():
    root.destroy()
    import home
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//3,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=3,padx=w//3)
Label(root,text='Check Your Booking',font='Arial 14 bold', bg='green2',fg='green4').grid(row=2,column=0,pady=20,columnspan=3,padx=w//3)
Label(root,text='Enter Your Mobile Number:').grid(row=3,column=0,padx=w//4,pady=20)
check=Entry(root)
check.grid(row=3,column=0,padx=(w//5.5,0))
Button(root,text='Check Booking',command=fun).grid(row=3,column=0,padx=(480,0))
Button(root,text='Back',command=b).grid(row=9,column=1,pady=30)
