import tkinter


def sumuj_elementy():
    a = float(a_entry.get())
    b = float(b_entry.get())
    wynik = a + b
    wynik_label.configure(text=str(wynik))


root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="element a")
a_entry = tkinter.Entry(master=root)
a_label.pack()
a_entry.pack()

b_label = tkinter.Label(master=root, text="element b")
b_entry = tkinter.Entry(master=root)
b_label.pack()
b_entry.pack()

sumuj_button = tkinter.Button(master=root, text="Sumuj", command=sumuj_elementy)
sumuj_button.pack()
wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()

root.title("Sumator")
root.mainloop()



