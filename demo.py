import tkinter as tk
from tkinter import messagebox
from time import strftime
import threading
import datetime

# Main window
root = tk.Tk()
root.title("Digital Clock with Alarm")
root.geometry("600x300")
root.configure(bg='#1c1c1c')

# Digital clock label
clock_label = tk.Label(root,
                       font=('Courier', 50, 'bold'),
                       background='#1c1c1c',
                       foreground='#00FF00')
clock_label.pack(pady=20)

# Alarm input
alarm_frame = tk.Frame(root, bg='#1c1c1c')
alarm_frame.pack(pady=10)

tk.Label(alarm_frame, text="Set Alarm (HH:MM:SS AM/PM):",
         font=('Arial', 14), bg='#1c1c1c', fg='white').pack(side='left', padx=10)

alarm_time_entry = tk.Entry(alarm_frame, font=('Arial', 14))
alarm_time_entry.pack(side='left')

# Global alarm time variable
alarm_time = None

# Clock updater
def update_time():
    current_time = strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    if alarm_time == current_time:
        messagebox.showinfo("Alarm", "Time's up!")
    clock_label.after(1000, update_time)

# Alarm setter
def set_alarm():
    global alarm_time
    user_input = alarm_time_entry.get()
    try:
        # Validate format
        datetime.datetime.strptime(user_input, "%I:%M:%S %p")
        alarm_time = user_input
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
    except ValueError:
        messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS AM/PM format")

# Button to set alarm
set_btn = tk.Button(root, text="Set Alarm", font=('Arial', 14), command=set_alarm, bg='#00aa00', fg='white')
set_btn.pack(pady=10)

# Start clock
update_time()
root.mainloop()
