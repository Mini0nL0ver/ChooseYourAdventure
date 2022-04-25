import tkinter as tk


def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window = tk.Tk()
window.title("*placeholder*")

window.rowconfigure([0, 1, 2], minsize=150, weight=1)
window.columnconfigure(0, minsize=300, weight=1)

btn_colour = {
    "background": "#FFB6C1",
    "foreground": "White",
    "activebackground": "#FFB6C1",
    "activeforeground": "White"
}

lbl_value = tk.Label(master=window, text="0", borderwidth=25, bg="#FFB6C1", fg="White")
lbl_value.grid(row=0, column=0, sticky="nsew")

btn_choice_A = tk.Button(master=window, text="-", borderwidth=25, command=decrease, **btn_colour)
btn_choice_A.grid(row=1, column=0, sticky="nsew")

btn_choice_B = tk.Button(master=window, text="+", borderwidth=25, command=increase, **btn_colour)
btn_choice_B.grid(row=2, column=0, sticky="nsew")

window.mainloop()
