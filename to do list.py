import tkinter as tk # importing tkinter
from tkinter import messagebox #importing messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please give task.")

#deleting task
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def clear_tasks():
    listbox.delete(0, tk.END)

#Saving task
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Info", "Tasks saved to tasks.txt")

# Create main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget
entry = tk.Entry(root, font=("Helvetica", 15))
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(root, text="Add items",bg = "green", font=("Helvetica", 12), command=add_task)
add_button.pack()

# Create a listbox to display tasks
listbox = tk.Listbox(root, font=("Helvetica", 15), selectmode=tk.SINGLE)
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

# Create a button to delete selected task
delete_button = tk.Button(root, text="Delete Task", font=("Helvetica", 12), command=delete_task)
delete_button.pack()

# Create a button to clear all tasks
clear_button = tk.Button(root, text="Clear All", font=("Helvetica", 12), command=clear_tasks)
clear_button.pack()

# Create a button to save tasks to a file
save_button = tk.Button(root, text="Save Tasks", font=("Helvetica", 12), command=save_tasks)
save_button.pack()

# Load tasks from a file if present
try:
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for task in tasks:
            listbox.insert(tk.END, task.strip())
except FileNotFoundError:
    pass

# Start the GUI event loop
root.mainloop()