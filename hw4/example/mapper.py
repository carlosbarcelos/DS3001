#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words: 
        print '%s\t%s' % (word, "1")
