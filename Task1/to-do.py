import tkinter as tk
from tkinter import messagebox


def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")


# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the task entry
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create and configure the buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Create and configure the task list
task_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
task_list.pack()

# Start the GUI application
root.mainloop()
