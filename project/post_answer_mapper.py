#!/usr/bin/python
import sys, csv, string

reader = csv.reader(sys.stdin, delimiter = '\t')
reader.next()

for line in reader:
	node_type = line[5]
	body = line[4]
	body_len = len(body)
	node_id = line[0]
	question_id = str(line[7])
	if node_type == 'question':
		print '{0}\t{1}\t{2}'.format(node_id, 'A', body_len)

	if node_type == 'answer':
		print '{0}\t{1}\t{2}'.format(question_id,'B',body_len)	
