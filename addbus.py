from tkinter import *
from tkinter.messagebox import *
root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def ope():
    root.destroy()
    import operator
def newb():
    root.destroy()
    import busdetails
def newr():
    root.destroy()
    import newroute
def newrun():
    root.destroy()
    import newrun
img=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=img).grid(row=0,column=0,columnspan=4,padx=(500,0),pady=10)
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').grid(row=1,column=0,columnspan=4,padx=(500,0))
Label(root,text='Add New Details to DataBase',font='Arial 14 bold',fg='green4').grid(row=2,column=0,columnspan=4,padx=(500,0),pady=20)
Button(root,text='New Operator',bg='SpringGreen2',command=ope).grid(row=3,column=0,padx=(500,50))
Button(root,text='New Bus',bg='orange red',command=newb).grid(row=3,column=1,padx=50)
Button(root,text='New Route',bg='DodgerBlue3',command=newr).grid(row=3,column=2,padx=50)
Button(root,text='New Run',bg='pink4',command=newrun).grid(row=3,column=3,padx=50)
root.mainloop()
