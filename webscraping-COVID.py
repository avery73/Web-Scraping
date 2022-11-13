# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers) #!

webpage = urlopen(req).read() #!

soup = BeautifulSoup(webpage, 'html.parser') #! these three lines largely stay the same across all files

table_rows = soup.findAll("tr")

state_worst_death = ''
state_best_death = ''
high_death_ratio = 0.0
low_death_ratio = 100.0

state_best_test = ''
state_worst_test = ''
high_test_ratio = 0.0
low_test_ratio = 100.0

for row in table_rows[2:51]:
    td = row.findAll("td")
    state = td[1].text
    total_cases = int(td[2].text.replace(",",""))
    total_deaths = int(td[4].text.replace(",",""))
    total_test = int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))

    death_rate = round((total_deaths / total_cases) * 100, 2)
    test_rate = round((total_test / population) * 100, 2)

    print(state)
    print(f"Death Rate: {death_rate}%")
    print(f"Test Rate: {test_rate}%")

    if death_rate > high_death_ratio:
        state_worst_death = state
        high_death_ratio = death_rate

    if death_rate < low_death_ratio:
        state_best_death = state
        low_death_ratio = death_rate

    if test_rate > high_test_ratio:
        state_best_test = state
        high_death_ratio = test_rate

    if test_rate < low_test_ratio:
        state_worst_test = state
        low_test_ratio = test_rate

print()
print()

print(f"state with worst death rate: {state_worst_death}")
print(f"death rate: {high_death_ratio}%")
print()
print(f"state with best death rate: {state_best_death}")
print(f"death rate: {low_death_ratio}%")
print()
print(f"state with worst test rate: {state_worst_test}")
print(f"test rate: {low_test_ratio}%")
print()
print(f"state with best test rate: {state_best_test}")
print(f"test rate: {high_test_ratio}%")


# need to use rstrip to take away commas that are in between all the numbers on the website - python can't do anything when the commas are there!!!

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

'''

table = table

thead
/thead = these are the headers

tr = each row
    td california td  = each cell in each row
    td .......... td
tr

/table

each of these is written with <tr>

'''