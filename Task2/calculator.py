import tkinter as tk


# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            if num2 == 0:
                result.set("Error")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid Input")


# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter Number 1:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Enter Number 2:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Create operation selection
operation_var = tk.StringVar()
operation_var.set("+")  # Default operation

operation_label = tk.Label(root, text="Select Operation:")
operation_label.grid(row=2, column=0)

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.grid(row=2, column=1)

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2)

# Create result label
result = tk.StringVar()
result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0)

result_display = tk.Label(root, textvariable=result)
result_display.grid(row=4, column=1)

# Start the GUI application
root.mainloop()
