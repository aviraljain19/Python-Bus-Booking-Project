from tkinter import *
from tkinter.messagebox import *
import mysql.connector
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
fr=Frame(root)
fr.grid(row=0,column=0,columnspan=10)
def fun2():
    try:
        s=int(no.get())
        conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
        cur=conn.cursor()
        cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                    as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                    and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
        res=cur.fetchall()
        cur.execute(""" select sum(no_of_seats) from booking_history group by dot having dot="{}" """.format(journey.get()))
        r=cur.fetchall()
        if(res[0][2]-r[0][0]<s):
            showerror("Error","Entered no. of seats not available")
        else:
            try:
                t1=int(no.get())
                t2=int(mobile.get())
                t3=int(age.get())
    
                if len(name.get())==0:
                    showerror('Value Missing','Please Enter Name')
                elif gender.get()=='Select Gender':
                    showerror('Value Missing','Please select gender')
                elif t1==0:
                    showerror('Value Missing','Please Enter No. of Seats')
                elif (t2<1111111111 or t2>9999999999):
                    showerror('Value Error','Check Mobile Number')
                elif t3==0:
                    showerror('Value Missing','Please Enter Age')        
                else:
                    try:
                        conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                        cur=conn.cursor()
        
                        cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                            as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                            and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
                        res=cur.fetchall()
                        conn.commit()
                        conn.close()
                        r=askquestion('Fare Confirm','Total amount to be paid rs. {}'.format((int(res[0][4]))*int((no.get()))))
                        if r=='yes':
                            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                            cur=conn.cursor()
                            cur.execute(""" insert into booking_history(mobile,pname, gender,age,no_of_seats,dob,bfrom,bto,dot,bname,fare,bid) values({},"{}","{}",{},{},current_date,"{}","{}","{}","{}",{},{})""".format(int(mobile.get()),name.get(),gender.get(),int(age.get()),int(no.get()),From.get(),to.get(),journey.get(),res[0][0],res[0][4],res[0][5]))
                            conn.commit()
                            conn.close()
                            root.destroy()
                            import ticket
                            
                    except(ValueError):
                        showerror('Error','Enter valid values')
            except(ValueError):
                        showerror('Error','Enter valid values')
    except(ValueError,IndexError):
        conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
        cur=conn.cursor()
        
        cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                            as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                            and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
        res=cur.fetchall()
        a=int(no.get())
        if(a>res[0][3]):
            showerror("Error","Entered no. of seats not available")
        else:
            try:
                t1=int(no.get())
                t2=int(mobile.get())
                t3=int(age.get())
    
                if len(name.get())==0:
                    showerror('Value Missing','Please Enter Name')
                elif gender.get()=='Select Gender':
                    showerror('Value Missing','Please select gender')
                elif t1==0:
                    showerror('Value Missing','Please Enter No. of Seats')
                elif (t2<1111111111 or t2>9999999999):
                    showerror('Value Error','Check Mobile Number')
                elif t3==0:
                    showerror('Value Missing','Please Enter Age')        
                else:
                    try:
                        conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                        cur=conn.cursor()
        
                        cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                            as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                            and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
                        res=cur.fetchall()
                        conn.commit()
                        conn.close()
                        r=askquestion('Fare Confirm','Total amount to be paid rs. {}'.format((int(res[0][4]))*int((no.get()))))
                        if r=='yes':
                            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                            cur=conn.cursor()
                            cur.execute(""" insert into booking_history(mobile,pname, gender,age,no_of_seats,dob,bfrom,bto,dot,bname,fare,bid) values({},"{}","{}",{},{},current_date,"{}","{}","{}","{}",{},{})""".format(int(mobile.get()),name.get(),gender.get(),int(age.get()),int(no.get()),From.get(),to.get(),journey.get(),res[0][0],res[0][4],res[0][5]))
                            conn.commit()
                            conn.close()
                            root.destroy()
                            import ticket
                    
                    except(ValueError):
                        showerror('Error','Enter valid values')
            except(ValueError):
                showerror('Error','Enter valid values')
        conn.commit()
        conn.close()
        
