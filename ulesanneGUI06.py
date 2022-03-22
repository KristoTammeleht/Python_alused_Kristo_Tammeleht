from tkinter import *
aken = Tk()
aken.title('den')

louend = Canvas(aken, width=500, height=500)
louend.pack()





louend.create_rectangle(500, 500, 0, 0, fill='#DC143C', outline='#DC143C')
louend.create_rectangle(100,0, 150, 600, fill='#FFFFFF', outline='#FFFFFF')
louend.create_rectangle(0,130, 500, 180, fill='#FFFFFF', outline='#FFFFFF')

minu_pilt = PhotoImage(file='taani.png')
louend.create_image(150, 150, anchor=NW, image=minu_pilt)
louend.create_text(150,50, text="Hello denmark!", fill="black", font=("Tahoma", 30))
aken.mainloop()