Today, we will make **Pomodoro Timer** using *Tkinter* and *canvas*.


```
window = Tk()
window.title("Bouddha's Pomodoro")
window.minsize(width=450, height=380)
window.config(padx=60, pady=10, bg=YELLOW)


#Important
window.after(1000, )

#Canvas is very important
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img )
timer_text = canvas.create_text(102,130, text= "00:00", fill="white", font=(FONT_NAME, 28 ,"bold"))
canvas.grid(row=1, column=1)
```