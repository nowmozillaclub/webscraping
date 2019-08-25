# Currency converter by Urmil Shroff

import bs4
import requests

res = requests.get("http://dollarrupee.in/")
soup = bs4.BeautifulSoup(res.text, "lxml")

rate = soup.select(".item-page p strong")
rupee = float(rate[0].text)

print("Today's rate: $1 = ₹{}".format(rupee))

print("What do you want to convert?")
print("1. Dollars to Rupees")
print("2. Rupees to Dollars")

choice = int(input())

if(choice == 1):
    amount = int(input("Enter amount in USD: "))
    print("Today's conversion: ${} = ₹{} (approx.)".format(
        amount, round(amount * rupee)))

elif(choice == 2):
    amount = int(input("Enter amount in INR: "))
    print("Today's conversion: ₹{} = ${} (approx.)".format(
        amount, round(amount / rupee)))

else:
    print("Bad choice!")
