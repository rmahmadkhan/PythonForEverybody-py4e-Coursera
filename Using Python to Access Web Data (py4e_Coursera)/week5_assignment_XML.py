import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter url - ')
data = urllib.request.urlopen(url).read()

stuff = ET.fromstring(data)
counts = stuff.findall('.//count')
nums = list()
for count in counts:
    nums.append(count.text)
for num in range(len(nums)):
    nums[num] = int(nums[num])
total = sum(nums)
print(total)
