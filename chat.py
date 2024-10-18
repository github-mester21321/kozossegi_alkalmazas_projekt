from tkinter import *

def chatFolyamat():
    root = Tk()
    root.title("Chat")
    root.attributes('-fullscreen', True)
    root.configure(bg='#6a6664')
    
    
    
    
    
    
    
    
    #bezaras
    def bezaras():
        root.destroy()
    bezaro_gomb2 = Button(root, text="x", bg="red", command=bezaras).place(relx=0.995, rely=0.01, anchor=CENTER)
    #----------
    
    root.mainloop()