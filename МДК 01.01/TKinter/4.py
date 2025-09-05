import tkinter as tk

class CalculatorButtonsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Кнопки калькулятора")
        self.root.geometry("250x300")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.create_buttons()
    
    
    def create_buttons(self):
        button_config = {
            "font": ("Arial", 14, "bold"),
            "width": 5,
            "height": 2,
            "bd": 3,
            "relief": "raised"
        }
        
        seven_btn = tk.Button(
            self.root,
            text="7",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        seven_btn.grid(row=0, column=0, padx=5, pady=5)
        
        eight_btn = tk.Button(
            self.root,
            text="8",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        eight_btn.grid(row=0, column=1, padx=5, pady=5)
        
        nine_btn = tk.Button(
            self.root,
            text="9",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        nine_btn.grid(row=0, column=2, padx=5, pady=5)
        
        four_btn = tk.Button(
            self.root,
            text="4",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        four_btn.grid(row=1, column=0, padx=5, pady=5)
        
        five_btn = tk.Button(
            self.root,
            text="5",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        five_btn.grid(row=1, column=1, padx=5, pady=5)
        
        six_btn = tk.Button(
            self.root,
            text="6",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        six_btn.grid(row=1, column=2, padx=5, pady=5)
        
        one_btn = tk.Button(
            self.root,
            text="1",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        one_btn.grid(row=2, column=0, padx=5, pady=5)
        
        two_btn = tk.Button(
            self.root,
            text="2",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        two_btn.grid(row=2, column=1, padx=5, pady=5)
        
        three_btn = tk.Button(
            self.root,
            text="3",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        three_btn.grid(row=2, column=2, padx=5, pady=5)
        
        zero_btn = tk.Button(
            self.root,
            text="0",
            bg="#95E1D3",
            fg="black",
            font=("Arial", 14, "bold"),
            height=2,
            bd=3,
            relief="raised"
        )
        zero_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        
        decimal_btn = tk.Button(
            self.root,
            text=".",
            bg="#95E1D3",
            fg="black",
            **button_config
        )
        decimal_btn.grid(row=3, column=2, padx=5, pady=5)

def main():
    root = tk.Tk()
    app = CalculatorButtonsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()