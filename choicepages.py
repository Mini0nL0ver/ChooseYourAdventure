import tkinter

from PIL import ImageTk, Image
from tkinter import Frame, Event
from details import *


class Branch(Frame):  # concrete widget
    def __init__(self, parent, style, image: Image.Image, info_text, **options: 'Path'):
        Frame.__init__(self, parent)

        self.image = ImageTk.PhotoImage(image)

        self.rowconfigure(len(options) + 1, minsize=50, weight=0)
        self.columnconfigure(0, minsize=100, weight=1)
        self.grid(sticky="nsew")

        self.rowconfigure(0, weight=1)
        _ = {self.rowconfigure(row, weight=0) for row in range(1, len(options) + 2)}

        row_nbr = [0]

        def next_row() -> int:
            nbr = row_nbr[0]
            row_nbr[0] = nbr + 1
            return nbr

        can = tkinter.Canvas(master=self, **{key: prop for (key, prop) in style.items() if key in canvas_accepted_props})
        can.grid(row=next_row(), column=0, sticky="nsew")
        can.create_image(0, 0, anchor=tkinter.NW, image=self.image)

        def resize(e: Event):
            scale_factor = min(e.width / image.width, e.height / image.height)
            self.image = ImageTk.PhotoImage(image.resize((int(image.width * scale_factor), int(image.height * scale_factor)), Image.ANTIALIAS))
            can.create_image(e.width / 2, e.height / 2, anchor=tkinter.CENTER, image=self.image)

        can.bind("<Configure>", resize)
        tkinter.Label(master=self, text=info_text, **{key: prop for (key, prop) in style.items() if key in label_accepted_props}).grid(row=next_row(), column=0, sticky="nsew")

        def make_button(_txt, _path: 'Path') -> None:
            tkinter.Button(master=self, text=_txt, command=lambda: self.swap(_path), **{key: prop for (key, prop) in _path.path_style.items() if key in button_accepted_props}).grid(row=next_row(), column=0, sticky="nsew")

        _ = {make_button(txt, state) for (txt, state) in options.items()}

    def swap(self, path: 'Path', master=None) -> None:
        if master is None: master = self.master
        self.destroy()
        path(master)


class State:  # functional Branch
    def __init__(self, image: Image.Image, info_text, **options: 'Path'):
        self.image_arg = image
        self.text_arg = info_text
        self.options_arg = options
        self.branch_style = dict()

    def __call__(self, parent) -> Branch:
        return Branch(parent, self.branch_style, self.image_arg, self.text_arg, **self.options_arg)

    def state_style(self, **kwargs) -> 'State':
        self.branch_style = kwargs
        return self

    def option_style(self, **kwargs) -> 'Path':
        return Path(self).option_style(**kwargs)

    def path(self) -> 'Path':
        return Path(self)


class Path:  # functional state transfer
    def __init__(self, state):
        self.target = state
        self.path_style = dict()

    def __call__(self, parent) -> Branch:
        return self.target(parent)

    def option_style(self, **kwargs) -> 'Path':
        self.path_style = kwargs
        return self
