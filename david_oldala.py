from tkinter import *

root = Tk()
root.title("Dávid oldali chat")
root.geometry("500x500")
root.configure(bg="#257180")

szovegmezo = Entry(root, borderwidth=2)
szovegmezo.place(relx=0.5, rely=0.1, anchor=CENTER)

def fofuggveny():
    szoveg = str(szovegmezo.get())
    if szoveg != "":    
        with open('./messages.txt', 'a', encoding='utf-8') as irogatas:
            print(80, szoveg, sep=";", file=irogatas)

    
    
    with open('./messages.txt', 'r', encoding='utf-8') as uzenetek:
        if len(uzenetek.readlines()) == 0:
            print("Még nem érkezett üzenete.")
        else:
            for i in uzenetek:
                i.strip()
                i = i.split(';')
                i = [int(i[0]), str(i[1])]
                #patrik=420, david=80
                


    

    root.mainloop()


bekero_gomb = Button(root, text="Küldés", font="Rubik 10 bold", command=fofuggveny).place(relx=0.5, rely=0.8, anchor=CENTER)

fofuggveny()