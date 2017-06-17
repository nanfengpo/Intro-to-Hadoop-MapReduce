#!/usr/bin/python

'''
#cat ../data/ud_forum/forum_node.tsv | python top_10_mapper.py | sort | python top_10_reducer.py
The result

cs101	11622
cs373	4952
cs253	4542
discussion	3560
meta	2664
cs212	2009
homework	1682
bug	1651
cs262	1561
st101	1489

and 
#hadoop fs -cat output/part-00000

cs101	11622
cs373	4952
cs253	4542
discussion	3560
meta	2664
cs212	2009
homework	1682
bug	1651
cs262	1561
st101	1489
'''


import sys, csv, string

oldKey = None
total = 0

import Queue as Q
q = Q.PriorityQueue()


for line in sys.stdin:
	data = line.strip().split('\t')
	
	if len(data) != 2: 
		continue
	
	thisKey, thisValue =  data
	if oldKey and oldKey != thisKey:
		if len(q.queue) < 10:
			q.put((total, oldKey))
		else:
			if total > q.queue[0][0]:
				q.get()
				q.put((total, oldKey))
		total = 0
	oldKey = thisKey
	total += 1
res = []

if oldKey:
	if len(q.queue) < 10:
		q.put((total, oldKey))
	else:
		if total > q.queue[0][0]:
			q.get()
			q.put((total, oldKey))

#get all item  from queue in ascending order
while not q.empty():
	res.insert(0,q.get())

for item in res:	
	print "{0}\t{1}".format(item[1], item[0])
