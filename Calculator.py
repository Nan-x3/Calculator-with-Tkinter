# Importing

from tkinter import *

# Window

win = Tk()
win.title("Calculator")
win.geometry("400x210")

e = Entry(win, width=64, borderwidth=5)
e.place(x=3, anchor=NW)

# Variables

default = 0

buttons = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

themes = ["🔆", "🌙", "🍃", "🌸", "🫐", "🍒"]
theme_index = 0

# Defining Functions


def cycle_theme():
    global theme_index
    global button
    theme_index = (theme_index + 1) % len(themes)
    theme = themes[theme_index]
    button.config(text=theme)

    if theme_index == 0:
        win.config(bg="#f0f0f0")
        e.config(bg="#f0f0f0", fg="#000000")
        button.config(bg="#e0e0e0", fg="#000000")
        button1.config(bg="#e0e0e0", fg="#000000")
        button2.config(bg="#e0e0e0", fg="#000000")
        button3.config(bg="#e0e0e0", fg="#000000")
        button4.config(bg="#e0e0e0", fg="#000000")
        button5.config(bg="#e0e0e0", fg="#000000")
        button6.config(bg="#e0e0e0", fg="#000000")
        button7.config(bg="#e0e0e0", fg="#000000")
        button8.config(bg="#e0e0e0", fg="#000000")
        button9.config(bg="#e0e0e0", fg="#000000")
        button10.config(bg="#e0e0e0", fg="#000000")
        button11.config(bg="#e0e0e0", fg="#000000")
        button12.config(bg="#e0e0e0", fg="#000000")
        button13.config(bg="#e0e0e0", fg="#000000")
        button14.config(bg="#e0e0e0", fg="#000000")
        button15.config(bg="#e0e0e0", fg="#000000")
        button16.config(bg="#e0e0e0", fg="#000000")
        button17.config(bg="#e0e0e0", fg="#000000")
        button18.config(bg="#e0e0e0", fg="#000000")
        button19.config(bg="#e0e0e0", fg="#000000")

    elif theme_index == 1:
        win.config(bg="#1f1f1f")
        e.config(bg="#1f1f1f", fg="#ffffff")
        button.config(bg="#303030", fg="#ffffff")
        button1.config(bg="#303030", fg="#ffffff")
        button2.config(bg="#303030", fg="#ffffff")
        button3.config(bg="#303030", fg="#ffffff")
        button4.config(bg="#303030", fg="#ffffff")
        button5.config(bg="#303030", fg="#ffffff")
        button6.config(bg="#303030", fg="#ffffff")
        button7.config(bg="#303030", fg="#ffffff")
        button8.config(bg="#303030", fg="#ffffff")
        button9.config(bg="#303030", fg="#ffffff")
        button10.config(bg="#303030", fg="#ffffff")
        button11.config(bg="#303030", fg="#ffffff")
        button12.config(bg="#303030", fg="#ffffff")
        button13.config(bg="#303030", fg="#ffffff")
        button14.config(bg="#303030", fg="#ffffff")
        button15.config(bg="#303030", fg="#ffffff")
        button16.config(bg="#303030", fg="#ffffff")
        button17.config(bg="#303030", fg="#ffffff")
        button18.config(bg="#303030", fg="#ffffff")
        button19.config(bg="#303030", fg="#ffffff")

    elif theme_index == 2:
        win.config(bg="#77ff77")
        e.config(bg="#77ff77", fg="#1f1111")
        button.config(bg="#b5ffb5", fg="#1f1111")
        button.config(bg="#b5ffb5", fg="#1f1111")
        button1.config(bg="#b5ffb5", fg="#1f1111")
        button2.config(bg="#b5ffb5", fg="#1f1111")
        button3.config(bg="#b5ffb5", fg="#1f1111")
        button4.config(bg="#b5ffb5", fg="#1f1111")
        button5.config(bg="#b5ffb5", fg="#1f1111")
        button6.config(bg="#b5ffb5", fg="#1f1111")
        button7.config(bg="#b5ffb5", fg="#1f1111")
        button8.config(bg="#b5ffb5", fg="#1f1111")
        button9.config(bg="#b5ffb5", fg="#1f1111")
        button10.config(bg="#b5ffb5", fg="#1f1111")
        button11.config(bg="#b5ffb5", fg="#1f1111")
        button12.config(bg="#b5ffb5", fg="#1f1111")
        button13.config(bg="#b5ffb5", fg="#1f1111")
        button14.config(bg="#b5ffb5", fg="#1f1111")
        button15.config(bg="#b5ffb5", fg="#1f1111")
        button16.config(bg="#b5ffb5", fg="#1f1111")
        button17.config(bg="#b5ffb5", fg="#1f1111")
        button18.config(bg="#b5ffb5", fg="#1f1111")
        button19.config(bg="#b5ffb5", fg="#1f1111")

    elif theme_index == 3:
        win.config(bg="#f8c8dc")
        e.config(bg="#f8c8dc", fg="#d2042d")
        button.config(bg="#ffd9e9", fg="#d2042d")
        button.config(bg="#ffd9e9", fg="#d2042d")
        button1.config(bg="#ffd9e9", fg="#d2042d")
        button2.config(bg="#ffd9e9", fg="#d2042d")
        button3.config(bg="#ffd9e9", fg="#d2042d")
        button4.config(bg="#ffd9e9", fg="#d2042d")
        button5.config(bg="#ffd9e9", fg="#d2042d")
        button6.config(bg="#ffd9e9", fg="#d2042d")
        button7.config(bg="#ffd9e9", fg="#d2042d")
        button8.config(bg="#ffd9e9", fg="#d2042d")
        button9.config(bg="#ffd9e9", fg="#d2042d")
        button10.config(bg="#ffd9e9", fg="#d2042d")
        button11.config(bg="#ffd9e9", fg="#d2042d")
        button12.config(bg="#ffd9e9", fg="#d2042d")
        button13.config(bg="#ffd9e9", fg="#d2042d")
        button14.config(bg="#ffd9e9", fg="#d2042d")
        button15.config(bg="#ffd9e9", fg="#d2042d")
        button16.config(bg="#ffd9e9", fg="#d2042d")
        button17.config(bg="#ffd9e9", fg="#d2042d")
        button18.config(bg="#ffd9e9", fg="#d2042d")
        button19.config(bg="#ffd9e9", fg="#d2042d")

    elif theme_index == 4:
        win.config(bg="#add8e6")
        e.config(bg="#add8e6", fg="#2c5cab")
        button.config(bg="#bbeafa", fg="#2c5cab")
        button.config(bg="#bbeafa", fg="#2c5cab")
        button1.config(bg="#bbeafa", fg="#2c5cab")
        button2.config(bg="#bbeafa", fg="#2c5cab")
        button3.config(bg="#bbeafa", fg="#2c5cab")
        button4.config(bg="#bbeafa", fg="#2c5cab")
        button5.config(bg="#bbeafa", fg="#2c5cab")
        button6.config(bg="#bbeafa", fg="#2c5cab")
        button7.config(bg="#bbeafa", fg="#2c5cab")
        button8.config(bg="#bbeafa", fg="#2c5cab")
        button9.config(bg="#bbeafa", fg="#2c5cab")
        button10.config(bg="#bbeafa", fg="#2c5cab")
        button11.config(bg="#bbeafa", fg="#2c5cab")
        button12.config(bg="#bbeafa", fg="#2c5cab")
        button13.config(bg="#bbeafa", fg="#2c5cab")
        button14.config(bg="#bbeafa", fg="#2c5cab")
        button15.config(bg="#bbeafa", fg="#2c5cab")
        button16.config(bg="#bbeafa", fg="#2c5cab")
        button17.config(bg="#bbeafa", fg="#2c5cab")
        button18.config(bg="#bbeafa", fg="#2c5cab")
        button19.config(bg="#bbeafa", fg="#2c5cab")

    elif theme_index == 5:
        win.config(bg="#d20434")
        e.config(bg="#d20434", fg="#344c2e")
        button.config(bg="#ff5047", fg="#344c2e")
        button.config(bg="#ff5047", fg="#344c2e")
        button1.config(bg="#ff5047", fg="#344c2e")
        button2.config(bg="#ff5047", fg="#344c2e")
        button3.config(bg="#ff5047", fg="#344c2e")
        button4.config(bg="#ff5047", fg="#344c2e")
        button5.config(bg="#ff5047", fg="#344c2e")
        button6.config(bg="#ff5047", fg="#344c2e")
        button7.config(bg="#ff5047", fg="#344c2e")
        button8.config(bg="#ff5047", fg="#344c2e")
        button9.config(bg="#ff5047", fg="#344c2e")
        button10.config(bg="#ff5047", fg="#344c2e")
        button11.config(bg="#ff5047", fg="#344c2e")
        button12.config(bg="#ff5047", fg="#344c2e")
        button13.config(bg="#ff5047", fg="#344c2e")
        button14.config(bg="#ff5047", fg="#344c2e")
        button15.config(bg="#ff5047", fg="#344c2e")
        button16.config(bg="#ff5047", fg="#344c2e")
        button17.config(bg="#ff5047", fg="#344c2e")
        button18.config(bg="#ff5047", fg="#344c2e")
        button19.config(bg="#ff5047", fg="#344c2e")


