import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os

from imgoptimizr.imageutil.utils import thumbnails_exact


def int_val(string):
    try:
        return int(string)
    except ValueError:
        return -1


class ThumbnailExactManyGui:
    def __init__(self):
        unit = 15
        row = 1
        self.root = tk.Tk()
        self.root.geometry('265x380')
        self.root.resizable(0, 0)
        self.root.title('Thumbnail Exact Many')
        self.src_label = tk.Label(self.root, text='Source directory').place(x=unit, y=unit * row)
        row += 2
        self.src_dir_val = tk.StringVar()
        self.src_dir = tk.Entry(self.root, textvariable=self.src_dir_val)
        self.src_dir.place(x=unit, y=unit * row, width=200, height=25)
        self.src_button = tk.Button(self.root, text='...', command=self.choose_src)
        self.src_button.place(x=unit * 15, y=unit * row)
        row += 3
        self.dest_label = tk.Label(self.root, text='Destination directory').place(x=unit, y=unit * row)
        row += 2
        self.dest_dir_val = tk.StringVar()
        self.dest_dir = tk.Entry(self.root, textvariable=self.dest_dir_val)
        self.dest_dir.place(x=unit, y=unit * row, width=200, height=25)
        self.dest_button = tk.Button(self.root, text='...', command=self.choose_dest)
        self.dest_button.place(x=unit * 15, y=unit * row)
        row += 3
        self.width_label = tk.Label(self.root, text='Width').place(x=unit, y=unit * row)
        row += 2
        self.width_val = tk.StringVar()
        self.width = tk.Entry(self.root, textvariable=self.width_val)
        self.width.place(x=unit, y=unit * row, width=100, height=25)
        row += 3
        self.height_label = tk.Label(self.root, text='Height').place(x=unit, y=unit * row)
        row += 2
        self.height_val = tk.StringVar()
        self.height = tk.Entry(self.root, textvariable=self.height_val)
        self.height.place(x=unit, y=unit * row, width=100, height=25)
        row += 3
        self.create_button = tk.Button(self.root, text='Create', command=self.create_thumbnail_exact_many)
        self.create_button.place(x=unit, y=unit * row)

    def thumbnail_exact_many_window(self):
        self.root.mainloop()

    def choose_src(self):
        result = filedialog.askdirectory()
        self.src_dir_val.set(result)

    def choose_dest(self):
        result = filedialog.askdirectory()
        self.dest_dir_val.set(result)

    def create_thumbnail_exact_many(self):
        src_dir = self.src_dir_val.get()
        dest_dir = self.dest_dir_val.get()
        if not os.path.isdir(src_dir):
            messagebox.showerror('Invalid directory', 'Source directory not valid')
            return
        # todo check if dest path is valid path without creating it if it doesn't exist
        width = int_val(self.width_val.get())
        height = int_val(self.height_val.get())
        if width < 0 or height < 0:
            messagebox.showerror('Invalid dimensions', 'Width / height not valid')
        try:
            thumbnails_exact(src_dir, dest_dir, (width, height))
            messagebox.showinfo('Success', 'Finished creating thumbnails')
        except BaseException as error:
            messagebox.showerror('Error', error)


ThumbnailExactManyGui().root.mainloop()
