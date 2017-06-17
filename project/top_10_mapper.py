#!/usr/bin/python
import sys, csv, string

reader = csv.reader(sys.stdin, delimiter = '\t')
reader.next()


for line in reader:
	node_type = line[5]
	if node_type == 'question':
		tags = line[2].split()
		for tag in tags:
			print "{0}\t{1}".format(tag,1)
	
	#if node_type == 'answer':
	
