import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

from imgoptimizr.imageutil.utils import webps


def int_val(string):
    try:
        return int(string)
    except ValueError:
        return -1


class WebPManyGui:
    def __init__(self):
        unit = 15
        row = 1
        self.root = tk.Tk()
        self.root.geometry('200x215')
        self.root.title('WebP Many')
        self.src_label = tk.Label(self.root, text='Source directory').place(x=unit, y=unit * row)
        row += 2
        self.src_dir_val = tk.StringVar()
        self.src_dir = tk.Entry(self.root, textvariable=self.src_dir_val)
        self.src_dir.place(x=unit, y=unit * row)
        self.src_button = tk.Button(self.root, text='...', command=self.choose_src)
        self.src_button.place(x=unit * 10, y=unit * row)
        row += 3
        self.dest_label = tk.Label(self.root, text='Destination directory').place(x=unit, y=unit * row)
        row += 2
        self.dest_dir_val = tk.StringVar()
        self.dest_dir = tk.Entry(self.root, textvariable=self.dest_dir_val)
        self.dest_dir.place(x=unit, y=unit * row)
        self.dest_button = tk.Button(self.root, text='...', command=self.choose_dest)
        self.dest_button.place(x=unit * 10, y=unit * row)
        row += 3
        self.create_button = tk.Button(self.root, text='Create', command=self.create_webp_many)
        self.create_button.place(x=unit, y=unit * row)

    def thumbnail_exact_many_window(self):
        self.root.mainloop()

    def choose_src(self):
        result = filedialog.askdirectory()
        self.src_dir_val.set(result)

    def choose_dest(self):
        result = filedialog.askdirectory()
        self.dest_dir_val.set(result)

    def create_webp_many(self):
        src_dir = self.src_dir_val.get()
        dest_dir = self.dest_dir_val.get()
        if not os.path.isdir(src_dir):
            messagebox.showerror('Invalid directory', 'Source directory not valid')
            return
        # todo check if dest path is valid path without creating it if it doesn't exist
        try:
            webps(src_dir, dest_dir)
            messagebox.showinfo('Success', 'Finished creating webp files')
        except BaseException as error:
            messagebox.showerror('Error', error)


WebPManyGui().root.mainloop()
