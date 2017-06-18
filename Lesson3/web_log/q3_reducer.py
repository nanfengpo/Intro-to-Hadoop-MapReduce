#!/usr/bin/python

import sys

mostHits=0
totalHits=0
mostPop=None
oldKey=None

for line in sys.stdin:
	data_mapped = line.strip().split('\t')
	if len(data_mapped) !=2 :
 		continue
	thisKey, hit = data_mapped
	if oldKey and oldKey != thisKey:
		if totalHits > mostHits:
			mostPop = oldKey
			mostHits = totalHits
		totalHits = 0
	oldKey = thisKey
	totalHits += float(hit)

if mostPop:
	print mostPop,"\t",mostHits
