from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
showinfo('Status','Ticket Booked successfully')
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//3,pady=20)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=3,padx=w//3)
Label(root,text='Bus Ticket',font='Arial 12 bold').grid(row=2,column=0,columnspan=3,padx=w//3,pady=20)
conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
cur=conn.cursor()
cur.execute("""select max(reference_no) from booking_history""")
res1=cur.fetchall()
cur.execute("""select pname,gender,no_of_seats,mobile,age,fare,reference_no,bfrom,dot,bto from booking_history where reference_no={}""".format(res1[0][0]))
res=cur.fetchall()
Label(root,text='Passengers :').grid(row=4,column=0,padx=(w//8,0))
Label(root,text=res[0][0]).grid(row=4,column=0,padx=(w//5,0))
Label(root,text='Gender :').grid(row=4,column=0,padx=(w//2.8,0))
Label(root,text=res[0][1]).grid(row=4,column=0,padx=(w//2.3,0))
Label(root,text='No. of seats :').grid(row=5,column=0,padx=(w//8,0))
Label(root,text=res[0][2]).grid(row=5,column=0,padx=(w//5,0))
Label(root,text='Phone :').grid(row=5,column=0,padx=(w//2.8,0))
Label(root,text=res[0][3]).grid(row=5,column=0,padx=(w//2.3,0))
Label(root,text='Age :').grid(row=6,column=0,padx=(w//8,0))
Label(root,text=res[0][4]).grid(row=6,column=0,padx=(w//5,0))
Label(root,text='Fare rs. :').grid(row=6,column=0,padx=(w//2.8,0))
Label(root,text=(res[0][5]*res[0][2])).grid(row=6,column=0,padx=(w//2.3,0))
Label(root,text='Booking ref. :').grid(row=7,column=0,padx=(w//8,0))
Label(root,text=res[0][6]).grid(row=7,column=0,padx=(w//5,0))
Label(root,text='Boarding Point :').grid(row=7,column=0,padx=(w//2.8,0))
Label(root,text=res[0][7]).grid(row=7,column=0,padx=(w//2.3,0))
Label(root,text='Travel on :').grid(row=8,column=0,padx=(w//8,0))
Label(root,text=res[0][8]).grid(row=8,column=0,padx=(w//5,0))
Label(root,text='Destination Point :').grid(row=8,column=0,padx=(w//2.8,0))
Label(root,text=res[0][9]).grid(row=8,column=0,padx=(w//2.2,0))
conn.commit()
conn.close()
root.mainloop()
