from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#EA5455"
RED = "#e7305b"
GREEN = "#539165"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER RESET")
    checkmark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60    

    #Decide on breaks on the basis of reps 
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="LONG BREAK", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="FOCUS TIME", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    count_sec = count % 60
    #Handling the prefix 0 scenario like 01:09 etc
    if count_min <10:
        count_min = f"0{count_min}"
    if count_sec <10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")

    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmark_label.config(text=marks)          


# ---------------------------- UI SETUP ------------------------------- #

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

#Label for Timer
timer_label = Label()
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW ,font=(FONT_NAME, 28, "bold"))
timer_label.grid(row=0, column=1)

#Label for Checkmark
checkmark_label = Label()
checkmark_label.config(fg=GREEN, bg=YELLOW ,font=(FONT_NAME, 10, "bold"))
checkmark_label.grid(column=1, row=3)


#Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.config(font=(FONT_NAME, 14, "bold"))
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.config(font=(FONT_NAME, 14, "bold"))
reset_button.grid(row=2, column=2)





window.mainloop()
