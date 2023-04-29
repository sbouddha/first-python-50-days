from bs4 import BeautifulSoup
import requests
import certifi


date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(
    "https://www.billboard.com/charts/hot-100/" + date, verify=certifi.where())

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(
    "span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]
