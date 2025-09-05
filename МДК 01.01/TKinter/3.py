import tkinter as tk

class CompassApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Стороны света")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")
        
        self.create_compass_labels()
    
    def create_compass_labels(self):
        north_label = tk.Label(
            self.root,
            text="СЕВЕР",
            font=("Arial", 16, "bold"),
            bg="#87CEEB",
            fg="white",
            width=12,
            height=2,
            relief="raised",
            bd=3
        )
        north_label.place(x=150, y=30)
        
        south_label = tk.Label(
            self.root,
            text="ЮГ",
            font=("Arial", 16, "bold"),
            bg="#FFB6C1",
            fg="white",
            width=12,
            height=2,
            relief="raised",
            bd=3
        )
        south_label.place(x=150, y=330)
        
        west_label = tk.Label(
            self.root,
            text="ЗАПАД",
            font=("Arial", 16, "bold"),
            bg="#98FB98",
            fg="white",
            width=12,
            height=2,
            relief="raised",
            bd=3
        )
        west_label.place(x=30, y=180)
        
        east_label = tk.Label(
            self.root,
            text="ВОСТОК",
            font=("Arial", 16, "bold"),
            bg="#F0E68C",
            fg="black",
            width=12,
            height=2,
            relief="raised",
            bd=3
        )
        east_label.place(x=270, y=180)
        
        center_label = tk.Label(
            self.root,
            text="🧭",
            font=("Arial", 40),
            bg="#f0f0f0",
            fg="black"
        )
        center_label.place(x=185, y=175)
        
        arrow_north = tk.Label(
            self.root,
            text="↑",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#87CEEB"
        )
        arrow_north.place(x=195, y=100)
        
        arrow_south = tk.Label(
            self.root,
            text="↓",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#FFB6C1"
        )
        arrow_south.place(x=195, y=270)
        
        arrow_west = tk.Label(
            self.root,
            text="←",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#98FB98"
        )
        arrow_west.place(x=120, y=185)
        
        arrow_east = tk.Label(
            self.root,
            text="→",
            font=("Arial", 24, "bold"),
            bg="#f0f0f0",
            fg="#F0E68C"
        )
        arrow_east.place(x=270, y=185)

def main():
    root = tk.Tk()
    
    app = CompassApp(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()