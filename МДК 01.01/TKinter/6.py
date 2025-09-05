import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Пользователь")
root.geometry("300x200")

label = tk.Label(root, text="Имя и фамилия пользователя", font=("Arial", 12))
label.pack(pady=10)

frame = ttk.LabelFrame(root, text="Данные пользователя", padding=10)
frame.pack(pady=10, padx=20, fill="x")

tk.Label(frame, text="Имя:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(frame, width=20)
name_entry.grid(row=0, column=1, pady=5, padx=(10, 0))

tk.Label(frame, text="Фамилия:").grid(row=1, column=0, sticky="w", pady=5)
surname_entry = tk.Entry(frame, width=20)
surname_entry.grid(row=1, column=1, pady=5, padx=(10, 0))

root.mainloop()