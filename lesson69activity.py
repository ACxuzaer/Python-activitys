import tkinter as tk

def check_password_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password", fg="red")
    elif length < 5:
        result_label.config(text="Weak Password", fg="red")
    elif 5 <= length < 8:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

# Create window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("300x200")

# Label for instruction
label = tk.Label(window, text="Enter your password:")
label.pack(pady=5)

# Entry for password
entry = tk.Entry(window, show="*")
entry.pack(pady=5)

# Button to check strength
check_button = tk.Button(window, text="Check Strength", command=check_password_strength)
check_button.pack(pady=5)

# Label to display result
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run the GUI
window.mainloop()
