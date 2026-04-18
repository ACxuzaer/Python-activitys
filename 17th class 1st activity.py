from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")
root.geometry("400x400")

# Give your real image file name here
upload = Image.open("image.png")   

# Resize image if needed
upload = upload.resize((300, 350))

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image)
label.place(x=50, y=0)

label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)

root.mainloop()