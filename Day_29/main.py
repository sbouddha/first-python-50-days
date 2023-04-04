from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    # Delete old pass from the GUI
    password_entry.delete(0, END)
    # Insert new pass in the GUI
    password_entry.insert(0, password)

    # Copy generated password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    file_name = "data.txt"
    data = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"

    # To check if user actually enetered something:
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(
            title="Oops", message="Fields can't be empty !!!")
    else:
        with open(file_name, "a+") as data_file:
            data_file.write(data)

        # Now clear/delete the entries from the GUI
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Sid's Password Manager")
window.config(padx=35, pady=35)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)  # These values are half of above
canvas.grid(row=0, column=1)

# columnspan

# Create Lables for all
website = Label()
website.config(text="Website: ")
website.grid(row=1, column=0)

username = Label()
username.config(text="Email/Username: ")
username.grid(row=2, column=0)

password = Label()
password.config(text="Password: ")
password.grid(row=3, column=0)

# Create Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "youremail")

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# Create Buttons
gen_pass_button = Button()
gen_pass_button.config(text="Generate Password", width=14, command=gen_pass)
gen_pass_button.grid(row=3, column=2)

add_pass_button = Button()
add_pass_button.config(text="Add", width=30, command=save_data)
add_pass_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
