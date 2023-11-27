import tkinter as tk
from tkinter import Scrollbar, Listbox


def add_task(task_list, new_task):
        task_list.insert("end", new_task)
        entry_task.delete(0, tk.END)

def delete_task(task_list):
    selected_index = task_list.curselection()
    if selected_index:
        task_list.delete(selected_index)

def clear_all_tasks(task_list):
    task_list.delete(0, "end")

def save_tasks(task_list, filename="tasks.txt"):
    tasks = task_list.get(0, "end")
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks(task_list, filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_list.insert("end", task.strip())
    except FileNotFoundError:
        pass
def exit():
    root.destroy()

def main():
    global entry_task,root
    root = tk.Tk()
    root.title("To-Do List App")

    task_list = Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
    task_list.grid(row=0, column=0, padx=10, pady=10)

    scrollbar = Scrollbar(root)
    scrollbar.grid(row=0, column=1, sticky=tk.NS)

    task_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_list.yview)

    entry_task = tk.Entry(root, width=30)
    entry_task.grid(row=1, column=0, padx=10, pady=5)
    entry_task.insert(0, "Enter Task")

    #buttons
    add_button = tk.Button(root, text="Add Task", command=lambda: add_task(task_list, entry_task.get()))
    add_button.grid(row=1, column=1, padx=5, pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=lambda: delete_task(task_list))
    delete_button.grid(row=2, column=0, padx=5, pady=5)

    clear_button = tk.Button(root, text="Clear All Tasks", command=lambda: clear_all_tasks(task_list))
    clear_button.grid(row=2, column=1, padx=5, pady=5)

    save_button = tk.Button(root, text="Save Tasks", command=lambda: save_tasks(task_list))
    save_button.grid(row=3, column=0, padx=5, pady=5)

    load_button = tk.Button(root, text="Load Tasks", command=lambda: load_tasks(task_list))
    load_button.grid(row=3, column=1, padx=5, pady=5)

    exit_button = tk.Button(root, text="Exit", command=lambda: exit())
    exit_button.grid(row=5, column=1, padx=5, pady=5)
    
    #startup load
    load_tasks(task_list)

    root.mainloop()
   
main()
