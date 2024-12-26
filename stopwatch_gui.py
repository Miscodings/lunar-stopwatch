import tkinter as tk
from tkinter import font, colorchooser
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Lunar Stopwatch")
        self.root.config(bg="#141414")
        self.root.geometry("400x600")

        self.start_time = None
        self.running = False
        self.elapsed_time = 0

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  # Time label row
        self.root.rowconfigure(1, weight=1)  # Buttons row

        self.time_label = tk.Label(
            root, 
            text="00:00:00", 
            font=("Eczar", 48), 
            fg="#f1ec55", 
            bg="#141414"
        )
        self.time_label.grid(row=0, column=0, pady=20, sticky="n")

        button_frame = tk.Frame(root, bg="#141414")
        button_frame.grid(row=1, column=0, pady=10)

        self.start_button = tk.Button(
            button_frame, 
            text="Start", 
            command=self.start, 
            font=("Eczar", 14), 
            fg="#ffffff", 
            bg="#333333", 
            activebackground="#787878", 
            relief="flat"
        )
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(
            button_frame, 
            text="Stop", 
            command=self.stop, 
            font=("Eczar", 14), 
            fg="#ffffff", 
            bg="#333333", 
            activebackground="#787878", 
            relief="flat"
        )
        self.stop_button.grid(row=0, column=1, padx=10)

        self.reset_button = tk.Button(
            button_frame, 
            text="Reset", 
            command=self.reset, 
            font=("Eczar", 14), 
            fg="#ffffff", 
            bg="#333333", 
            activebackground="#787878", 
            relief="flat"
        )
        self.reset_button.grid(row=0, column=2, padx=10)

        self.settings_button = tk.Button(
            button_frame, 
            text="Settings", 
            command=self.open_settings, 
            font=("Eczar", 14), 
            fg="#ffffff", 
            bg="#333333", 
            activebackground="#787878", 
            relief="flat"
        )
        self.settings_button.grid(row=0, column=3, padx=10)

        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)
        button_frame.columnconfigure(3, weight=1)

    def format_time(self):
        hours = int(self.elapsed_time // 3600)
        minutes = int((self.elapsed_time % 3600) // 60)
        seconds = int(self.elapsed_time % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.time_label.config(text=self.format_time())
            self.root.after(100, self.update_time)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self.update_time()

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False

    def reset(self):
        self.elapsed_time = 0
        self.running = False
        self.time_label.config(text="00:00:00")

    def open_settings(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Lunar Stopwatch Settings")
        settings_window.geometry("300x200")
        settings_window.config(bg="#141414")

        # Font settings
        tk.Label(settings_window, text="Font:", fg="#f1ec55", bg="#222222", font=("Eczar", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        font_var = tk.StringVar(value=self.time_label.cget("font").split()[0])
        font_dropdown = tk.OptionMenu(settings_window, font_var, "Eczar", "Arial", "Courier", "Times New Roman", "Comic Sans MS")
        font_dropdown.config(bg="#333333", fg="#ffffff", font=("Eczar", 12))
        font_dropdown["menu"].config(bg="#333333", fg="#ffffff")
        font_dropdown.grid(row=0, column=1, padx=10, pady=5)

        # Font size settings
        tk.Label(settings_window, text="Size:", fg="#f1ec55", bg="#222222", font=("Eczar", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        size_var = tk.IntVar(value=int(self.time_label.cget("font").split()[1]))
        size_entry = tk.Entry(settings_window, textvariable=size_var, bg="#333333", fg="#ffffff", font=("Eczar", 12), width=5)
        size_entry.grid(row=1, column=1, padx=10, pady=5)

        # Color settings
        tk.Label(settings_window, text="Color:", fg="#f1ec55", bg="#222222", font=("Eczar", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
        color_var = tk.StringVar(value=self.time_label.cget("fg"))
        color_entry = tk.Entry(settings_window, textvariable=color_var, bg="#333333", fg="#ffffff", font=("Eczar", 12))
        color_entry.grid(row=2, column=1, padx=10, pady=5)

        # Color settings
        tk.Label(settings_window, text="Color:", fg="#ffffff", bg="#141414").pack(pady=5)
        color_button = tk.Button(
            settings_window, 
            text="Choose Color", 
            command=lambda: self.choose_color(color_button), 
            bg=self.timer_color, 
            fg="#ffffff"
        )
        color_button.pack()

        # Apply Button
        def apply_changes():
            new_font = font_var.get()
            new_size = size_var.get()
            new_color = color_var.get()
            self.time_label.config(font=(new_font, new_size), fg=new_color)

        apply_button = tk.Button(
            settings_window, 
            text="Apply", 
            command=apply_changes, 
            bg="#444444", 
            fg="#ffffff", 
            font=("Eczar", 12), 
            relief="flat"
        )
        apply_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Configure rows/columns for layout
        settings_window.grid_columnconfigure(0, weight=1)
        settings_window.grid_columnconfigure(1, weight=2)


# Create the application window
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
