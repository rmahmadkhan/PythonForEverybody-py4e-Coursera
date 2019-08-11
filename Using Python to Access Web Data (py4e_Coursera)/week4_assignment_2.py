# Edit it to your requirement :)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

url = input('Enter url -')
count = input('Enter count -')
count = int(count)
pos = input('Enter position -')
pos = int(pos)
for repeat in range(count):
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')

    url = tags[pos-1].get('href', None)
lst = re.findall('known_by_(.+).html',url)
print(lst[0])
