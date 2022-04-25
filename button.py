import tkinter as tk


def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"


def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window = tk.Tk()
window.title("Increment Counter")

window.rowconfigure(0, minsize=250, weight=1)
window.columnconfigure([0, 1, 2], minsize=250, weight=1)

btn_colour = {
    "background": "#FFB6C1",
    "foreground": "White",
    "activebackground": "#FFB6C1",
    "activeforeground": "White"
}

btn_decrease = tk.Button(master=window, text="-", borderwidth=25, command=decrease, **btn_colour)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0", borderwidth=125, bg="#FFB6C1", fg="White")
lbl_value.grid(row=0, column=1, sticky="nsew")

btn_increase = tk.Button(master=window, text="+", borderwidth=25, command=increase, **btn_colour)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()
