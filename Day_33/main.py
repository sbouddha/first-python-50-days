import requests
from datetime import datetime
import smtplib

my_email = "test@gmail.com"
my_password = "dfhgfdshgshgdf"

MY_LAT = 59.913868
MY_LNG = 10.752245

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(
    "http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

# Send email function


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="test@gmail.com",
                            msg="Subject : ISS Nearby\n\nLook Up")
    print("Mail Send")


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
if (MY_LAT+5 > iss_latitude > MY_LAT-5) and (MY_LNG+5 > iss_longitude > MY_LNG-5) and (time_now > 18):
    send_email()
else:
    print("It's far away")
