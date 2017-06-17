#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')

oldID, oldBody  = None, None
total, count = 0, 0

#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
oldID, oldQLen, oldALen = None,0,0
count = 0

for line in reader:

	if len(line) != 3: continue

	thisID, Type, thisLength = line
	if oldID and oldID != thisID:
		length = 0 if count == 0 else oldALen/count
		print "{0}\t{1}\t{2}".format(oldID, oldQLen, length)
		oldALen,count = 0,0
	oldID = thisID
	if Type == 'A':
		oldQLen = int(thisLength)
	elif Type == 'B':
		oldALen += float(thisLength)
		count += 1
if oldID != None:
	length = 0 if count == 0 else oldALen/count
	print oldID, '\t', oldQLen,'\t',length
