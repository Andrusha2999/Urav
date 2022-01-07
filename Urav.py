from tkinter import*
import numpy as np
global a,b,c
def lahenda():
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=float(a.get())
        b_=float(a.get())
        c_=float(a.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))*(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Нет корней"
            graf=False
        otvetik.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return graf,D,t

aken=Tk()
aken.title("Решение квадратного уравнения")
aken.geometry("800x300")
reshen=Label(aken,text="Решение квадратного уравнения",font="Arial 20", fg="green",bg="lightblue")
otvetik=Label(aken,text="ответик", height=4,width=60,bg="purple")
a=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=3)
x2=Label(aken,text="x**2+",font="Alial 20", fg="green", padx=10)
b=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=3)
x=Label(aken,text="x+",font="Arial 20", fg="green")
c=Entry(aken,font="Arial 20", fg="green",bg="lightblue",width=3)
ghj=Label(aken,text="=0",font="Arial 20", fg="green")
bnt=Button(aken,text="Решить",font="Arial 20",bg="green",command=lahenda)
bnt.pack(side=LEFT)




reshen.pack()
otvetik.pack(side=BOTTOM)
a.pack(side=LEFT)
x2.pack(side=LEFT)
b.pack(side=LEFT)
x.pack(side=LEFT)
c.pack(side=LEFT)
ghj.pack(side=LEFT)
bnt.pack(side=RIGHT)




aken.mainloop()