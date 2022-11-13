
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
#import openpyxl as xl
#from openpyxl.styles import Font

#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)        

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
print()

movie_rows = soup.findAll('tr')

for x in range(1,6):
    td = movie_rows[x].findAll('td')
    rank = td[0].text
    name = td[1].text
    release_date = td[8].text
    dist = td[9].text.strip("\n")
    total_gross = td[5].text.replace(",","").replace("$","").strip("\n")
    total_gross = float(total_gross)
    
    theater = td[6].text.replace(",","")
    theather = float(theater)
    avg_theater = float(total_gross) / float(theater)
    print(f"{rank}. {name}")
    print(f"Release Date: {release_date}")
    print(f"Distributor: {dist}")
    total_gross = format(total_gross, ",.2f")
    print(f"Total Gross: ${total_gross}")
    print(f"Number of Theaters: {theater}")
    avg_theater = format(avg_theater, ",.2f")
    print(f"Average Revenue Per Theater: ${avg_theater}")
    print()


# DO TOTAL GROSS / THEATER = AVG REV FOR THEATER
# NEED TO GET RID OF COMMAS AND ALL THAT FOR MATH

# rank, release, total gross, distributor
