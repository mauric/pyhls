#!/usr/bin/python

#
# This script plot all the report information from VIVADO HLS synthesis
#

import re # Support for regular expression (RE)




titles = {"Performance Estimates", "Utilisztion Estimates" , "Interface"} 
keywords = {"Timing", "Latency", "Detail"} # id with '+'
keyworks_sub = {"Register", "Multiplexer", "Expression", "FIFO", "Memory",
                   "DSP48", "Instance"}
fields_col = [] # To store all the fields in columns and ranks
fields_rank = [] #

fileName1 = "file1.rpt" 
fileName2 = "file2.rpt"


## Open files.
f1 = open(fileName1, 'r')
print f1
f2 = open(fileName2, 'r')
print f2

for line in f1:
    if line.startswith("=========="):
        print ("Title here")
    if line.startswith('*'):
        print ("    Keyword here")
    if line.startswith('+'):
        print ("        Subkeyword here")

# Rewind file and store
f1.seek(0)
listf = f1.readlines()  


# Extract some dummy information to test string methods
index = listf[72].rfind("Utilization Estimates")
info = (listf[72].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3])
print (values)
print (values_dict)

## Close files.
f1.close()
f2.close()
