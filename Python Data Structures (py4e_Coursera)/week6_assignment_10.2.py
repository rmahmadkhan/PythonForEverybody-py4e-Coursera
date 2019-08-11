# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Cannot open file:',fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    else:
        hours = words[5].split(':')
        if hours[0] not in counts:
            counts[hours[0]] = 1
        else:
            counts[hours[0]] = counts[hours[0]] + 1
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))
lst.sort()
for val, key in lst[:]:
    print(val, key)
