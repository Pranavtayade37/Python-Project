import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("600x200")  # Set window size
root.configure(bg='#0f0f0f')  # Dark background

# Create a label for displaying time
label = tk.Label(root,
                 font=('DS-Digital', 80),  # A digital-style font (see below)
                 background='#0f0f0f',
                 foreground='#39ff14')  # Neon green
label.pack(anchor='center', expand=True)

# Update function
def time():
    string = strftime('%H:%M:%S %p\n%A, %d %B %Y')  # Add full date
    label.config(text=string)
    label.after(1000, time)

time()
root.mainloop()
