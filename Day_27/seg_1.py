import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text = "I am a Label", font=("Arial",20,"bold"))
my_label.pack(expand=True) # To show/keep things inside the screen 

my_label["text"] = "New Text"
my_label.config(text= "New Text")

#Button

button = tkinter.Button()









#To Keel the window open 
window.mainloop()