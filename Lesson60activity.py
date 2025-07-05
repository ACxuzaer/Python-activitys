# Import necessary libraries
from tkinter import *
from datetime import date  # You had a typo here: "form" instead of "from"

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)

# Add Label for getting name as input from the user
name_lbl = Label(text="Full Name", bg="#3895D3")
# Use Entry Widget to create a text box for user to enter details
name_entry = Entry()

# Function to display a message
def display():
    # Read input given by user
    name = name_entry.get()

    # Declaring a message
    message = "Welcome to the Application! \nToday's date is: "
    greet = "Hello " + name + "\n"

    # Clear text box first (optional, so previous messages don't stack)
    text_box.delete("1.0", END)

    # Display details in a text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, str(date.today()))

# Add a text widget to display information/messages
text_box = Text(height=5)

# Add button and give value of command as name of the function
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')  # You had 'fr' instead of 'fg'

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the event loop
root.mainloop()
