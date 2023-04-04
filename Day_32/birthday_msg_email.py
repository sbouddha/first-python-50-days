import datetime as dt
import pandas as pd
import random
import smtplib


# Defining variables
letter_path = r"C:\Without_Sync\Py\python-100-days\Day_32\Birthday_Wish_Hard\letter_templates"
my_email = "test@gmail.com"
my_password = "kdkdhdhsgshg"

# 2. Check if today matches a birthday in the birthdays.csv

# Create a tuple from todays month and date
today = dt.datetime.now()
today_tuple = (today.month, today.day)
print(today_tuple)

# read the csv using pandas
data = pd.read_csv("birthdays.csv")

# HINT 2: You could create a dictionary from birthdays.csv that looks like this:

# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

# to make as below, we need to use te Dictionary Comprehension
# birthdays_dict = {new_key: new_value for (index, data_row) in data.iterrows()}

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)


# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    random_num = random.randint(1, 3)
    letter = f"{letter_path}/letter_{random_num}.txt"

    with open(letter) as letter_file:
        letter_content = letter_file.read()
        letter_content = letter_content.replace(
            "[NAME]", birthdays_person["name"])
        print(letter_content)

    # now send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject : Happy Birthday my Friend :)\n\n{letter_content}")
