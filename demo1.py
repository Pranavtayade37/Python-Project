import tkinter as tk
from tkinter import messagebox
import json
import os

# File to save tasks
TASKS_FILE = "tasks.json"

# === Main window ===
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x500")
root.configure(bg="#f7f7f7")

# === Task List Display ===
task_listbox = tk.Listbox(root, font=("Arial", 14), height=15, selectbackground="skyblue")
task_listbox.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# === Scrollbar for Listbox ===
scrollbar = tk.Scrollbar(task_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# === Task Entry Field ===
entry_frame = tk.Frame(root, bg="#f7f7f7")
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, font=("Arial", 14), width=22)
task_entry.pack(side=tk.LEFT, padx=10)

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

# === Buttons ===
btn_frame = tk.Frame(root, bg="#f7f7f7")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", font=("Arial", 12), command=add_task, bg="#28a745", fg="white")
add_btn.grid(row=0, column=0, padx=10)

delete_btn = tk.Button(btn_frame, text="Delete Task", font=("Arial", 12), command=delete_task, bg="#dc3545", fg="white")
delete_btn.grid(row=0, column=1, padx=10)

# === Load and Save Tasks ===
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        json.dump(list(tasks), file)

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                tasks = json.load(file)
                for task in tasks:
                    task_listbox.insert(tk.END, task)
            except json.JSONDecodeError:
                pass

# === Start App ===
load_tasks()
root.mainloop()

