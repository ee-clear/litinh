import tkinter as tk 
from tkinter import filedialog, messagebox

class TXT_Editor:
        def __init__(self, root):
                self.root = root
                self.root.title("TXT-ужас")
                self.root.geometry("800x600")

                self.text_area = tk.Text(self.root, wrap = 'word', font = ('Arial', 12))
                self.text_area.pack(expand = True, fill = 'both', padx = 5, pady = 5)

        def create_menu(self):
                menu_bar = tk.menu(self.root)
                self.root.config(menu = menu_bar)

                file_menu = tk.menu(menu_bar, tearoff = 0)

                menu_bar.add_cascade(label="файл", menu = file_menu)

                file_menu.add_command(label = "новый", command = self.new_file)
                file_menu.add_command(label = "открыть...", command = self.open_file)
                file_menu.add_command(label = "сохранить", command = self.save_file)

                file_menu.add_command(label = "сохранить как...", command = self.save_file_as)

                file_menu.add_command(label="выход", command = self.root.quit)
if __name__ == "__main__":
        root = tk.Tk()
        app = TXT_Editor(root)
        root.mainloop()
