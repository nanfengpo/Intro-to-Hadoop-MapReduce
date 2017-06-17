#!/usr/bin/python
import sys, csv, string

reader = csv.reader(sys.stdin, delimiter = '\t')
reader.next()

question = {}
answer = {}

for line in reader:
	node_type = line[5]
	body = line[4]
	body_len = len(body)
	node_id = line[0]
	question_id = str(line[7])
	if node_type == 'question':
		question[node_id] = body_len
	
	if node_type == 'answer':
		if not question_id in answer:
			answer[question_id] = [body_len]
		else:
			answer[question_id].append(body_len)

#print out the answer length for each
for id in question:
	if not id in answer:
		print "{0}\t{1}\t{2}".format(int(id), int(question[id]),'0')
	else:
	    for length in answer[id]:
		print "{0}\t{1}\t{2}".format(int(id),int(question[id]), length)
