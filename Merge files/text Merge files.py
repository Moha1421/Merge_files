import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
root.title("مدمج الملفات النصية")
files = []

def add_files():
    for widget in frame.winfo_children():
        widget.destroy()

    filenames = filedialog.askopenfilenames(initialdir="/", title="Select Files",
                                            filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    for filename in filenames:
        files.append(filename)
        label = tk.Label(frame, text=filename, bg="gray")
        label.pack()

def merge_files():
    content = ""
    for file in files:
        with open(file, 'r') as f:
            content += f.read() + "\n"
    
    with open("merged_files.txt", 'w') as f:
        f.write(content)
    label = tk.Label(frame, text="Files Merged Successfully!", bg="gray")
    label.pack()

root.geometry("500x500")
root.configure(bg='gray20')

frame = tk.Frame(root, bg="gray")
frame.place(relwidth=0.8, relheight=0.75, relx=0.1, rely=0.05)

openFile = tk.Button(root, text="Open Files", padx=10, pady=5, fg="white", bg="gray", command=add_files)
openFile.pack()

mergeButton = tk.Button(root, text="Merge Files", padx=10, pady=5, fg="white", bg="gray", command=merge_files)
mergeButton.pack()

root.mainloop()
