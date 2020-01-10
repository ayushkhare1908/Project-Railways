
from Tkinter import *
import ttk
from project_db import *
import webbrowser
import tkMessageBox
splash=Tk()
splash.title("Ayush khare")
splash.config(bg='red')
splash.geometry('600x200')
def spp(event):
    splash.destroy()
    root=Tk()
    root.config(bg='powder blue')
    root.geometry('1000x768')
    root.title('Ticketing System')
    frame1=Frame(root,bg='powder blue')
    frame1.pack(side=TOP)
    v1=StringVar()
    v2=StringVar()
    v3=StringVar()
    v4=StringVar()
    v5=StringVar()
    v6=StringVar()
    v7=StringVar()
    #**********************************************
    v8=StringVar()
    v9=StringVar()
    v10=StringVar()
    v11=StringVar()
    v12=StringVar()
    v13=StringVar()
    v14=StringVar()
    v15=StringVar()
    v16=StringVar()
    v17=StringVar()
    v18=StringVar()
    v19=StringVar()
    v20=StringVar()
    v21=StringVar()
    v22=StringVar()
    v23=StringVar()
    v24=StringVar()
    v25=StringVar()
    v26=StringVar()
    v27=StringVar()
    v28=StringVar()
    v29=StringVar()
    v30=StringVar()
    v31=StringVar()
    v32=StringVar()
    v33=StringVar()
    v34=StringVar()
    v35=StringVar()
    v36=StringVar()
    v37=StringVar()
    v38=StringVar()
    v39=StringVar()
    v40=StringVar()
    v41=StringVar()
    v42=StringVar()
    v43=StringVar()
    v44=StringVar()
    v45=StringVar()
    v46=StringVar()
    v47=StringVar()
    v48=StringVar()
    v49=StringVar()
    v50=StringVar()
    v51=StringVar()
    v52=StringVar()
    v53=StringVar()
    v54=StringVar()
    v55=StringVar()
    v56=StringVar()
    v57=StringVar()
    v58=StringVar()
    v59=StringVar()
    v60=StringVar()
    v61=StringVar()
    v62=StringVar()
    v63=StringVar()
    v64=StringVar()
    v65=StringVar()
    v66=StringVar()
    v67=StringVar()
    v68=StringVar()
    v69=StringVar()
    v70=StringVar()
    #**********************************************
    frame2=Frame(root,bg='powder blue')
    frame2.pack()

    frame3=Frame(root,bg='powder blue')
    frame3.pack()

    frame4=Frame(root,width=1368,bg='powder blue')


    frame5=Frame(root,bg='powder blue')
    frame5.pack()
    global count
    count=0
    xxx=[]
    def reserve():
        global xxx
        def next1(xx,xxxx,xxxxx,xxxxxx,xxxxxxx,xxxxxxxx):

            tkMessageBox.showinfo('Confirm','reservation successfull')
            tkMessageBox.showinfo('price','total'+' '+str(int(count)*450)+' '+'rs')

            global xxx
            a=[i.get() for i in xxx]
            a1=[i.get() for i in xx]
            a2=[i.get() for i in xxxx]
            a3=[i.get() for i in xxxxx]
            a4=[i.get() for i in xxxxxx]
            a5=[i.get() for i in xxxxxxx]
            a6=[i.get() for i in xxxxxxxx]
            for i in a1:
                if i=='':
                    break
                else:
                    count = count+1
            print count
            print len(a)
            print len(a1)
            
            for i in range(count):
                insert_into_reservation(str(a[0]),a[1],a[2],a[3],a[4],a[5],a[6],a[7],a1[i],a2[i],a3[i],a4[i],a5[i],a6[i])
        
          
            #tkMessageBox.showinfo('Confirm','reservation successfull')
            #tkMessageBox.showinfo('price','total'+' '+str(int(count)*450)+' '+'rs')

                
           
        def Next():
            root.geometry('1368x768')
            frame3.pack_forget()
            frame4.pack(fill=X)
            
            l.config(text='Passenger Details')
            Label(frame4,text='SNo',font='arial 17',padx=20,bd=4,relief=SUNKEN).grid(row=0,sticky=W)
            Label(frame4,text='Name',font='arial 17',width=20,padx=20,bd=4,relief=SUNKEN).grid(row=0,column=1,sticky=W)
            Label(frame4,text='Age',font='arial 17',padx=20,bd=4,relief=SUNKEN).grid(row=0,column=2,sticky=W)
            Label(frame4,text='Sex',font='arial 17',width=8,padx=20,bd=4,relief=SUNKEN).grid(row=0,column=3,sticky=W)
            Label(frame4,text='Berth preference',font='arial 17',width=20,padx=20,bd=4,relief=SUNKEN).grid(row=0,column=4,sticky=W)
            Label(frame4,text='Food preference',font='arial 17',width=10,padx=20,bd=4,relief=SUNKEN).grid(row=0,column=5,sticky=W)
            Label(frame4,text='Senior Citizen',font='arial 17',width=15,padx=20,bd=4,relief=SUNKEN).grid(row=0,column=6,sticky=W)

            Label(frame4,text='1',font='arial 14 ',padx=20,bd=4,relief=SUNKEN,bg='powderblue',pady=10).grid(row=1,sticky=W+E+N+S)
            Label(frame4,text='2',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=2,sticky=W+E+N+S)
            Label(frame4,text='3',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=3,sticky=W+E+N+S)
            Label(frame4,text='4',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=4,sticky=W+E+N+S)
            Label(frame4,text='5',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=5,sticky=W+E+N+S)
            Label(frame4,text='6',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=6,sticky=W+E+N+S)
            Label(frame4,text='7',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=7,sticky=W+E+N+S)
            
            Label(frame4,text='8',font='arial 14 ',padx=20,bd=4,relief=SUNKEN,bg='powderblue',pady=10).grid(row=8,sticky=W+E+N+S)
            Label(frame4,text='9',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=9,sticky=W+E+N+S)
            Label(frame4,text='10',font='arial 14 ',bg='powderblue',padx=20,bd=4,relief=SUNKEN,pady=10).grid(row=10,sticky=W+E+N+S)
            
            e2=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e2.grid(row=1,column=1)

            e3=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e3.grid(row=2,column=1)

            e4=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e4.grid(row=3,column=1)

            e5=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e5.grid(row=4,column=1)

            e6=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e6.grid(row=5,column=1)

            e7=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e7.grid(row=6,column=1)

            e8=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e8.grid(row=7,column=1)

            e9=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e9.grid(row=8,column=1)

            e10=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e10.grid(row=9,column=1)

            e11=Entry(frame4,font='arial 20',bd=4,relief=SUNKEN)
            e11.grid(row=10,column=1)

            f2=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f2.grid(row=1,column=2)

            f3=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f3.grid(row=2,column=2)

            f4=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f4.grid(row=3,column=2)

            f5=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f5.grid(row=4,column=2)

            f6=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f6.grid(row=5,column=2)

            f7=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f7.grid(row=6,column=2)

            f8=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f8.grid(row=7,column=2)

            f9=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f9.grid(row=8,column=2)

            f10=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f10.grid(row=9,column=2)

            f11=Entry(frame4,font='arial 20',width=3,bd=4,relief=SUNKEN)
            f11.grid(row=10,column=2)

            C1=ttk.Combobox(frame4,font='arial 17',textvariable=v17,width=10)
            C1.grid(row=1,column=3)
            C1['values']=['Male','Female']
            v17.set('Select')

            C2=ttk.Combobox(frame4,font='arial 17',textvariable=v18,width=10)
            C2.grid(row=2,column=3)
            C2['values']=['Male','Female']
            v18.set('Select')

            C3=ttk.Combobox(frame4,font='arial 17',textvariable=v19,width=10)
            C3.grid(row=3,column=3)
            C3['values']=['Male','Female']
            v19.set('Select')

            C4=ttk.Combobox(frame4,font='arial 17',textvariable=v20,width=10)
            C4.grid(row=4,column=3)
            C4['values']=['Male','Female']
            v20.set('Select')

            C5=ttk.Combobox(frame4,font='arial 17',textvariable=v21,width=10)
            C5.grid(row=5,column=3)
            C5['values']=['Male','Female']
            v21.set('Select')

            C6=ttk.Combobox(frame4,font='arial 17',textvariable=v22,width=10)
            C6.grid(row=6,column=3)
            C6['values']=['Male','Female']
            v22.set('Select')

            C7=ttk.Combobox(frame4,font='arial 17',textvariable=v23,width=10)
            C7.grid(row=7,column=3)
            C7['values']=['Male','Female']
            v23.set('Select')

            C8=ttk.Combobox(frame4,font='arial 17',textvariable=v24,width=10)
            C8.grid(row=8,column=3)
            C8['values']=['Male','Female']
            v24.set('Select')

            C9=ttk.Combobox(frame4,font='arial 17',textvariable=v25,width=10)
            C9.grid(row=9,column=3)
            C9['values']=['Male','Female']
            v25.set('Select')

            C10=ttk.Combobox(frame4,font='arial 17',textvariable=v26,width=10)
            C10.grid(row=10,column=3)
            C10['values']=['Male','Female']
            v26.set('Select')

            C11=ttk.Combobox(frame4,font='arial 20',textvariable=v27,width=16)
            C11.grid(row=1,column=4)
            C11['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v27.set('Select')

            C12=ttk.Combobox(frame4,font='arial 20',textvariable=v28,width=16)
            C12.grid(row=2,column=4)
            C12['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v28.set('Select')

            C13=ttk.Combobox(frame4,font='arial 20',textvariable=v29,width=16)
            C13.grid(row=3,column=4)
            C13['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side upper berth',' Side Middle Berth']
            v29.set('Select')

            C14=ttk.Combobox(frame4,font='arial 20',textvariable=v30,width=16)
            C14.grid(row=4,column=4)
            C14['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v30.set('Select')

            C15=ttk.Combobox(frame4,font='arial 20',textvariable=v31,width=16)
            C15.grid(row=5,column=4)
            C15['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v31.set('Select')

            C16=ttk.Combobox(frame4,font='arial 20',textvariable=v32,width=16)
            C16.grid(row=6,column=4)
            C16['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v32.set('Select')

            C17=ttk.Combobox(frame4,font='arial 20',textvariable=v33,width=16)
            C17.grid(row=7,column=4)
            C17['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v33.set('Select')

            C18=ttk.Combobox(frame4,font='arial 20',textvariable=v34,width=16)
            C18.grid(row=8,column=4)
            C18['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v34.set('Select')

            C19=ttk.Combobox(frame4,font='arial 20',textvariable=v35,width=16)
            C19.grid(row=9,column=4)
            C19['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v35.set('Select')

            C20=ttk.Combobox(frame4,font='arial 20',textvariable=v36,width=16)
            C20.grid(row=10,column=4)
            C20['values']=[' Lower Berth','Middle Berth',' Upper Berth',' Side Upper berth',' Side Middle Berth']
            v36.set('Select')

            C21=ttk.Combobox(frame4,font='arial 17',textvariable=v37,width=12)
            C21.grid(row=1,column=5)
            C21['values']=['Veg','Non Veg']
            v37.set('Select')

            C22=ttk.Combobox(frame4,font='arial 17',textvariable=v38,width=12)
            C22.grid(row=2,column=5)
            C22['values']=['Veg','Non Veg']
            v38.set('Select')

            C23=ttk.Combobox(frame4,font='arial 17',textvariable=v39,width=12)
            C23.grid(row=3,column=5)
            C23['values']=['Veg','Non Veg']
            v39.set('Select')

            C24=ttk.Combobox(frame4,font='arial 17',textvariable=v40,width=12)
            C24.grid(row=4,column=5)
            C24['values']=['Veg','Non Veg']
            v40.set('Select')

            C25=ttk.Combobox(frame4,font='arial 17',textvariable=v41,width=12)
            C25.grid(row=5,column=5)
            C25['values']=['Veg','Non Veg']
            v41.set('Select')

            C26=ttk.Combobox(frame4,font='arial 17',textvariable=v42,width=12)
            C26.grid(row=6,column=5)
            C26['values']=['Veg','Non Veg']
            v42.set('Select')

            C27=ttk.Combobox(frame4,font='arial 17',textvariable=v43,width=12)
            C27.grid(row=7,column=5)
            C27['values']=['Veg','Non Veg']
            v43.set('Select')

            C28=ttk.Combobox(frame4,font='arial 17',textvariable=v44,width=12)
            C28.grid(row=8,column=5)
            C28['values']=['Veg','Non Veg']
            v44.set('Select')

            C29=ttk.Combobox(frame4,font='arial 17',textvariable=v45,width=12)
            C29.grid(row=9,column=5)
            C29['values']=['Veg','Non Veg']
            v45.set('Select')

            C30=ttk.Combobox(frame4,font='arial 17',textvariable=v46,width=12)
            C30.grid(row=10,column=5)
            C30['values']=['Veg','Non Veg']
            v46.set('Select')

            cb1=Checkbutton(frame4,variable=v47,width=5,onvalue=1)
            cb1.grid(row=1,column=6)

            cb2=Checkbutton(frame4,variable=v48,width=5,onvalue=1)
            cb2.grid(row=2,column=6)

            cb3=Checkbutton(frame4,variable=v49,width=5,onvalue=1)
            cb3.grid(row=3,column=6)

            cb4=Checkbutton(frame4,variable=v50,width=5,onvalue=1)
            cb4.grid(row=4,column=6)

            cb5=Checkbutton(frame4,variable=v51,width=5,onvalue=1)
            cb5.grid(row=5,column=6)

            cb5=Checkbutton(frame4,variable=v52,width=5,onvalue=1)
            cb5.grid(row=6,column=6)

            cb6=Checkbutton(frame4,variable=v53,width=5,onvalue=1)
            cb6.grid(row=7,column=6)

            cb7=Checkbutton(frame4,variable=v54,width=5,onvalue=1)
            cb7.grid(row=8,column=6)

            cb8=Checkbutton(frame4,variable=v55,width=5,onvalue=1)
            cb8.grid(row=9,column=6)

            cb9=Checkbutton(frame4,variable=v56,width=5,onvalue=1)
            cb9.grid(row=10,column=6)
            xx=[e2,e3,e4,e5,e6,e7,e8,e9,e10,e11]
            xxxx=[f2,f3,f4,f5,f6,f7,f8,f9,f10,f11]
            xxxxx=[v17,v18,v19,v20,v21,v22,v23,v24,v25,v26]
            xxxxxx=[v27,v28,v29,v30,v31,v32,v33,v34,v35,v36]
            xxxxxxx=[v37,v38,v39,v40,v41,v42,v43,v44,v45,v46]
            xxxxxxxx=[v47,v48,v49,v50,v51,v52,v53,v54,v55,v56]
            
            Button(frame4,text='Next',font='Arial 17',command=lambda:next1(xx,xxxx,xxxxx,xxxxxx,xxxxxxx,xxxxxxxx)).grid(row=11,column=5,columnspan=1)
            
        root.geometry('1100x650')
        frame2.pack_forget()
        Label(frame3,text='Train Name',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=0,column=0,sticky=W)
        Label(frame3,text='Train number',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=0,column=2,sticky=W)
        Label(frame3,text='From',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=2,column=0,sticky=W)
        Label(frame3,text='Quota',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=3,column=0,sticky=W)
        Label(frame3,text='Boarding Point',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=1,column=0,sticky=W)
        Label(frame3,text='Reservation upto',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=1,column=2,sticky=W)
        Label(frame3,text='To',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=2,column=2,sticky=W)
        Label(frame3,text='Class',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=3,column=2,sticky=W)

        e1=Entry(frame3,font='Arial 17 bold',textvariable=v8)
        e1.grid(row=0,column=1)
        
        
        f1=Entry(frame3,font='Arial 17 bold',textvariable=v9)
        f1.grid(row=1,column=1)

        
        g1=Entry(frame3,font='Arial 17 bold',textvariable=v10)
        g1.grid(row=2,column=1)
        v10.set(str(v1.get()))
        g1.config(state='readonly')
        
        h1=Entry(frame3,font='Arial 17 bold',textvariable=v11)
        h1.grid(row=3,column=1)

        
        i1=Entry(frame3,font='Arial 17 bold',textvariable=v12)
        i1.grid(row=0,column=3)

        
        
        j1=Entry(frame3,font='Arial 17 bold',textvariable=v13)
        j1.grid(row=1,column=3)

        
        k1=Entry(frame3,font='Arial 17 bold',textvariable=v14)
        k1.grid(row=2,column=3)
        v14.set(str(v2.get()))
        k1.config(state='readonly')
        
        l1=Entry(frame3,font='Arial 17 bold',textvariable=v15)
        l1.grid(row=3,column=3)
        v15.set(str(v3.get()))
        l1.config(state='readonly')
        xxx=[i1,e1,l1,g1,k1,h1,f1,j1]
        Button(frame3,text='Next',font='Arial 18',width=10,command=Next,bd=5,relief=RAISED).grid(row=4,column=3,sticky=E)
    def details():
        a=fetch_data(str(v1.get()),str(v2.get()))
        webbrowser.open('www.irctc.co.in')



        
    l=Label(frame1,text='Travelling Ticketing System',bg='powderblue',font='times 40 bold underline',fg='red',pady=31,padx=10)
    l.grid(row=0)


    Label(frame2,text='Source Station Name  ',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=0,sticky=W)
    Label(frame2,text='Destination Station Name ',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=1,sticky=W)

    c=ttk.Combobox(frame2,width=20,font='Arial 15',textvariable=v1)
    c.grid(row=0,column=1,sticky=W)
    v1.set('      --Please Select--')
    c['values']=['Bhopal','indore','ratlam','ujjain','gwalior']

    c2=ttk.Combobox(frame2,width=20,font='Arial 15',textvariable=v2)
    c2.grid(row=1,column=1,sticky=W)
    v2.set('      --Please Select--')
    c2['values']=['Bhopal','indore','ratlam','ujjain','gwalior']

    Label(frame2,text='Select Class Type',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=2,sticky=W)

    c3=ttk.Combobox(frame2,width=20,font='Arial 15',textvariable=v3)
    c3.grid(row=2,column=1,sticky=W)
    v3.set('      --Please Select--')
    c3['values']=['First Ac','Second Ac','Third Ac','AC Chair Car','First Class','Sleeper']

    Label(frame2,text='Select Journey Date ',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=3,sticky=W)
    c4=ttk.Combobox(frame2,width=7,font='Arial 13',textvariable=v4)
    c4.grid(row=3,column=1,sticky=W)
    v4.set('Day')
    c4['values']=[str(i) for i in range(1,32)]

    c5=ttk.Combobox(frame2,width=10,font='Arial 13',textvariable=v5)
    c5.grid(row=3,column=1,sticky=E)
    v5.set('Month')
    c5['values']=[str(i) for i in range(1,13)]

    Label(frame2,text='Depature Time',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=4,sticky=W)
    c6=ttk.Combobox(frame2,width=20,font='Arial 15',textvariable=v6)
    c6.grid(row=4,column=1,sticky=W)
    v6.set('Any time')
    c6['values']=[str(i) for i in range(1,25)]

    Label(frame2,text='Arrival Time',font='Arial 25 bold',bg='powderblue',pady=22,padx=10).grid(row=5,sticky=W)
    c7=ttk.Combobox(frame2,width=20,font='Arial 15',textvariable=v7)
    c7.grid(row=5,column=1,sticky=W)
    v7.set('Any time')
    c7['values']=[str(i) for i in range(1,25)]







    Button(frame2,text='Get Detail',font='Arial 17',command=details).grid(row=6,column=0,sticky=W)
    Button(frame2,text='Reserve',font='Arial 17',command=reserve).grid(row=6,column=1,sticky=W)
    root.mainloop()


lb=Label(splash,text="Name:\tAyush khare\nEnroll:\t171B043\nProject:\tRailway Ticketing System",bd=5,font="times 20 roman italic",bg='tomato',fg="red",pady=35,padx=35)
lb.bind("<Motion>",spp)
lb.grid(column=0,sticky=E)
splash.mainloop()





   
