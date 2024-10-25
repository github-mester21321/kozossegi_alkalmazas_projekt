from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 
import time

root = Tk()
root.title("Dávid oldali chat")
root.geometry("550x500")
root.resizable(width=False, height=False)
root.configure(bg="#257180")

scroll = tk.Scrollbar(root) 
text = tk.Text(root, height=15, width=65) 
text.configure(yscrollcommand=scroll.set, padx=5) 
text.place(relx=0.5, rely=0.26, anchor=CENTER)


#szovegbeolvasas1 ------------------------------------------------
textbox = tk.Text(root, height=4, width=30)
scroll = tk.Scrollbar(root) 
textbox.configure(yscrollcommand=scroll.set, borderwidth=2, relief="solid", padx=5) 
textbox.place(relx=0.3, rely=0.7, anchor=CENTER)
#------------------------------------------------------------------


def fofuggveny():
    text.delete("1.0", END)
    #szovegbeolvasas1 ------------------------------------------------
    asd = textbox.get(1.0, "end-1c")
    if asd != "":    
        with open('./messages.txt', 'a', encoding='utf-8') as irogatas:
            print(420, asd, sep=";", file=irogatas)
    #------------------------------------------------------------------

    with open('./messages.txt', 'r', encoding='utf-8') as uzenetek:
        for i in uzenetek:
            i = i.split(';')
            x = i[1].replace("\n", "")          
            i = [int(i[0]), str(x)]
            # print(i)
            if i[0] == 420:
                text.insert(tk.END, i[1] + "\n", "patrik")
                text.tag_config("patrik", foreground="white", background="darkgreen", font="rubik 12 bold", justify="right", borderwidth=1, relief="solid")
                text.yview(END)
            elif i[0] == 80:
                text.insert(tk.END, i[1] + "\n", "david")
                text.tag_config("david", foreground="white", background="red", font="rubik 12 bold", justify="left", borderwidth=1, relief="solid")
                text.yview(END)
    
    bekero_gomb = Button(root, text="Küldés", font="Rubik 10 bold", command=fofuggveny).place(relx=0.75, rely=0.7, anchor=CENTER)
    
    root.mainloop()
    
fofuggveny()