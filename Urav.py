from tkinter import*






aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x200")
nupp=Button(aken,text="уравнения!",font="Arial 20",fg="red",bg="lightblue",height=2,width=30,relief=GROOVE)
knopka=Button(aken,text="Решения!",font="Arial 20",fg="green",bg="lightgreen",height=2,width=30,relief=GROOVE)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightyellow",relief=GROOVE)
txt=Entry(aken,width=5,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt1=Entry(aken,width=5,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)
txt2=Entry(aken,width=5,font="Arial 20",fg="green",bg="lightblue",justify=CENTER)


knopka.pack()
txt1.pack(side=LEFT)
txt2.pack()
txt.pack()
lbl.pack()
nupp.pack(side=RIGHT)
aken.mainloop()