import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import sqlite3

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Библиотека книг")
        self.root.geometry("800x600")
        
        self.init_db()
        self.create_menu()
        self.create_widgets()
        
    def init_db(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books 
                              (id INTEGER PRIMARY KEY, title TEXT, author TEXT, 
                               genre TEXT, available INTEGER, year INTEGER)''')
        self.conn.commit()
        
    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Файл", menu=file_menu)
        file_menu.add_command(label="Сохранить", command=self.save_data)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.root.quit)
        
    def create_widgets(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True,  padx=10, pady=10)
        
        input_frame = ttk.LabelFrame(main_frame, text="Добавить книгу", padding=10)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(input_frame, text="Название:").grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(input_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(input_frame, text="Автор:").grid(row=0, column=2, sticky="w", padx=(20, 0))
        self.author_entry = tk.Entry(input_frame, width=25)
        self.author_entry.grid(row=0, column=3, padx=5)
        
        tk.Label(input_frame, text="Жанр:").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.genre_var = tk.StringVar(value="Фантастика")
        genres = ["Фантастика", "Детектив", "Роман", "Поэзия"]
        for i, genre in enumerate(genres):
            tk.Radiobutton(input_frame, text=genre, variable=self.genre_var, 
                          value=genre).grid(row=1, column=i+1, sticky="w", padx=5, pady=(10, 0))
        
        tk.Label(input_frame, text="Год:").grid(row=2, column=0, sticky="w", pady=(10, 0))
        self.year_entry = tk.Entry(input_frame, width=10)
        self.year_entry.grid(row=2, column=1, sticky="w", pady=(10, 0))
        
        self.available_var = tk.BooleanVar(value=True)
        tk.Checkbutton(input_frame, text="В наличии", variable=self.available_var).grid(row=2, column=2, pady=(10, 0))
        
        tk.Button(input_frame, text="Добавить", command=self.add_book, 
                 bg="#4CAF50", fg="white", width=15).grid(row=2, column=3, pady=(10, 0))
        
        filter_frame = tk.Frame(main_frame)
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.filter_label = tk.Label(filter_frame, text="Фильтр по жанру:")
        self.filter_label.place(x=0, y=5)
        
        self.filter_var = tk.StringVar(value="Все")
        self.filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, 
                                        values=["Все", "Фантастика", "Детектив", "Роман", "Поэзия"],
                                        width=15, state="readonly")
        self.filter_combo.place(x=120, y=5)
        self.filter_combo.bind("<<ComboboxSelected>>", self.filter_books)
        
        self.available_filter = tk.BooleanVar(value=False)
        tk.Checkbutton(filter_frame, text="Только в наличии", 
                      variable=self.available_filter, command=self.filter_books).place(x=300, y=5)
        
        display_frame = ttk.LabelFrame(main_frame, text="Список книг", padding=10)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        self.text_display = scrolledtext.ScrolledText(display_frame, wrap=tk.WORD, 
                                                     font=("Consolas", 10))
        self.text_display.pack(fill=tk.BOTH, expand=True)
        
        button_frame = tk.Frame(display_frame)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        tk.Button(button_frame, text="Обновить список", command=self.refresh_display,
                 bg="#2196F3", fg="white").pack(side=tk.LEFT)
        tk.Button(button_frame, text="Очистить", command=self.clear_display,
                 bg="#FF5722", fg="white").pack(side=tk.LEFT, padx=(10, 0))
        
        self.refresh_display()
        
    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()
        
        if not title or not author:
            messagebox.showwarning("Предупреждение", "Заполните название и автора!")
            return
            
        try:
            year = int(year) if year else 0
        except ValueError:
            messagebox.showerror("Ошибка", "Год должен быть числом!")
            return
            
        self.cursor.execute("INSERT INTO books (title, author, genre, available, year) VALUES (?, ?, ?, ?, ?)",
                           (title, author, self.genre_var.get(), int(self.available_var.get()), year))
        self.conn.commit()
        
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.available_var.set(True)
        
        self.refresh_display()
        messagebox.showinfo("Успех", "Книга добавлена!")
        
    def filter_books(self, event=None):
        self.refresh_display()
        
    def refresh_display(self):
        self.text_display.delete(1.0, tk.END)
        
        query = "SELECT * FROM books WHERE 1=1"
        params = []
        
        if self.filter_var.get() != "Все":
            query += " AND genre = ?"
            params.append(self.filter_var.get())
            
        if self.available_filter.get():
            query += " AND available = 1"
            
        query += " ORDER BY title"
        
        self.cursor.execute(query, params)
        books = self.cursor.fetchall()
        
        if not books:
            self.text_display.insert(tk.END, "Книги не найдены.")
            return
            
        header = f"{'ID':<5} {'Название':<30} {'Автор':<20} {'Жанр':<15} {'Год':<6} {'В наличии':<10}\n"
        self.text_display.insert(tk.END, header)
        self.text_display.insert(tk.END, "-" * 90 + "\n")
        
        for book in books:
            available = "Да" if book[4] else "Нет"
            line = f"{book[0]:<5} {book[1]:<30} {book[2]:<20} {book[3]:<15} {book[5]:<6} {available:<10}\n"
            self.text_display.insert(tk.END, line)
            
    def clear_display(self):
        self.text_display.delete(1.0, tk.END)
        
    def save_data(self):
        self.conn.commit()
        messagebox.showinfo("Сохранение", "Данные сохранены!")
        
    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

root = tk.Tk()
app = LibraryApp(root)
root.mainloop()