#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter = '\t')
writer = csv.writer(sys.stdout, delimiter = '\t')
reader.next()
for line in reader:
	if len(line) == 19:
		hour = int(line[8][11:13])
		author_id = line[3]
		writer.writerow([author_id] + [hour])
