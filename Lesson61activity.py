from tkinter import *
from datetime import date

def calculate_age():
    try:
        d = int(day_entry.get())
        m = int(month_entry.get())
        y = int(year_entry.get())
        birth_date = date(y, m, d)
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        result_label.config(text=f"Your age is: {age} years")
    except Exception as e:
        result_label.config(text="Invalid input! Please enter valid numbers.")

# Create window
root = Tk()
root.title("Age Calculator")
root.geometry("300x250")

# Labels and Entries
Label(root, text="Enter your Date of Birth", font=("Arial", 14)).pack(pady=10)

Label(root, text="Day:").pack()
day_entry = Entry(root)
day_entry.pack()

Label(root, text="Month:").pack()
month_entry = Entry(root)
month_entry.pack()

Label(root, text="Year:").pack()
year_entry = Entry(root)
year_entry.pack()

# Button to calculate age
Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

# Label to show result
result_label = Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
