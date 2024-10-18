# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# import valasztas

# def galeria_ablak():
#     root = Tk()
#     root.title("döntés")
#     root.geometry("400x350")
#     # root.configure(bg='#6a6664')
    
 
 
#     # Read the Image
#     image = Image.open("bmw.jpg")
 
#     # Resize the image using resize() method
#     resize_image = image.resize((300, 180))
 
#     img = ImageTk.PhotoImage(resize_image)
    
#     # create label and add resize image
#     kepLabel = Label(image=img)
#     kepLabel.image = img
#     kepLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
 
 
#     def chatMegnyitas():
#         valasztas.foChat()
#         # root.destroy()
        
    
#     chat_gomb = Button(root, text="CHAT", command=chatMegnyitas, font='Rubik 10 bold').place(relx=0.5, rely=0.1, anchor=CENTER)


#     root.mainloop()
    
# galeria_ablak()





import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Display Image in Tk")
root.geometry("400x300")
# Load image from disk.
image = tk.PhotoImage(file="patrik.png")
# Display it within a label.
label = ttk.Label(image=image)
label.pack()
root.mainloop()