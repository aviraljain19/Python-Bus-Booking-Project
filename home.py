from tkinter import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def seat():
    root.destroy()
    import journey_details
def check():
    root.destroy()
    import checkbooking
def add():
    root.destroy()
    import addbus
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//3)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=3,padx=w//3)
Label(root,text='').grid(row=2,column=1)
Label(root,text='').grid(row=3,column=1)
Button(root,text='Seat Booking',bg='green2',command=seat).grid(row=4,column=0)
Button(root,text='Check Booked Seat', bg='green3',command=check).grid(row=4,column=1)
Button(root,text='Add Bus Details', bg='green4',command=add).grid(row=4,column=2)
Label(root,text='').grid(row=5,column=1)
Label(root,text='For admin only',fg='red').grid(row=6,column=2)
root.mainloop()
