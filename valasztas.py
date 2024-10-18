from tkinter import *
import david_oldala
import patrik_oldala

def valasztasAblak():
    root = Tk()
    root.title("Chat")
    root.geometry("350x300")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
    
    def bezaras():
        root.destroy()
        
        
    def david_oldal():
        david_oldala.fofuggveny()

    def patrik_oldal():
        patrik_oldala.ablak()
    
    # bezaro_gomb = Button(root, text="x", bg="red", height=2, width=3, command=bezaras).place(relx=0.995, rely=0.01, anchor=CENTER)
    megnyito_david_profil = Button(root, text="Dávid", bg="green", height=5, width=10, command=david_oldal).place(relx=0.5, rely=0.2, anchor=CENTER)
    megnyito_patrik_profil = Button(root, text="Patrik", bg="green", height=5, width=10, command=patrik_oldal).place(relx=0.8, rely=0.2, anchor=CENTER)
    
    root.mainloop()
    
valasztasAblak()