# Wikipedia scraper by Urmil Shroff

import bs4
import requests
import operator

user_id = input("Enter username of the GitHub profile:\n")
user_link = "https://github.com/" + user_id

print("Fetching profile...")

res = requests.get(user_link)
soup = bs4.BeautifulSoup(res.text, "lxml")

name = soup.select(".p-name.vcard-fullname.d-block.overflow-hidden")
count = soup.select(".Counter")

contribs = soup.select(".f4.text-normal.mb-2")
contribs = contribs[1].text[:-44]

max_contribs = {}

for item in soup.findAll("rect", {"class": "day"}):
    date = item.get("data-date")
    max_contribs[date] = int(item.get("data-count"))

max_contribs = sorted(max_contribs.items(),
                      key=operator.itemgetter(1), reverse=True)

max_num = max_contribs[0][1]
max_date = max_contribs[0][0]

print("\nSummary for GitHub user {} (aka @{}):".format(name[0].text, user_id))

print("\nNumber of repositories: {}".format(count[0].text.strip()))
print("Number of projects: {}".format(count[1].text.strip()))
print("Number of starred items: {}".format(count[2].text.strip()))
print("Number of followers: {}".format(count[3].text.strip()))
print("Number of following: {}".format(count[4].text.strip()))

print("\nMost contributions in a single day: {}".format(max_num))
print("Date of most contributions: {}".format(max_date))
print("Total contributions in the last year: {}".format(contribs.strip()))
