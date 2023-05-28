# Importing

from tkinter import *

# Window

win = Tk()
win.title("Calculator")
win.geometry("400x210")

# Variables

default = 0

label = Label(win, text=default, font=("ms ui gothic", 15))
label.place(x=382, y=3,  anchor=NW)

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


def cycle_theme1():
    global theme_index
    global button
    theme_index = (theme_index + 1) % len(themes)
    theme = themes[theme_index]
    button.config(text=theme)

    if theme_index == 0:
        win.config(bg="#f0f0f0")
        label.config(bg="#f0f0f0", fg="#000000")
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
        label.config(bg="#1f1f1f", fg="#ffffff")
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
        label.config(bg="#77ff77", fg="#000000")
        button.config(bg="#b5ffb5", fg="#000000")
        button.config(bg="#b5ffb5", fg="#000000")
        button1.config(bg="#b5ffb5", fg="#000000")
        button2.config(bg="#b5ffb5", fg="#000000")
        button3.config(bg="#b5ffb5", fg="#000000")
        button4.config(bg="#b5ffb5", fg="#000000")
        button5.config(bg="#b5ffb5", fg="#000000")
        button6.config(bg="#b5ffb5", fg="#000000")
        button7.config(bg="#b5ffb5", fg="#000000")
        button8.config(bg="#b5ffb5", fg="#000000")
        button9.config(bg="#b5ffb5", fg="#000000")
        button10.config(bg="#b5ffb5", fg="#000000")
        button11.config(bg="#b5ffb5", fg="#000000")
        button12.config(bg="#b5ffb5", fg="#000000")
        button13.config(bg="#b5ffb5", fg="#000000")
        button14.config(bg="#b5ffb5", fg="#000000")
        button15.config(bg="#b5ffb5", fg="#000000")
        button16.config(bg="#b5ffb5", fg="#000000")
        button17.config(bg="#b5ffb5", fg="#000000")
        button18.config(bg="#b5ffb5", fg="#000000")
        button19.config(bg="#b5ffb5", fg="#000000")


button = Button(win, text=themes[theme_index], font=(
    "ms ui gothic", 15), width=8, height=1, command=cycle_theme1)
button.place(x=5, y=31)
button1 = Button(win, text="", font=("ms ui gothic", 15), width=8, height=1)
button1.place(x=103, y=31)
button2 = Button(win, text="⇦", font=("ms ui gothic", 15), width=8, height=1)
button2.place(x=201, y=31)
button3 = Button(win, text="C", font=("ms ui gothic", 15), width=8, height=1)
button3.place(x=299, y=31)
button4 = Button(win, text="1", font=("ms ui gothic", 15), width=8, height=1)
button4.place(x=5, y=66)
button5 = Button(win, text="2", font=("ms ui gothic", 15), width=8, height=1)
button5.place(x=103, y=66)
button6 = Button(win, text="3", font=("ms ui gothic", 15), width=8, height=1)
button6.place(x=201, y=66)
button7 = Button(win, text="+", font=("ms ui gothic", 15), width=8, height=1)
button7.place(x=299, y=66)
button8 = Button(win, text="4", font=("ms ui gothic", 15), width=8, height=1)
button8.place(x=5, y=101)
button9 = Button(win, text="5", font=("ms ui gothic", 15), width=8, height=1)
button9.place(x=103, y=101)
button10 = Button(win, text="6", font=("ms ui gothic", 15), width=8, height=1)
button10.place(x=201, y=101)
button11 = Button(win, text="-", font=("ms ui gothic", 15), width=8, height=1)
button11.place(x=299, y=101)
button12 = Button(win, text="7", font=("ms ui gothic", 15), width=8, height=1)
button12.place(x=5, y=136)
button13 = Button(win, text="8", font=("ms ui gothic", 15), width=8, height=1)
button13.place(x=103, y=136)
button14 = Button(win, text="9", font=("ms ui gothic", 15), width=8, height=1)
button14.place(x=201, y=136)
button15 = Button(win, text="×", font=("ms ui gothic", 15), width=8, height=1)
button15.place(x=299, y=136)
button16 = Button(win, text="↲", font=("ms ui gothic", 15), width=8, height=1)
button16.place(x=5, y=171)
button17 = Button(win, text="0", font=("ms ui gothic", 15), width=8, height=1)
button17.place(x=103, y=171)
button18 = Button(win, text="·", font=("ms ui gothic", 15), width=8, height=1)
button18.place(x=201, y=171)
button19 = Button(win, text="÷", font=("ms ui gothic", 15), width=8, height=1)
button19.place(x=299, y=171)

# Main Game Loop

win.mainloop()
