#!/usr/bin/env python
import sys
 
#--- get all lines from stdin ---
for line in sys.stdin:
    line = line.strip()
    value = line.split()
    #print '%s\t%s' % (value[0], "1") # value[0] = VoterID
    print '%s\t%s' % (value[1], "1") # value[1] = CountryID
    #print '%s\t%s' % (value[2], "1") # value[2] = PartyID
    #print '%s\t%s' % (value[1] + " " + value[2], "1") # Country per party
