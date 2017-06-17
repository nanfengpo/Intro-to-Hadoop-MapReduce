#!/usr/bin/python

import sys

oldKey = None
id = []

for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 2:
		continue
	
	thisKey, thisID = data
	
	if oldKey and oldKey != thisKey:
		print oldKey, '\t', id
		id = []

	oldKey = thisKey
	id = id + [thisID]	 
if oldKey != None:
	print oldKey, '\t', id
