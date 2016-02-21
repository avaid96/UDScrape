from bs4 import BeautifulSoup
import csv
import webbrowser
import urllib
import sys

if len(sys.argv) != 2:
    print('Usage: python udscrape.py [word] -> meaning or -1 if not found')
    sys.exit()

opener = urllib.FancyURLopener({})
word= sys.argv[1]

url="http://www.urbandictionary.com/define.php?term="+word

openerFile = opener.open(url)
htmlFile = openerFile.read()
# print htmlFile
soup = BeautifulSoup(htmlFile,"html.parser")
meanings = soup.find_all("div", "meaning")
meaning = str(meanings[0])
# print meaning

meaning=meaning[22:]
meaning=meaning[:-7]
notfound="There aren't any definitions"
if(notfound in meaning):
	print -1
else:
	print meaning

#<div class>nice, angel, perfect,etc. etc. etc....</div>
