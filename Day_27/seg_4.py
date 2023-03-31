from tkinter import *

def button_clicked():
    # print("I got clicked")
    my_label.config(text= input.get())
    # print (input.get())

window  = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#You have to pack everything
#Label
my_label = Label(text="I am a level", font=("Arial", 15, "bold"))
my_label.config(text= "New Text")
my_label.pack() 

#Button
button = Button(text= "Click Me", command = button_clicked)
button.pack()

#Entry component (same as turtle input)
input = Entry(width=10)
input.pack()




#To Keel the window open 
window.mainloop()
