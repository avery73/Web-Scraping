from urllib.request import urlopen, Request
from bs4 import BeautifulSoup # html parser that lets you find certain tags




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'
# <div> opens and closes the tab (divider), <table> creates a table
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# he will give us header info that we don't understand (some of it)

req = Request(url, headers=headers) #!

webpage = urlopen(req).read() #!

soup = BeautifulSoup(webpage, 'html.parser') #! these three lines largely stay the same across all files

title = soup.title

print(title.text)

tablecells = soup.findAll("div", attrs={"class":"table-cell"})
# class is key, table cell is value
#print(tablecells) # prints a list of all this stuff, each element is line on Chrome
print(tablecells[0]) # what isn't in < > is our text (in this case that's 1)
print(tablecells[0].text) # prints out 1, which is a string

print()

print(tablecells[1].text)

for cell in tablecells[:7]:
    print()
    print(cell.text)
# high - low = value
# value /low x 100 = change %

#high = float(tablecells[5].text)
#low = float(tablecells[6].text)
#math = (high - low) / low * 100
#print(math) # print percent change in 1D
print()
print()

counter = 1

for x in range(5): # no value for x, just helps count
    name = tablecells[counter].text
    change = tablecells[counter+2].text
    high = float(tablecells[counter+4].text)
    low = float(tablecells[counter+5].text)

    calc_change = round(((high-low)/low) * 100, 2)

    print(name)
    print(f"% change on webpage: {change}")
    print(f"High: {high}")
    print(f"low: {low}")
    print(f"Calculated change %: {calc_change}%")
    print()
    print()

    counter += 11




		






#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

