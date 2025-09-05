import tkinter as tk
from tkinter import ttk

class RainbowColorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Цвета радуги")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        
        self.colors = {
            "Красный": "#ff0000",
            "Оранжевый": "#ff7d00", 
            "Желтый": "#ffff00",
            "Зеленый": "#00ff00",
            "Голубой": "#007dff",
            "Синий": "#0000ff",
            "Фиолетовый": "#7d00ff"
        }
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        title_label = ttk.Label(main_frame, text="Выберите цвет радуги:", font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        for i, (color_name, color_code) in enumerate(self.colors.items()):
            btn = tk.Button(
                buttons_frame,
                text=color_name,
                bg=color_code,
                fg="white" if color_name in ["Красный", "Синий", "Фиолетовый"] else "black",
                font=("Arial", 10, "bold"),
                width=12,
                height=2,
                command=lambda name=color_name, code=color_code: self.on_color_click(name, code),
                relief="raised",
                bd=3
            )
            btn.grid(row=0, column=i, padx=5, pady=5)
        
        ttk.Label(main_frame, text="Название цвета:", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, pady=(10, 5))
        
        self.color_name_label = ttk.Label(main_frame, text="", font=("Arial", 12, "bold"), foreground="blue")
        self.color_name_label.grid(row=2, column=1, sticky=tk.W, pady=(10, 5))
        
        ttk.Label(main_frame, text="Код цвета:", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, pady=(10, 5))
        
        self.color_code_entry = ttk.Entry(main_frame, font=("Arial", 12), width=20)
        self.color_code_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=(10, 5))
        
        info_frame = ttk.Frame(main_frame)
        info_frame.grid(row=4, column=0, columnspan=2, pady=(20, 0))
        
        info_text = "Нажмите на любую кнопку, чтобы увидеть код и название цвета"
        info_label = ttk.Label(info_frame, text=info_text, font=("Arial", 10), foreground="gray")
        info_label.pack()
    
    def on_color_click(self, color_name, color_code):
        self.color_code_entry.delete(0, tk.END)
        self.color_code_entry.insert(0, color_code)
        
        self.color_name_label.config(text=color_name)
        
        self.color_name_label.config(foreground=color_code)

def main():
    root = tk.Tk()
    app = RainbowColorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()