from tkinter import *

def main():
    window = Tk()
    window.title("// Measurement Converter \\\\")
    window.minsize(width=400, height=100)
    window.config(padx=80, pady=20)
    

    first_measurement = Entry(width=8)
    label_first = Label(text="Miles")
    label_is_equal = Label(text="is equal to")
    label_second = Label(text="Km")
    label_result = Label(text="0")
    button_convert = Button(text="Convert", command=lambda: mile_to_km(first_measurement, label_result))
    

    first_measurement.grid(row=1, column=5)
    label_first.grid(row=1, column=7)
    label_is_equal.grid(row=3, column=3)
    label_second.grid(row=3, column=7)
    label_result.grid(row=3, column=5)
    button_convert.grid(row=5, column=5)

    window.mainloop()


def mile_to_km(mile, label):
    mile = float(mile.get())
    label["text"] = f"{(mile * 1.609344):.2f}"

if __name__ == "__main__":
    main()