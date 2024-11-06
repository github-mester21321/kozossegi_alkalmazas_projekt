from tkinter import *
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 

root = Toplevel()
root.title("Patrik oldala")
root.geometry("550x500")
root.resizable(width=False, height=False)
root.configure(bg="#257180")

scroll = tk.Scrollbar(root) 
text = tk.Text(root, height=15, width=65) 
text.configure(yscrollcommand=scroll.set, padx=5) 
text.place(relx=0.5, rely=0.26, anchor=CENTER)


textbox = tk.Text(root, height=4, width=30)
scroll = tk.Scrollbar(root) 
textbox.configure(yscrollcommand=scroll.set, borderwidth=2, relief="solid", padx=5) 
textbox.place(relx=0.3, rely=0.7, anchor=CENTER)


def fofuggveny():
    text.delete("1.0", END)
    patrik = textbox.get(1.0, "end-1c")
    if patrik != "":    
        with open('./fajlba_iras/messages.txt', 'a', encoding='utf-8') as irogatas:
            print("patrik", patrik, sep=";", file=irogatas)

    with open('./fajlba_iras/messages.txt', 'r', encoding='utf-8') as uzenetek:
        for i in uzenetek:
            i = i.split(';')
            x = i[1].replace("\n", "")          
            i = [str(i[0]), str(x)]
            if i[0] == "patrik":
                text.insert(tk.END, i[1] + "\n", "patrik")
                text.tag_config("patrik", foreground="white", background="darkgreen", font="rubik 12 bold", justify="right", borderwidth=1, relief="solid")
                text.yview(END)
            else:
                text.insert(tk.END, f"{i[0]}: {i[1]}" + "\n", "mas")
                text.tag_config("mas", foreground="white", background="red", font="rubik 12 bold", justify="left", borderwidth=1, relief="solid")
                text.yview(END)
        
    bekero_gomb = Button(root, text="Küldés", font="Rubik 10 bold", command=fofuggveny).place(relx=0.75, rely=0.7, anchor=CENTER)
        
    root.mainloop()
        
# fofuggveny()    