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

oldID, oldBody  = None, None
total, count = 0, 0

for line in reader:
	if len(line) != 3: continue
	thisID, thisBody, thisAns = line
	
	if oldID and oldID != thisID:
		print oldID,'\t',oldBody,'\t',total/float(count)
		total, count = 0, 0
	oldID = thisID
	oldBody = thisBody
	count += 1
	total += int(thisAns)

if oldID != None:
	print oldID, '\t', oldBody, '\t', total/float(count)
