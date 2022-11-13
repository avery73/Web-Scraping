from urllib.request import urlopen, Request
from bs4 import BeautifulSoup # html parser that lets you find certain tags
import keys2
from twilio.rest import Client

url = 'https://coincost.net/en/currencies'
#url = 'https://www.coinmarketsnews.com/'

# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers) #!

webpage = urlopen(req).read() #!

soup = BeautifulSoup(webpage, 'html.parser') #! these three lines largely stay the same across all files

table_rows = soup.findAll("tr")

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+14633454656"
myCellphone = '+12148018262'

for row in table_rows[1:6]:
    td = row.findAll("td")
    name = td[0].text.replace("Buy / Sell","").rstrip("\n")
    print(name)

    sep = "\n"
    p = row.findAll("p")
    price = p[0].text
    price = price.split(sep, 1)[0]
    price = float(price)
    print(f"Price: ${round(price,2)}")

    change = (td[2].text.replace("%",""))
    change = float(change)
    print(f"Percent Change in 24 Hours {round(change,2)}%")

    if change > 0:
        change_new = (100 + change) / 100
        pos = price / change_new
        print(f"Corresponding Price: ${round(pos,5)}")

    if change < 0:
        change_new = (100 - abs(change)) / 100
        neg = price / change_new
        print(f"Corresponding Price: ${round(neg,2)}")

for row in table_rows[1:2]:
    td = row.findAll("td")
    bitcoin = td[0].text.replace("Buy / Sell","").strip("\n")
    sep = "\n"
    p = row.findAll("p")
    price = p[0].text
    price = price.split(sep, 1)[0]
    price = float(price)
    if price < 40000:
        textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body="Bitcoin fell below $40,000")

for row in table_rows[2:3]:
    td = row.findAll("td")
    bitcoin = td[0].text.replace("Buy / Sell","").strip("\n")
    sep = "\n"
    p = row.findAll("p")
    price = p[0].text
    price = price.split(sep, 1)[0]
    price = float(price)
    if price < 3000:
        textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body="Ethereum fell below $3,000")
