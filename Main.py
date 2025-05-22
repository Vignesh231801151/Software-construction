# Main.py
import customtkinter as ctk
import BackEnd as backend
from FrontEnd import HospitalUI
import tkinter as tk

if __name__ == "__main__":
    backend.connect()

    root = ctk.CTk()

    # Set window size to 75% of screen and center it
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    win_width = int(screen_width * 0.75)
    win_height = int(screen_height * 0.75)
    x = (screen_width - win_width) // 2
    y = (screen_height - win_height) // 2

    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.title("Hospital Management System")

    app = HospitalUI(root, backend)
    root.mainloop()
