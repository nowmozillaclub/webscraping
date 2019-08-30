# Wikipedia scraper by Urmil Shroff

import bs4 # imports the BeautifulSoup library for web scraping
import requests # library for making requests

res = requests.get("https://en.wikipedia.org/wiki/List_of_Google_products") # gets a link
soup = bs4.BeautifulSoup(res.text, "lxml") # cooks the soup...

title = soup.select("title") # gets the html title tag
headlines = soup.select(".mw-headline") # fetches all headlines via the class ".mw-headline"

print("Title is {}".format(title[0].text))

print("Headlines are")
for i in headlines:
    print(i.text)
