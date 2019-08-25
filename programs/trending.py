import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://github.com/trending'
r = requests.get(URL)
date = datetime.datetime.now()

soup = BeautifulSoup(r.content, 'html5lib')

print("The Trending GitHub Repositories as of " + date.strftime("%c") + " are:")

h1Containers = soup.findAll('h1', attrs={'class': 'h3 lh-condensed'})

for container in h1Containers:
    print(container.a.text.replace('\n', ''))
