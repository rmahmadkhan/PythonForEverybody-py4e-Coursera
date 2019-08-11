# Edit it to your requirements :)

import re
fhand = open("regex_sum_265043.txt")
lst = list()
for line in fhand:
    y = re.findall('[0-9]+',line)
    lst.extend(y)
for digit in range(len(lst)):
    lst[digit] = int(lst[digit])
total = sum(lst)
print(total)
