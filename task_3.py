import tkinter as tk
import re

def check_password_strength():
    password = entry_password.get()
    if len(password) < 8:
        label_result.config(text="Password must contain at least 8 characters.\nYour password is weak.")
    elif not re.search("[A-Z]", password):        
        label_result.config(text="Your Password must contain at least one uppercase character.\nYour password is too weak.")
    elif not re.search("[a-z]", password):
        label_result.config(text="Password must contain at least one lowercase character.\nYour password is weak.")
    elif not re.search("[0-9]", password):
        label_result.config(text="Password must contain at least one digit character.\nYour password is weak.")
    elif not re.search("[!@^&~:><.,]", password):
        label_result.config(text="Your password is medium.\nYou can add a special character to make it strong.")
    else:
        label_result.config(text="Your Password is strong.")

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Password Strength Checker")

# Create GUI elements
label_instructions = tk.Label(root, text="Enter your password:")
label_instructions.pack(pady=10)

entry_password = tk.Entry(root)                 #You can use show="*" to show password in *
entry_password.pack(pady=5)

button_check = tk.Button(root, text="Check Password", command=check_password_strength)
button_check.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the main tkinter event loop
root.mainloop()
