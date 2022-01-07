from tkinter import*
def lahenda():
    global primer,bukva,c
    if (primer.get()!="" and bukva.get()!="" and c.get()!=""):
        primer_=float(primer.get())
        bukva_=float(bukva.get())
        c_=float(c.get())
        D=bukva_*bukva_-4*primer_*c_
        if D>0:
            x1_=round((-1*bukva_+sqrt(D))/(2*primer_),2)
            x2_=round((-1*bukva_-sqrt(D))/(2*primer_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            flag=True
        elif D==0:
            x1_=round((-1*bukva_)/(2*primer_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="корней нет"
            graf=False
        vastus.configure(text=f"D={D}\n{t}")
        primer.configure(bg="lightblue")
        bukva.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if primer.get()=="":
            primer.configure(bg="red")
        if bukva.get()=="":
            bukva.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return flag,D,t




aken=Tk()
aken.title("Akna nimetus")
aken.geometry("800x200")
nupp=Button(aken,text="решить!",font="Arial 20",fg="red",bg="lightblue",height=2,width=30,relief=GROOVE)
knopka=Button(aken,text="Решения квадратного уравнения!",font="Arial 20",fg="green",bg="lightgreen",height=2,width=30,relief=GROOVE)
lbl=Label(aken,text="...",height=4,width=20,font="Arial 20",fg="green",bg="lightyellow",relief=GROOVE)
primer=Label(aken,text="x**2+",font="Arial 20", fg="green", padx=8)
bukva=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=6)

znak=Label(aken,text="x+",font="Arial 20", fg="green")
c=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=6)
txt=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=6)
kn=Label(aken,text="=0",font="Arial 20", fg="green")





txt.pack(side=LEFT)
primer.pack(side=LEFT)
bukva.pack(side=LEFT)
znak.pack(side=LEFT)
c.pack(side=LEFT)
kn.pack(side=LEFT)
knopka.pack(side=TOP)
lbl.pack(side=BOTTOM)
nupp.pack(side=RIGHT)
aken.mainloop()