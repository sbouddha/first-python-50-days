# JSON
# JavaScript Object Notation

# Inbuild JSON Libraries

# Write : json.dump()
# Read : json.load()
# Update : json.update()

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

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
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password

        }
    }

    # data = f"{website} | {email} | {password}\n"
    # we will use the json file now , instead of data text file

    # To check if user actually enetered something:
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(
            title="Oops", message="Fields can't be empty !!!")
    else:
        try:
            # To try checking if the file exists
            with open("data.json", "r") as data_json_file:
                data = json.load(data_json_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_json_file:
                json.dump(new_data, data_json_file, indent=4)

        else:
            # Update the old json file
            data.update(new_data)

            with open("data.json", "w") as data_json_file:
                # Write in the file
                json.dump(data, data_json_file, indent=4)

        finally:
            # Now clear/delete the entries from the GUI
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------- PASSWORD SEARCH ----------------------------- #


def find_password():
    search_text = website_entry.get()

    try:
        with open("data.json") as pass_data_file:
            pass_dict = json.load(pass_data_file)
        found_email = pass_dict[search_text]["email"]
        found_pass = pass_dict[search_text]["password"]

    except FileNotFoundError:
        messagebox.showerror(
            title="Error", message=f"Password Json file not found")

    except KeyError:
        messagebox.showerror(
            title="Error", message=f"No Password Details found for {search_text}")

    else:
        messagebox.showinfo(title="Password/Website Details",
                            message=f"{found_email}\n{found_pass}")


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
website_entry = Entry(width=25)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "test.email@gmail.com")

password_entry = Entry(width=25)
password_entry.grid(row=3, column=1)

# Create Buttons
gen_pass_button = Button()
gen_pass_button.config(text="Generate Password", width=14, command=gen_pass)
gen_pass_button.grid(row=3, column=2)

add_pass_button = Button()
add_pass_button.config(text="Add", width=36, command=save_data)
add_pass_button.grid(row=4, column=1, columnspan=2)

search_button = Button()
search_button.config(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)


window.mainloop()
