#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
count=0

# Loop around the data
# It will be in the format key\tval

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:   continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", float(salesTotal/count)
        oldKey = thisKey;
        salesTotal = 0
        count=0

    oldKey = thisKey
    salesTotal += float(thisSale)
    count+=1

if oldKey != None:
    print oldKey, "\t", float(salesTotal/count)