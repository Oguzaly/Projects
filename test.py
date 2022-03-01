import tkinter as tk
import PyPDF2
from PIL import Image,ImageTk

root=tk.Tk() # Window object

canvas = tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)  #this attribute is going to split 3 identicly secret cloumn

#logo

logo= Image.open('logo.png') # kullanacağımız logoyu belittik
logo= ImageTk.PhotoImage(logo) #logoyu tkinder da kullanacağımız bir widget yaptık
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

#instructions

instructions = tk.Label(root, text="select a pdf file on your computer to extract all its text", font="Raleway")
instructions.grid( columnspan=3, column=0, row=1)

#browser Button

browse_text =tk.StringVar()
browse_btn =tk.Button(root,textvariable =browse_text, font='Raleway',bg='#20bebe',fg='white',height=2,width =15 ) # background clour için bg kullandık,font clour için fg kullndık
browse_text.set('Browse')
browse_btn.grid(column=1,row=2)

canvas = tk.Canvas(root,width=600,heigh=250)  # bu iki satır sadece kolay yoldan browse buttonın altındaki alanı arttırmak için kullanıldı.
canvas.grid(columnspan=3)

root.mainloop()   # all the elements that we will add is inside that two code
