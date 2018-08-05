import tkinter


def distance_cost():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    wynik = a*b*c/100
    wynik_label.configure(text='Koszt: '+str(wynik)+'zł')


root = tkinter.Tk()
a_label = tkinter.Label(master=root, text="cena paliwa (zł/l)")
a_entry = tkinter.Entry(master=root)
a_label.pack()
a_entry.pack()

b_label = tkinter.Label(master=root, text="spalanie (l/100km)")
b_entry = tkinter.Entry(master=root)
b_label.pack()
b_entry.pack()

c_label = tkinter.Label(master=root, text="dystans (km)")
c_entry = tkinter.Entry(master=root)
c_label.pack()
c_entry.pack()


oblicz_button = tkinter.Button(master=root, text="Oblicz", command=distance_cost)
oblicz_button.pack()
wynik_label = tkinter.Label(master=root, text="Wynik")
wynik_label.pack()

root.title("Koszt podróży")
root.mainloop()