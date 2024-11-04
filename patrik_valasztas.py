from tkinter import *
# import patrik_oldala
import patrikgaleria

def valasztasAblak():
    root = Tk()
    root.title("dasokpsaklpoas")
    root.geometry("300x100")
    # root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
        
        
    def patrik_oldal():
        import patrik_oldala
        patrik_oldala.fofuggveny()
    
    def galeria_oldal():
        patrikgaleria.galeria_p()

    
    megnyito_patrik_profil = Button(root, text="Patrik", bg="green", height=2, width=8, command=patrik_oldal).place(relx=0.2, rely=0.5, anchor=CENTER)
    galeria_gomb = Button(root, text="Galéria", bg="green", height=2, width=8, command=galeria_oldal).place(relx=0.5, rely=0.5, anchor=CENTER)
    
    
    root.mainloop()
    
# valasztasAblak()