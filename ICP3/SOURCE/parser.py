import requests
from bs4 import BeautifulSoup
import urllib.request

html_page = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
soup = BeautifulSoup(html_page.text, "html.parser")

print(soup.title.string)

for i in soup.find_all('a'):
    print(i.get('href'))

