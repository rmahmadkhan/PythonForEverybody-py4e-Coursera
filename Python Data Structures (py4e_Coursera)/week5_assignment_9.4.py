# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

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
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] = counts[words[1]] + 1
maxCount = None
maxWord = None
for word,count in counts.items():
    if maxCount is None or maxCount < count:
        maxWord = word
        maxCount = count
print(maxWord, maxCount)
