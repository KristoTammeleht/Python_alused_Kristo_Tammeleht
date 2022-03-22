from tkinter import *

#Teeme tehted
def cal_prot():
    a= int(hind.get())
    b= var.get()
    prot= (a*b)/100
    silt3.config(text=prot)
    silt5.config(text=a+prot)
    silt3(0)
    silt5(0)

aken = Tk()
aken.title('Käibemaksekalkulaator')

silt = Label(aken, text="käibemaksuta: ", font='Tahoma 12')
silt.grid(row=0, column=0)
hind = Entry(aken)
hind.grid(row=0,column=1)

silt1 = Label(aken, text="Käibemaksumäär: ", font='Tahoma 12')
silt1.grid(row=1, column=0)

joon = Label(aken, text="*****************************************************************")
joon.grid(row=3, columnspan=3)

silt2 = Label(aken, text="Käibemaks:", font='Tahoma 12' )
silt2.grid(row=4, column=0)

silt3 = Label(aken ,text=cal_prot, font='Tahoma 12')
silt3.grid(row=4, column=1)

silt4 = Label(aken, text="käibemaksuga:", font='Tahoma 12')
silt4.grid(row=5, column=0)

silt5 = Label(aken ,text=cal_prot, font='Tahoma 12')
silt5.grid(row=5, column=1)


def naita_valikut():
    print(var.get())
     
var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9, command=naita_valikut)
valikukast.grid(row=1, column=1)

valikukast = Radiobutton(aken,text="20%", variable=var, value=20, command=naita_valikut)
valikukast.grid(row=2, column=1)

ok = Button(aken, text="OK", command=cal_prot)
ok.grid(row=6, column=1)




aken.mainloop()