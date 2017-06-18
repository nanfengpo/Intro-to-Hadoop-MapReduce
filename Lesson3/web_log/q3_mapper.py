#!/usr/bin/python

#Extract the hits for each different file on the Web site

#Common Log Format:
#Input file Example:
#10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
#10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
#

import sys
import re

p = re.compile('.*".*\s+(/.*)\s+.*".*')

for line in sys.stdin:
    data = p.match(line.replace("http://","").replace("www.","").replace("the-associates.co.uk",""))
    if data:
	print "{0}\t{1}".format(data.groups()[0],1)
