from tkinter import *

def miles_to_kilo():
    miles= float(input_miles.get())
    km = miles * 1.609
    km_result_label.config(text=str(km))


window = Tk()
window.title("Mile to Kilo Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input_miles = Entry(width=15)
input_miles.grid(column=1 ,row=0 )

miles_label = Label(text="Miles")
miles_label.grid(column=2 ,row=0 )

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0 ,row= 1)

km_result_label = Label(text="0")
km_result_label.grid(column=1 ,row= 1)

km_label = Label(text="km")
km_label.grid(column= 2,row=1 )


calc_button =Button(text="Calculate", command=miles_to_kilo)
calc_button.grid(column=1 ,row=2 )


window.mainloop()