def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))


def Clear():
    e.delete(0, END)


def button_nil():
    current = e.get()
    if current == "":
        e.insert(0, "0")
    if current != "":
        if current[-1] != "+":
            if current[-1] != "-":
                if current[-1] != "*":
                    if current[-1] != "/":
                        e.delete(0, END)
                        e.insert(0, str(current) + "+")


def button_add():
    current = e.get()
    if current[-1] != '.':
        if current[-1] != "+":
            if current[-1] != "-":
                if current[-1] != "*":
                    if current[-1] != "/":
                        e.delete(0, END)
                        e.insert(0, str(current) + "+")


def button_sub():
    current = e.get()
    if current[-1] != '.':
        if current[-1] != "+":
            if current[-1] != "-":
                if current[-1] != "*":
                    if current[-1] != "/":
                        e.delete(0, END)
                        e.insert(0, str(current) + "-")


def button_mult():
    current = e.get()
    if current[-1] != '.':
        if current[-1] != "+":
            if current[-1] != "-":
                if current[-1] != "*":
                    if current[-1] != "/":
                        e.delete(0, END)
                        e.insert(0, str(current) + "*")


def button_div():
    current = e.get()
    if current[-1] != '.':
        if current[-1] != "+":
            if current[-1] != "-":
                if current[-1] != "*":
                    if current[-1] != "/":
                        e.delete(0, END)
                        e.insert(0, str(current) + "/")


