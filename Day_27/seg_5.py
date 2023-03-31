from tkinter import *

def button_clicked():
    # print("I got clicked")
    my_label.config(text= input.get())
    # print (input.get())

window  = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Using GRID now

#Label
my_label = Label(text="I am a level", font=("Arial", 15, "bold"))
my_label.config(text= "New Text")
my_label.grid(column=0, row=0)

#New Button
new_button = Button(text="Button-2")
new_button.grid(column=2, row=0)

#Button
button = Button(text= "Click Me", command = button_clicked)
button.grid(column=1, row=1)

#Entry component (same as turtle input)
input = Entry(width=10)
input.grid(column=3, row=3)



#To Keel the window open 
window.mainloop()
