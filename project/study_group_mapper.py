#!/usr/bin/python
import sys, csv, string

reader = csv.reader(sys.stdin, delimiter = '\t')
reader.next()

for line in reader:
	node_type = line[5]
	node_id = line[0]
	question_id = str(line[7])
	author_id = line[3]

	if node_type == 'question':
		print "{0}\t{1}".format(node_id, author_id)
	else:
		print "{0}\t{1}".format(question_id, author_id)		
	