def button_equal():
    expression = e.get()
    try:
        result = eval(expression)
        e.delete(0, END)
        e.insert(0, str(result))
    except:
        e.delete(0, END)
        e.insert(0, "Error")


def button_backspace():
    current_expression = e.get()
    new_expression = current_expression[:-1]
    e.delete(0, END)
    e.insert(0, new_expression)


def button_dot():
    current_expression = e.get()
    if '.' in current_expression.split()[-1]:
        return
    if current_expression[-1] != '.':
        if current_expression[-1] != "+":
            if current_expression[-1] != "-":
                if current_expression[-1] != "*":
                    if current_expression[-1] != "/":
                        new_expression = current_expression + "."
                        e.delete(0, END)
                        e.insert(0, new_expression)


button = Button(win, text=themes[theme_index], font=(
    "ms ui gothic", 15), width=8, height=1, command=cycle_theme)
button.place(x=5, y=31)

button1 = Button(win, text="", font=("ms ui gothic", 15), width=8, height=1)
button1.place(x=103, y=31)

button2 = Button(win, text="⇦", font=("ms ui gothic", 15),
                 width=8, height=1, command=button_backspace)
button2.place(x=201, y=31)

button3 = Button(win, text="C", font=("ms ui gothic", 15),
                 width=8, height=1, command=lambda: Clear())
button3.place(x=299, y=31)

button4 = Button(win, text="1", font=("ms ui gothic", 15),
                 width=8, height=1, command=lambda: button_click(1))
button4.place(x=5, y=66)

button5 = Button(win, text="2", font=("ms ui gothic", 15),
                 width=8, height=1, command=lambda: button_click(2))
button5.place(x=103, y=66)

button6 = Button(win, text="3", font=("ms ui gothic", 15),
                 width=8, height=1, command=lambda: button_click(3))
button6.place(x=201, y=66)

button7 = Button(win, text="+", font=("ms ui gothic", 15),
                 width=8, height=1, command=button_add)
button7.place(x=299, y=66)

button8 = Button(win, text="4", font=("ms ui gothic", 15),
                 width=8, height=1, command=lambda: button_click(4))
button8.place(x=5, y=101)

button9 = Button(win, text="5", font=("ms ui gothic", 15),
                 width=8, height=1, command=lambda: button_click(5))
button9.place(x=103, y=101)

button10 = Button(win, text="6", font=("ms ui gothic", 15),
                  width=8, height=1, command=lambda: button_click(6))
button10.place(x=201, y=101)

button11 = Button(win, text="-", font=("ms ui gothic", 15),
                  width=8, height=1, command=button_sub)
button11.place(x=299, y=101)

button12 = Button(win, text="7", font=("ms ui gothic", 15),
                  width=8, height=1, command=lambda: button_click(7))
button12.place(x=5, y=136)

button13 = Button(win, text="8", font=("ms ui gothic", 15),
                  width=8, height=1, command=lambda: button_click(8))
button13.place(x=103, y=136)

button14 = Button(win, text="9", font=("ms ui gothic", 15),
                  width=8, height=1, command=lambda: button_click(9))
button14.place(x=201, y=136)

button15 = Button(win, text="×", font=("ms ui gothic", 15),
                  width=8, height=1, command=button_mult)
button15.place(x=299, y=136)

button16 = Button(win, text="↲", font=("ms ui gothic", 15),
                  width=8, height=1, command=button_equal)
button16.place(x=5, y=171)

button17 = Button(win, text="0", font=("ms ui gothic", 15),
                  width=8, height=1, command=lambda: button_click(0))
button17.place(x=103, y=171)

button18 = Button(win, text="·", font=("ms ui gothic", 15),
                  width=8, height=1, command=button_dot)
button18.place(x=201, y=171)

button19 = Button(win, text="÷", font=("ms ui gothic", 15),
                  width=8, height=1, command=button_div)
button19.place(x=299, y=171)

# Main Loop

win.mainloop()