def passenger():
    if bus_select.get()==0:
        showerror('Value Missing','Please Select Bus')
    else:
        try:
            Label(root,text='Fill Passenger Details to book the bus ticket',font='Arial 16 bold', bg='cadetblue1',fg='red').grid(row=8,column=0,columnspan=10,pady=20,padx=w//3)
            Label(root,text='').grid(row=9,column=1)
            Label(root,text='Name').grid(row=10,column=0)
    
            name.grid(row=10,column=1)
            Label(root,text='Gender').grid(row=10,column=2)
    
            gender.set('Select Gender')
            opt=["Male","female","other"]
            d_menu=OptionMenu(root,gender,*opt).grid(row=10,column=3)
            Label(root,text='No of seats').grid(row=10,column=4)
    
            no.grid(row=10,column=5)
            Label(root,text='Mobile No').grid(row=10,column=6)
    
            mobile.grid(row=10,column=7)
            Label(root,text='Age').grid(row=10,column=8)
    
            age.grid(row=10,column=9)
            Button(root,text='Book seat', bg='green2',command=fun2).grid(row=11,column=0,columnspan=10,padx=w//3,pady=20)
        except(ValueError):
            showerror('Error','Enter valid values')
def showbus():
    try:
        conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
        cur=conn.cursor()
        cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                    as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                    and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
        res=cur.fetchall()
        cur.execute(""" select sum(no_of_seats) from booking_history group by dot having dot="{}" """.format(journey.get()))
        r=cur.fetchall()
        if(res[0][2]-r[0][0]==0):
            showerror('Full','Seats are full')
    
    
        else:
        
            try:
                Label(root,text='Select Bus',fg='green4').grid(row=5,column=1, padx=(150,20),pady=10)
                Label(root,text='Operator',fg='green4').grid(row=5,column=2, pady=10)
                Label(root,text='Bus Type',fg='green4').grid(row=5,column=3, padx=20,pady=10)
                Label(root,text='Capacity',fg='green4').grid(row=5,column=4, pady=10)
                Label(root,text='Available',fg='green4').grid(row=5,column=5, padx=20,pady=10)
                Label(root,text='Fare',fg='green4').grid(row=5,column=6,pady=10)
                conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
                cur=conn.cursor()
                cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                    as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                    and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
                res=cur.fetchall()
                try:
                
                    cur.execute(""" select sum(no_of_seats) from booking_history group by dot having dot="{}" """.format(journey.get()))
                    r=cur.fetchall()
            
                    Label(root,text=res[0][0]).grid(row=6,column=2)
                    Label(root,text=res[0][1]).grid(row=6,column=3)
                    Label(root,text=res[0][3]).grid(row=6,column=4)
                    Label(root,text=res[0][2]-r[0][0]).grid(row=6,column=5)
        
                    Label(root,text=res[0][4]).grid(row=6,column=6)
                    Radiobutton(root,text='Bus1',variable=bus_select,value=1).grid(row=6,column=1)

                    Label(root,text=res[1][0]).grid(row=7,column=2)
                    Label(root,text=res[1][1]).grid(row=7,column=3)
                    Label(root,text=res[1][3]).grid(row=7,column=4)
                    Label(root,text=res[1][2]).grid(row=7,column=5)
        
                    Label(root,text=res[1][4]).grid(row=7,column=6)
                    Radiobutton(root,text='Bus2',variable=bus_select,value=2).grid(row=7,column=1)

                    
                
     
                    Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7, padx=20)
                except(ValueError,IndexError):
                    Label(root,text=res[0][0]).grid(row=6,column=2)
                    Label(root,text=res[0][1]).grid(row=6,column=3)
                    Label(root,text=res[0][3]).grid(row=6,column=4)
                    Label(root,text=res[0][2]-r[0][0]).grid(row=6,column=5)
        
                    Label(root,text=res[0][4]).grid(row=6,column=6)
                    Radiobutton(root,text='Bus1',variable=bus_select,value=1).grid(row=6,column=1)
                    Label(root,text=res[1][0]).grid(row=7,column=2)
                    Label(root,text=res[1][1]).grid(row=7,column=3)
                    Label(root,text=res[1][3]).grid(row=7,column=4)
                    Label(root,text=res[1][2]).grid(row=7,column=5)
        
                    Label(root,text=res[1][4]).grid(row=7,column=6)
                    Radiobutton(root,text='Bus2',variable=bus_select,value=2).grid(row=7,column=1)
                    
                
     
                    Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7, padx=20)
                
            except(ValueError):
                showerror('Error','Enter valid values')
            except(mysql.connector.errors.DatabaseError):
                showerror('Date Error','Enter date in format yyyy-mm-dd')
            except(IndexError):
                showerror('Not Found','Bus not found')
        conn.commit()
        conn.close()
    except(ValueError,IndexError):
        try:
            Label(root,text='Select Bus',fg='green4').grid(row=5,column=1, padx=(150,20),pady=10)
            Label(root,text='Operator',fg='green4').grid(row=5,column=2, pady=10)
            Label(root,text='Bus Type',fg='green4').grid(row=5,column=3, padx=20,pady=10)
            Label(root,text='Capacity',fg='green4').grid(row=5,column=4, pady=10)
            Label(root,text='Available',fg='green4').grid(row=5,column=5, padx=20,pady=10)
            Label(root,text='Fare',fg='green4').grid(row=5,column=6,pady=10)
            conn=mysql.connector.connect(host='localhost',user='root',password='Aviral@2004',database='bus_booking')
            cur=conn.cursor()
            cur.execute(""" select O.name,B.type,R.seat_available,B.capacity,B.fare,B.bid from operator as O,bus as B, runs as R, route as F, route
                    as T where F.sname="{}" and T.sname="{}" and F.rid=T.rid and F.sid<T.sid and R.date="{}" and B.rid=T.rid
                    and o.opid=b.opid""".format(From.get(),to.get(),journey.get()))
            res=cur.fetchall()
            try:
                
                cur.execute(""" select sum(no_of_seats) from booking_history group by dot having dot="{}" """.format(journey.get()))
                r=cur.fetchall()
            
                Label(root,text=res[0][0]).grid(row=6,column=2)
                Label(root,text=res[0][1]).grid(row=6,column=3)
                Label(root,text=res[0][3]).grid(row=6,column=4)
                Label(root,text=res[0][2]).grid(row=6,column=5)
        
                Label(root,text=res[0][4]).grid(row=6,column=6)
                Radiobutton(root,text='Bus1',variable=bus_select,value=1).grid(row=6,column=1)

                
     
                Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7, padx=20)
            except(ValueError,IndexError):
                Label(root,text=res[0][0]).grid(row=6,column=2)
                Label(root,text=res[0][1]).grid(row=6,column=3)
                Label(root,text=res[0][3]).grid(row=6,column=4)
                Label(root,text=res[0][2]).grid(row=6,column=5)
        
                Label(root,text=res[0][4]).grid(row=6,column=6)
                Radiobutton(root,text='Bus1',variable=bus_select,value=1).grid(row=6,column=1)
                
     
                Button(root,text='Proceed To Book', bg='green2', command=passenger).grid(row=6,column=7, padx=20)
            conn.commit()
            conn.close()     
        except(ValueError):
            showerror('Error','Enter valid values')
        except(mysql.connector.errors.DatabaseError):
            showerror('Date Error','Enter date in format yyyy-mm-dd')
        except(IndexError):
            showerror('Not Found','Bus not found')
        
