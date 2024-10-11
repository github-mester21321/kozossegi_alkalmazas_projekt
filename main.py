#kiegeszitok beimportalasa
from tkinter import*

root = Tk()
root.geometry("400x600")
root.configure(bg='#6a6664')

felhasznalonev = Entry(root).place(relx=0.25, y=20, anchor=CENTER)
jelszo = Entry(root).place(relx=0.75, y=20, anchor=CENTER)


root.mainloop()