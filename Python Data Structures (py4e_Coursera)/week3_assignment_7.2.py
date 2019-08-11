# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit()
count = 0
total = float(0)
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')
        num = float(line[pos+2:pos+8])
        total = total + num
avg = total/count
print('Average spam confidence:',avg)
