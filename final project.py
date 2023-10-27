import tkinter as tk
from tkinter import messagebox

# Function to add a task and apply a simple animation
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, "✅ " + task)  # Added a checkmark emoji
        task_entry.delete(0, tk.END)
        animate(task_list, "green")

# Function to remove a task and apply a simple animation
def remove_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        task_list.delete(tk.ACTIVE)
        animate(task_list, "red")
    except:
        pass

# Function for a simple color animation
def animate(widget, color):
    widget.configure(bg=color)
    window.after(100, lambda: widget.configure(bg="white"))

def show_list():
    tasks = task_list.get(0, tk.END)
    if not tasks:
        messagebox.showinfo("To-Do List", "Your to-do list is empty.")
    else:
        task_list_text = "\n".join(tasks)
        messagebox.showinfo("To-Do List", task_list_text)

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create a task entry field with an emoji
task_entry = tk.Entry(window, width=40)
task_entry.insert(tk.END, "✏️ Enter a task")
task_entry.pack()

# Create an "Add" button to add tasks
add_button = tk.Button(window, text="Add", command=add_task)
add_button.pack()

# Create a list to display tasks
task_list = tk.Listbox(window, selectmode=tk.SINGLE, width=40, height=10)
task_list.pack()

# Create a "Remove" button to remove selected tasks
remove_button = tk.Button(window, text="Remove", command=remove_task)
remove_button.pack()

# Create a "Show List" button to display the entire task list
show_list_button = tk.Button(window, text="Show List", command=show_list)
show_list_button.pack()

window.mainloop()
