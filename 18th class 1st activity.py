from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Image
upload = Image.open("https://www.bing.com/images/search?view=detailV2&ccid=kM3KLr0h&id=9F1B0A598AB141795EB12DED301585ED6AD70356&thid=OIP.kM3KLr0hMvDLmgdHT2COIwHaEo&mediaurl=https%3a%2f%2fwallpaperaccess.com%2ffull%2f398864.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.90cdca2ebd2132f0cb9a07474f608e23%3frik%3dVgPXau2FFTDtLQ%26pid%3dImgRaw%26r%3d0&exph=2400&expw=3840&q=sky+images&mode=overlay&FORM=IQFRBA&ck=F9CA14EADBF4D021BDBAC40F51522346&selectedIndex=0&idpp=serp&adlt=strict")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)


def msg():
    MsgBox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()


def topwin():
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    # Input
    label = Label(top, text="Enter Amount:", bg='grey')
    label.place(x=200, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    # Button
    btn = Button(top, text="Calculate")
    btn.place(x=240, y=120)

    # Output labels
    l1 = Label(top, text="2000 Notes:", bg='grey')
    l1.place(x=180, y=200)

    l2 = Label(top, text="500 Notes:", bg='grey')
    l2.place(x=180, y=230)

    l3 = Label(top, text="100 Notes:", bg='grey')
    l3.place(x=180, y=260)

    # Result fields
    t1 = Entry(top)
    t1.place(x=270, y=200)

    t2 = Entry(top)
    t2.place(x=270, y=230)

    t3 = Entry(top)
    t3.place(x=270, y=260)


# Button
button1 = Button(root,
                 text="Lets get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

root.mainloop()