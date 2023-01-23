import tkinter 

# Vytvoření okna pro kalkulačku
window = tkinter.Tk()
window.title("Kalkulačka")

# Vytvoření zobrazovacího pole pro výsledky
display = tkinter.Entry(window, width=35, bg="#EEE")
display.grid(row=0, column=0, columnspan=5)

# Funkce pro zpracování tlačítek
def press(num):
    """Zobrazí zadanou hodnotu na kalkulačce"""
    current = display.get()
    display.delete(0, tkinter.END)
    display.insert(0, str(current) + str(num))

def equal():
    """Vypočítá výsledek zadaného výrazu na kalkulačce"""
    result = eval(display.get())
    display.delete(0, tkinter.END)
    display.insert(0, result)

def clear():
    """Vymaže zobrazovací pole na kalkulačce"""
    display.delete(0, tkinter.END)


# Vytvoření tlačítek pro číslice
button_1 = tkinter.Button(window, text="1", width=10, command=lambda: press(1))
button_2 = tkinter.Button(window, text="2", width=10, command=lambda: press(2))
button_3 = tkinter.Button(window, text="3", width=10, command=lambda: press(3))
button_4 = tkinter.Button(window, text="4", width=10, command=lambda: press(4))
button_5 = tkinter.Button(window, text="5", width=10, command=lambda: press(5))
button_6 = tkinter.Button(window, text="6", width=10, command=lambda: press(6))
button_7 = tkinter.Button(window, text="7", width=10, command=lambda: press(7))
button_8 = tkinter.Button(window, text="8", width=10, command=lambda: press(8))
button_9 = tkinter.Button(window, text="9", width=10, command=lambda: press(9))
button_0 = tkinter.Button(window, text="0", width=10, command=lambda: press(0))

# Vytvoření tlačítek pro operace
button_add = tkinter.Button(window, text="+", width=10, command=lambda: press("+"))
button_subtract = tkinter.Button(window, text="-", width=10, command=lambda: press("-"))
button_multiply = tkinter.Button(window, text="*", width=10, command=lambda: press("*"))
button_divide = tkinter.Button(window, text="/", width=10, command=lambda: press("/"))
button_equal = tkinter.Button(window, text="=", width=10, command=equal)
button_clear = tkinter.Button(window, text="AC", width=10, command=clear)


# Umístění tlačítek do okna
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)

# Spuštění okna s kalkulačkou
window.mainloop()