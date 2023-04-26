from tkinter import *


def miles_to_km():
    num_miles = float(input.get())
    km = round(num_miles * 1.609)
    return resultado.config(text=km)


# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

# Input Text
input = Entry(width=10)
input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label equal
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Label Resultado
resultado = Label(text="0")
resultado.grid(column=1, row=1)

# Label Km
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()
