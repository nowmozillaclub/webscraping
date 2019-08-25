# Wikipedia scraper by Urmil Shroff

import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/List_of_Google_products")
soup = bs4.BeautifulSoup(res.text, "lxml")

title = soup.select("title")
headlines = soup.select(".mw-headline")

print("Title is {}".format(title[0].text))

print("Headlines are")
for i in headlines:
    print(i.text)
