import tkinter as tk
from PIL import Image, ImageTk
from choicepages import State

_image_cache = dict()


def picture(local_path: str) -> Image.Image:
    if local_path in _image_cache.keys():
        return _image_cache[local_path]
    else:
        img = Image.open(local_path)
        _image_cache[local_path] = img
        return img


default_style = {
    "borderwidth": 5, "bg": "#414345", "fg": "White"
}

button_style = {
    "borderwidth": 20, "bg": "#323435", "activebackground": "#323435", "foreground": "White", "activeforeground": "White"
}

window = tk.Tk()
window.title("*placeholder*")

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

State(
    picture("Pictures/dragon1.png"),
    "root",
    **{
        "option one": State(
            picture("Pictures/placeholder.png"),
            "one"
        ).state_style(**default_style).option_style(**button_style),
        "option two": State(
            picture("Pictures/placeholder.png"),
            "two"
        ).state_style(**default_style).option_style(**button_style)
    }
).state_style(**default_style)(window)

window.mainloop()
