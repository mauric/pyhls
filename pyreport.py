#!/usr/bin/python

#
# This script plot all the report information from VIVADO HLS synthesis
#
# This script has been written in Python3 
#

## import re # Support for regular expression (RE)
import matplotlib.pyplot as plt
import sys

titles = {"Performance Estimates", "Utilisztion Estimates" , "Interface"} 
keywords = {"Timing", "Latency", "Detail"} # id with '+'
keyworks_sub = {"Register", "Multiplexer", "Expression", "FIFO", "Memory",
                   "DSP48", "Instance"}
fields_col = [] # To store all the fields in columns and ranks
fields_rank = [] #

# Extract argument from command line
fileName1 = sys.argv[1]
fileName2 = sys.argv[2]
fileName3 = sys.argv[3]
print (fileName1, fileName2, fileName3)

# List file names only for test.
#ffileName1 = "file1.rpt" 
#ffileName2 = "file2.rpt"
#ffileName3 = "file3.rpt"

## Open files.
f1 = open(fileName1, 'r')
f2 = open(fileName2, 'r')
f3 = open(fileName3, 'r')
print (f1,f2,f3)


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
listf2 = f2.readlines()
listf3 = f3.readlines()

## Extract some information using line number. 
# Total  resources used
info = (listf[72].rstrip()).replace("|", "")
info2 = (listf2[72].rstrip()).replace("|", "")
info3 = (listf3[72].rstrip()).replace("|", "")


# Values of bitdwith only for test, TODO extract this information
bw1 = 32 
bw2 = 24
bw3 = 16 

# Extract values of resources used and stored in a dictionary.
values = [int(s) for s in info.split() if s.isdigit()]
values_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=bw1)

values2 = [int(s) for s in info2.split() if s.isdigit()]
values_dict2 = dict(bram=values2[0], dsp=values2[1],ff=values2[2], lut=values2[3], bitwidth=bw2)

values3 = [int(s) for s in info3.split() if s.isdigit()]
values_dict3 = dict(bram=values3[0], dsp=values3[1],ff=values3[2], lut=values3[3], bitwidth=bw3)


## Plot charts.
plt.figure(1)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"]], [values_dict["bram"], values_dict2["bram"], values_dict3["bram"]],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")


plt.figure(2)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"]], [values_dict["dsp"], values_dict2["dsp"], values_dict3["dsp"]],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")


plt.figure(3)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"]], [values_dict["ff"], values_dict2["ff"], values_dict3["ff"]],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")

# Show plots
plt.show()
#f = plt.bar(range(len(all_values)), all_values.values(), align='center')
#plt.xticks(range(len(all_values)), all_values.keys())


# Rsc Utilization %

## Close files.
f1.close()
f2.close()
f3.close()
