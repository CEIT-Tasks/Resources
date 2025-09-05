import tkinter as tk
from tkinter import messagebox

class MessageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа с сообщениями")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.create_buttons()
    
    def create_buttons(self):
        info_button = tk.Button(
            self.root,
            text="Информация",
            command=self.show_info,
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold")
        )
        info_button.pack(pady=10)
        
        warning_button = tk.Button(
            self.root,
            text="Предупреждение",
            command=self.show_warning,
            width=20,
            height=2,
            bg="#FF9800",
            fg="white",
            font=("Arial", 12, "bold")
        )
        warning_button.pack(pady=10)
        
        error_button = tk.Button(
            self.root,
            text="Ошибка",
            command=self.show_error,
            width=20,
            height=2,
            bg="#F44336",
            fg="white",
            font=("Arial", 12, "bold")
        )
        error_button.pack(pady=10)
    
    def show_info(self):
        messagebox.showinfo("Информация", "Это информационное сообщение!\nВсе работает корректно.")
    
    def show_warning(self):
        messagebox.showwarning("Предупреждение", "Внимание! Это предупреждающее сообщение.\nБудьте осторожны!")
    
    def show_error(self):
        messagebox.showerror("Ошибка", "Произошла ошибка!\nПроверьте введенные данные.")

def main():
    root = tk.Tk()
    app = MessageApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()