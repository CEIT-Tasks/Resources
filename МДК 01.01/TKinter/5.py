import tkinter as tk

class DiagonalButtonsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Диагональное расположение кнопок")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.create_buttons()
    
    def create_buttons(self):
        button_config = {
            "font": ("Arial", 14, "bold"),
            "width": 4,
            "height": 2,
            "bd": 3,
            "relief": "raised"
        }
        
        btn1 = tk.Button(
            self.root,
            text="1",
            bg="#FF6B6B",
            fg="white",
            **button_config
        )
        btn1.grid(row=0, column=0, padx=5, pady=5)
        
        btn2 = tk.Button(
            self.root,
            text="2",
            bg="#FF6B6B",
            fg="white",
            **button_config
        )
        btn2.grid(row=1, column=1, padx=5, pady=5)
        
        btn3 = tk.Button(
            self.root,
            text="3",
            bg="#4ECDC4",
            fg="white",
            **button_config
        )
        btn3.grid(row=2, column=2, padx=5, pady=5)
        
        btn4 = tk.Button(
            self.root,
            text="4",
            bg="#FF6B6B",
            fg="white",
            **button_config
        )
        btn4.grid(row=3, column=3, padx=5, pady=5)
        
        btn5 = tk.Button(
            self.root,
            text="5",
            bg="#FF6B6B",
            fg="white",
            **button_config
        )
        btn5.grid(row=4, column=4, padx=5, pady=5)
        
        btn6 = tk.Button(
            self.root,
            text="6",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        btn6.grid(row=0, column=4, padx=5, pady=5)
        
        btn7 = tk.Button(
            self.root,
            text="7",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        btn7.grid(row=1, column=3, padx=5, pady=5)
        
        btn8 = tk.Button(
            self.root,
            text="8",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        btn8.grid(row=3, column=1, padx=5, pady=5)
        
        btn9 = tk.Button(
            self.root,
            text="9",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        btn9.grid(row=4, column=0, padx=5, pady=5)

def main():
    root = tk.Tk()
    app = DiagonalButtonsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()