from tkinter import *

#Akna seadistamine
aken =Tk()
aken.title('Tervitus')
aken.configure(background='black')


#Teksti lisamine
Label(aken ,text='Nimi: Kristo Tammeleht',foreground='red',background='black', font='Tahoma 16 bold italic',pady=10, padx=30).pack()
Label(aken ,text='Rühm: IT21',foreground='red',background='black', font='Tahoma 16 bold italic',pady=10, padx=30).pack()
Label(aken ,text='2021',foreground='red',background='black', font='Tahoma 16 bold italic',pady=10, padx=30).pack()