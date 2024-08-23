import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Global variable to store the current file path
current_file_path = None

def new_file():
    global current_file_path
    current_file_path = None
    text.delete(1.0, tk.END)

def open_file():
    global current_file_path
    file_path = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if file_path:
        current_file_path = file_path
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    global current_file_path
    if current_file_path:
        with open(current_file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("File Saved", "Successfully saved the file")
    else:
        save_as_file()

def save_as_file():
    global current_file_path
    file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
    if file_path:
        current_file_path = file_path
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("File Saved", "Successfully saved the file")

def change_font_size():
    size = simpledialog.askinteger("Font Size", "Enter font size:", initialvalue=12, minvalue=8, maxvalue=72)
    if size:
        text.config(font=('Helvetica', size))
root = tk.Tk()
root.title('Custom Notepad')
root.geometry("800x600")

# Creating a menu bar for the root window
menu = tk.Menu(root)
root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_command(label='Save As', command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

# Edit Menu
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label="Change Font Size", command=change_font_size)

# Text Widget
text = tk.Text(root, wrap=tk.WORD, font=('Helvetica', 12), fg='blue')
text.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()
