from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=25, pady=25)
# window.wm_attributes('-toolwindow', 'True')

in_km=0

#Putting all functions here
#create function in km
def miles_to_km():
    global in_km
    in_miles = float(entry.get())
    in_km = (in_miles)*1.609
    value_in_km.config(text=in_km)

#Functions end here

# Label
miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label()
km_label.config(text="Km")
km_label.grid(row=1, column=2)

equal_label = Label()
equal_label.config(text="is equal to ")
equal_label.grid(row=1, column=0)


# Button
calc_button = Button()
calc_button.config(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

# Entry
entry = Entry(width=10)
entry.grid(row=0, column=1)

#Show Km
value_in_km=Label()
value_in_km.grid(row=1, column=1)



window.mainloop()
