#szukseges modulok beimportalasa
from tkinter import *
import belepes
import regisztracio
import tkinter.font as tkFont
from tkinter import PhotoImage


root = Tk() #a fo oldal letrehozasa
root.geometry("450x400")    #az oldal meretenek beallitasa
root.resizable(False, False)    #az oldal atmeretezhetosegenek letiltasa
root.title("ECHO fő oldal") #az oldal cimenek beallitasa


bg = PhotoImage(file='./kepek/fold.gif')
my_canvas = Canvas(root, width=450, height=400)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_text(225, 54, text="ECHO", font="Monaco 60 bold", fill="white")


def belepesFg():    #a belepes oldalt megnyito fuggveny letrehozasa
    belepes.belepesAblak()  #a belepes oldal megnyitasa
    
def regisztracioFg():   #a regisztracios oldalt megnyito fuggveny letrehozasa
    regisztracio.regisztaciosAblak()    #a regisztracios oldal megnyitasa


#a belepes oldalt megnyito gomb letrehozasa es elhelyezese
belepes_gomb = Button(root, text="Belépés", command=belepesFg, fg='black', bg='#FD8B51', font='Times 10 bold', bd=2)
belepes_gomb.place(relx=0.25, rely=0.5, anchor=CENTER)

#a regisztracios oldalt megnyito gomb letrehozasa es elhelyezese
regisztracio_gomb = Button(root, text="Regisztáció", command=regisztracioFg, fg='black', bg='#FD8B51', font='Times 10 bold', bd=2)
regisztracio_gomb.place(relx=0.75, rely=0.5, anchor=CENTER)


#a program folyamatos futasat vegzo fuggveny meghivas
root.mainloop()