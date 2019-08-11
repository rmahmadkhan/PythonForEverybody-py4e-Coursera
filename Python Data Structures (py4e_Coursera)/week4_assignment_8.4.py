# 8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see 
# if the word is already in the list and if not append it to the list. When the program completes, sort 
# and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

fhand = open('romeo.txt')
t = list()
for line in fhand:
    t1 = line.split()
    for i in range(len(t1)):
        if t1[i] not in t:
            t.append(t1[i])
t.sort()
print(t)
