from tkinter import*
from math import*
import matplotlib.pyplot as plt 
import numpy as np
global a,b,c
def lahenda():    
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Корней нет"
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
def graafik():
    flag,D,t=lahenda()
    if flag==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    otvetik.configure(text=f"D={D}\n{t}\n{text}")









aken=Tk()
aken.title("Решение Уравнения")
aken.geometry("750x280")
reshen=Label(aken,text="Решение_Квадратного_Уравнения",font="Arial 20", fg="black",bg="lightyellow")
otvetik=Label(aken,text="ответик", height=4,width=60,bg="purple")
a=Entry(aken,font="Arial 25",bg="lightblue",    fg="green",width=4)
x2=Label(aken,text="x**2+",  font="Arial 25",   fg="green", padx=12)
b=Entry(aken,font="Arial 25",bg="lightblue",    fg="green",width=4)
x=Label(aken,text="x+",      font="Arial 25",   fg="green")
c=Entry(aken,font="Arial 25",bg="lightblue",    fg="green",width=5)
piip=Label(aken,text="=0",   font="Arial 25",    fg="green")
knopka=Button(aken,text="РЕШИТЬ",font="Arial 25",  bg="pink",command=lahenda)
grafik_=Button(aken,text="График", font="Arial 25",bg="green",command=graafik)





reshen.pack()
otvetik.pack(side=BOTTOM)
a.pack(side=LEFT)
x2.pack(side=LEFT)
b.pack(side=LEFT)
x.pack(side=LEFT)
c.pack(side=LEFT)
piip.pack(side=LEFT)
knopka.pack(side=RIGHT)
grafik_.pack(side=LEFT)




aken.mainloop()