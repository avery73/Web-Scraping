import random
from urllib.request import urlopen
from bs4 import BeautifulSoup # soup is html parser
from urllib.request import urlopen, Request

import keys2
from twilio.rest import Client

# https://ebible.org/asv/JHN01.htm

random_chapter = random.randint(1,21)

if random_chapter < 10:
    random_chapter = "0" + str(random_chapter) # adds zero to url
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + ".htm"
print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

# text verses belong to parent tag, not child tags (because span open and closes)

page_verses = soup.findAll('div',class_='main')

verse_list = []

for verse in page_verses:
    #print(verse.text) # whole thing prints as text
    verse_list = verse.text.split(".") # period separates the verses

#print(verse_list) # this all only gets us one paragrah at a time

#print(random.choice(verse_list[:len(verse_list)-2])) # that fancy part at the end removes the footers and copyright

myverse = "Chapter: " + random_chapter + " Verse:" + random.choice(verse_list[:len(verse_list)-2])
print(myverse)

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = "+14633454656"
myCellphone = '+12148018262'

textmsg = client.messages.create(to=myCellphone,from_=TwilioNumber,body=myverse)
print(textmsg.status)
