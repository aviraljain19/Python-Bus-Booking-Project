from tkinter import *

root=Tk()
h,w=root.winfo_screenheight(),root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file=".\\Bus_for_project.png")
def fun(self):
    root.destroy()
    import home
Label(root,image=img).pack()
Label(root,text='Online Bus Booking System',font='Arial 18 bold', bg='cadetblue1',fg='red').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='Name: Aviral Jain',fg='blue2',font='Arial 12 bold').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='Er: 211B077',fg='blue2',font='Arial 12 bold').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='Mobile: 6260371790',fg='blue2',font='Arial 12 bold').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='').pack()
Label(root,text='Submitted to: Dr. Mahesh Kumar Sir',font='Arial 16 bold', bg='cadetblue1',fg='red').pack()
Label(root,text='Project Based Learning',fg='red',font='Arial 12 bold').pack()
root.bind('<KeyPress>',fun)
root.mainloop()
