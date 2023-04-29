from bs4 import BeautifulSoup

file_path = r"C:\Without_Sync\Py\python-100-days\Day_45\website.html"

with open(file_path, encoding='utf-8') as website_data:
    contents = website_data.read()
    # print(contents)

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)

# print(soup)
# print(soup.prettify())

# print(soup.a)
all_a_tags = soup.find_all(name="a")
# print(all_a_tags)

for tag in all_a_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)
