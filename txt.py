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

        def new_file(self):
                self.text_area.delete(1.0,tk.END)
                self.root.title("TXT-новый документ")

        def open_file(self):
                file_path = filedialog.askopenfilename(defaultextension = ".txt", filetypes = [("текстовые файлы", "*.txt"), ("все файлы", "*.*")])
                if file_path:
                        try:
                                with open(file_path, 'r', encoding = 'utf-8') as file:
                                        content = file.read()
                                        self.text_area.delete(1.0, tk.END)
                                        self.text_area.insert(1.0, content)
                                        self.root.title(f"TXT - {file_path}")
                                        self.current_file_path = file_path
                        except Exception as e:
                                messagebox.showerror("ошибка", f"не удалось открыть файл: {e}")
        def save_file_as(self):
                file_path = filedialog.asksaveasfilename(defaultextansion = ".txt", filetypes = [("текстовые файлы" "*.txt"), ("все файлы", "*.*")])
                if file_path:
                        try:
                                content = self.text_area.get(1.0, tk.END)
                                with open(file_path, 'w', encoding = 'utf-8') as file:
                                        file.write(content)
                                        self.root.title(f"TXT - {file_path}")
                                        self.current_file_path = file_path
                        except Exception as e:
                                messagebox.showeerror("ошибка", f"не удалось сохранить файл: {e}")
        def save_file(self):
                if hasattr(self, 'current_file_path') and self.current_file_path:
                        try:
                                content = self.text_area.get(1.0, tk.END)
                                with open(self.current_file_path, 'w', encoding = 'utf-8') as file:
                                        file.write(content)
                        except Exception as e:
                                messagebox.showerror("ошибка", f"не удалось сохранить файл: {e}")
                        else:
                                self.save_file_as()
if __name__ == "__main__":
        root = tk.Tk()
        app = TXT_Editor(root)
        root.mainloop()
