# Edit it to your requirement :)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_265045.html'
html =  urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retriving all of the anchor tags
tags = soup('span')
lst = list()
count = 0
for tag in tags:
    lst.append(tag.contents[0])
    count = count + 1
for num in range(len(lst)):
    lst[num] = int(lst[num])
total = sum(lst)
print(total)
