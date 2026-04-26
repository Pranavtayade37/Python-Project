import tkinter as tk
import math
import time
try:
    from playsound import playsound
    SOUND_ENABLED = True
except:
    SOUND_ENABLED = False

# Global state
theme = "dark"
history_list = []

def play_click_sound():
    if SOUND_ENABLED:
        try:
            playsound("click.mp3", block=False)  # Ensure you have a sound file named click.mp3
        except:
            pass

# Evaluate expressions
def handle_input(text):
    play_click_sound()
    if text == "=":
        try:
            expr = screen.get().replace("π", str(math.pi)).replace("^", "**")
            result = str(eval(expr))
            screen.set(result)
            update_history(expr + " = " + result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    elif text == "√":
        try:
            value = float(screen.get())
            screen.set(str(math.sqrt(value)))
        except:
            screen.set("Error")
    elif text == "x²":
        try:
            value = float(screen.get())
            screen.set(str(value ** 2))
        except:
            screen.set("Error")
    else:
        screen.set(screen.get() + text)

# Hover effect
def on_enter(event):
    event.widget.config(bg=themes[theme]["hover"])

def on_leave(event):
    event.widget.config(bg=themes[theme]["button"])

# Theme switcher
def switch_theme():
    global theme
    theme = "retro" if theme == "dark" else "neon" if theme == "retro" else "dark"
    apply_theme()

def apply_theme():
    root.config(bg=themes[theme]["bg"])
    display.config(bg=themes[theme]["display_bg"], fg=themes[theme]["display_fg"])
    for btn in all_buttons:
        btn.config(bg=themes[theme]["button"], fg=themes[theme]["fg"], activebackground=themes[theme]["active"])
    toggle_btn.config(bg=themes[theme]["button"], fg=themes[theme]["fg"])
    history_box.config(bg=themes[theme]["display_bg"], fg=themes[theme]["display_fg"])

# Add to history
def update_history(entry):
    history_list.append(entry)
    history_box.insert(tk.END, entry)
    history_box.see(tk.END)

# --- THEME SETTINGS ---
themes = {
    "dark": {
        "bg": "#121212",
        "display_bg": "#000000",
        "display_fg": "#39ff14",
        "button": "#2e2e2e",
        "hover": "#33cc33",
        "active": "#444",
        "fg": "white"
    },
    "neon": {
        "bg": "#000000",
        "display_bg": "#000000",
        "display_fg": "#00FFFF",
        "button": "#111",
        "hover": "#00FF00",
        "active": "#003300",
        "fg": "#00FFCC"
    },
    "retro": {
        "bg": "#2a2a2a",
        "display_bg": "#222",
        "display_fg": "#FFD700",
        "button": "#444",
        "hover": "#555",
        "active": "#666",
        "fg": "#FFD700"
    }
}

# --- GUI Setup ---
root = tk.Tk()
root.title("3D Digital Calculator - All Features")
root.geometry("700x620")
root.resizable(False, False)

screen = tk.StringVar()

# Display
display = tk.Entry(root, textvar=screen,
                   font=("DS-Digital", 40),
                   bd=10, relief=tk.FLAT,
                   bg="#000", fg="#39ff14", insertbackground="#39ff14",
                   justify=tk.RIGHT)
display.pack(fill=tk.X, padx=15, pady=15, ipady=10)

# Top frame with toggle
top_frame = tk.Frame(root)
top_frame.pack(padx=15, fill=tk.X)
toggle_btn = tk.Button(top_frame, text="Switch Theme", command=switch_theme,
                       font=("Arial", 12, "bold"), bd=5, relief=tk.RAISED)
toggle_btn.pack(side=tk.RIGHT)

# Frame for calculator and history
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Calculator buttons frame
calc_frame = tk.Frame(main_frame)
calc_frame.pack(side=tk.LEFT, padx=10)

# History list
history_box = tk.Listbox(main_frame, height=20, width=25, font=("Courier", 12))
history_box.pack(side=tk.RIGHT, padx=10, pady=5, fill=tk.Y)

# Buttons
buttons = [
    ["7", "8", "9", "/", "√"],
    ["4", "5", "6", "*", "x²"],
    ["1", "2", "3", "-", "π"],
    ["0", ".", "=", "+", "^"],
    ["C"]
]

all_buttons = []

for row in buttons:
    frame = tk.Frame(calc_frame)
    frame.pack(pady=4)
    for text in row:
        btn = tk.Button(frame, text=text, font=("Arial", 18, "bold"),
                        width=5, height=2, bd=8, relief=tk.RAISED,
                        bg="#2e2e2e", fg="white", activebackground="#444")
        btn.pack(side=tk.LEFT, padx=5)
        btn.bind("<Button-1>", lambda e, t=text: handle_input(t))
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        all_buttons.append(btn)

# Apply theme once at start
apply_theme()

root.mainloop()
