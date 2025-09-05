import tkinter as tk

def about():
    print("О программе: Приложение с меню")

root = tk.Tk()
root.title("Меню")
root.geometry("400x300")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Создать")
file_menu.add_command(label="Открыть")
file_menu.add_command(label="Сохранить")
file_menu.add_separator()
file_menu.add_command(label="Выход", command=root.quit)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Правка", menu=edit_menu)
edit_menu.add_command(label="Вырезать")
edit_menu.add_command(label="Копировать")
edit_menu.add_command(label="Вставить")

help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Помощь", menu=help_menu)
help_menu.add_command(label="О программе", command=about)

root.mainloop()