def fun1():
    try:
        if len(to.get())==0:
            showerror('Value Missing','Please Enter Destination')
        elif len(From.get())==0:
            showerror('Value Missing','Please Enter From')
        elif len(journey.get())==0:
            showerror('Value Missing','Please Enter Date')
        else:
        
            showbus()
    except(mysql.connector.errors.DatabaseError):
        showerror("Date Error","Enter date in yyyy-mm-dd format")
        
def h():
    root.destroy()
    import home
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,text='                 ').grid(row=0,column=0)
Label(root,image=img).grid(row=0,column=0,columnspan=10,padx=w//3)
Label(root,text='                 ').grid(row=1,column=0)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=10,padx=w//3)
Label(root,text='                 ').grid(row=3,column=0)
Label(root,text='').grid(row=2,column=1)
Label(root,text='Enter Journey Details',font='Arial 14 bold', bg='green2',fg='green4').grid(row=3,column=0,columnspan=10,pady=10,padx=w//3)
Label(root,text='To').grid(row=4,column=1)
to=Entry(root)
to.grid(row=4,column=2)
Label(root,text='From').grid(row=4,column=3)
From=Entry(root)
From.grid(row=4,column=4)
Label(root,text='Journey Date').grid(row=4,column=5)
journey=Entry(root)
journey.grid(row=4,column=6)
home=PhotoImage(file='.//home.png')
Button(root,image=home,command=h).grid(row=4,column=8,padx=30)  
Button(root,text='Show Bus', bg='springgreen4',command=fun1).grid(row=4,column=7,padx=30)
name=Entry(root)
no=Entry(root)
mobile=Entry(root)
age=Entry(root)
gender=StringVar()
bus_select=IntVar()
root.mainloop()
