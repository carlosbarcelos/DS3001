#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
    #Pass only the words that are palindromes
        if word == word[::-1]:
            print '%s\t%s' % (word, "1")
