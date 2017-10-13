import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
taglist=list()
count=int(input("Enter count: "))
position=int(input("Enter position: "))
for i in range(int(count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    tags = soup('a')
    url = tags[int(position)-1].get('href',None)
print (url)
