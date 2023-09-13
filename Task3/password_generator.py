import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showwarning(
                "Invalid Input", "Please enter a valid password length greater than 0."
            )
        else:
            characters = string.ascii_letters + string.digits + string.punctuation
            password = "".join(random.choice(characters) for _ in range(length))
            result.set(password)
    except ValueError:
        messagebox.showwarning(
            "Invalid Input", "Please enter a valid number for password length."
        )


# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create input fields and labels
label_length = tk.Label(root, text="Password Length:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label to display the generated password
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

# Start the GUI application
root.mainloop()
