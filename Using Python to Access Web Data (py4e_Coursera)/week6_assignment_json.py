import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = input('Enter url - ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
# http://py4e-data.dr-chuck.net/comments_265048.json
# http://py4e-data.dr-chuck.net/comments_42.json

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('User count:', len(info))
lst = list()
lst.extend(info['comments'])
total = 0
for item in lst:
    total = total + int(item['count'])
print('Total', total)
