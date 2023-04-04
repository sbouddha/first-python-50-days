Today we will learn about **Sending Emails with Python**


# SMTP : Simple Mail Transfer Protocol
```python

import smtplib

my_email = "youremail@gmail.com"
password = "yourapppass"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="yourfrindsemail@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email")

```