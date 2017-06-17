#!/usr/bin/python
import sys
import csv

def max_author_hour(hour_range):
	for hour, count in enumerate(hour_range):
		if count == max(hour_range):
			print oldKey,"\t",hour	

writer = csv.writer(sys.stdout, delimiter='\t')

hour_range = [0]*24
oldKey = None

for line in sys.stdin:
	data = line.strip().split('\t')
	# to check if it is part of forum usr
	if len(data) != 2:
		continue
	
	thisKey, thisValue = data

	if oldKey and oldKey != thisKey:
		max_author_hour(hour_range)
		hour_range = [0]*24
	
	oldKey = thisKey
	hour_range[int(thisValue)] += 1
if oldKey != None:
	max_author_hour(hour_range)
