#!/usr/bin/python

#
# This script plot all the report information from VIVADO HLS synthesis
#

## import re # Support for regular expression (RE)
import matplotlib.pyplot as plt



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

# Print a Table of Content of report
print ("Table of Content")
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


## Extract some dummy information to test string methods.
# Total  resources used
index = listf[58].rfind("Utilization Estimates")
info = (listf[72].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3])
print (values)
print (values_dict)

# Available Resouces
info = (listf[74].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_rsc_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3])
print (values)
print (values_rsc_dict)

# Utilisation
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_percente_rsc_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3])
print (values)
print (values_percente_rsc_dict)

## Plot.
plt.bar(range(len(values_dict)), values_dict.values(), align='center')
plt.xticks(range(len(values_dict)), values_dict.keys())

plt.show()


## Close files.
f1.close()
f2.close()
