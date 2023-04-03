from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

random_word = None
word_meaning = None
text_id = None
image_id = None
to_learn = {}
current_card = {}

# ---------------------------Logic--------------------------------#

csv_file_loc = r"C:\Without_Sync\Py\python-100-days\Day_31\data\french_words.csv"

try:
    data = pd.read_csv("data/Words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(csv_file_loc)
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(2000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def is_known():
    to_learn.remove(current_card)

    data = pd.DataFrame(to_learn)
    data.to_csv("data/Words_to_learn.csv", index=False)

    next_card()


# ---------------------------UI Setup------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(2000, flip_card)


canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(
    file=r"C:\Without_Sync\Py\python-100-days\Day_31\images\card_front.png")
card_back_image = PhotoImage(
    file=r"C:\Without_Sync\Py\python-100-days\Day_31\images\card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))

card_word = canvas.create_text(400, 263, text=word_meaning,
                               font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


# Adding Buttons
cross_image = PhotoImage(
    file=r"C:\Without_Sync\Py\python-100-days\Day_31\images\wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(
    file=r"C:\Without_Sync\Py\python-100-days\Day_31\images\right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
