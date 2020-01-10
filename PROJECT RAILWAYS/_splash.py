from Tkinter import*
import os
splash=Tk()
splash.title("Ayush khare")
splash.config(bg='red')
splash.geometry('600x200')
Label(splash,text="......").grid()
def spp(event):
    splash.destroy()
    root=Tk()
    root.title("Ayush khare")
    root.config(bg='powder blue')
    root.geometry('500x180')
    Label(root,text="USER_NAME",font="times 20 bold",bg='grey',relief="sunken").grid(row=3,column=1)
    l1=Entry(root,bg='white',font="times 20 bold")
    l1.grid(row=3,column=4)
    Label(root,text="PASSWORD",font="times 20 bold",bg='grey',relief="sunken").grid(row=4,column=1)
    l2=Entry(root,show='#',bd=5,bg='white',font="times 20 bold")
    l2.grid(row=4,column=4)

    def log():
        if l2.get() == "987456" and l1.get() == 'Ayush' :
            l2.delete(0,END)
            Label(root,text='Successfull Login').grid()
            os.startfile("MAIN.py")
        else :
            Label(root,text='Wrong Password').grid()
            

    Button(root,text='Login',command=log,bd=5,font="times 22 bold",pady=3,padx=5,bg='dark grey').grid(row=5,column=2,rowspan=2)
    root.mainloop()
lb=Label(splash,text="Name:\tAyush khare\nEnroll:\t171B043\nProject:\tRailway Ticketing System",bd=5,font="times 20 roman italic",bg='tomato',fg="red",pady=35,padx=35)
lb.bind("<Motion>",spp)
lb.grid(column=0,sticky=E)
splash.mainloop()
