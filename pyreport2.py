#!/usr/bin/python

#
# This script plot all the report information from VIVADO HLS synthesis
#

import re # Support for regular expression (RE)
import matplotlib.pyplot as plt



titles = {"Performance Estimates", "Utilisztion Estimates" , "Interface"} 
keywords = {"Timing", "Latency", "Detail"} # id with '+'
keyworks_sub = {"Register", "Multiplexer", "Expression", "FIFO", "Memory",
                   "DSP48", "Instance"}
fields_col = [] # To store all the fields in columns and ranks
fields_rank = [] #

fileName1 = "4bit.rpt" 
fileName2 = "6bit.rpt"
fileName3 = "12bit.rpt"
fileName4 = "16bit.rpt"
fileName5 = "24bit.rpt"
fileName6 = "32bit.rpt"

## Open files.
f1 = open(fileName1, 'r')
f2 = open(fileName2, 'r')
f3 = open(fileName3, 'r')
f4 = open(fileName4, 'r')
f5 = open(fileName5, 'r')
f6 = open(fileName6, 'r')



print (f1)
print (f2)
print (f3)
print (f4)
print (f5)
print (f6)

# Print a Table of Content of report
#print ("Table of Content")
#for line in f1:
#    if line.startswith("=========="):
#        print ("Title here")
#    if line.startswith('*'):
#        print ("    Keyword here")
#    if line.startswith('+'):
#        print ("        Subkeyword here")
#
# Rewind file and store
f1.seek(0)
listf = f1.readlines()  


# Total  resources used
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=4)
print (values)
print (values_dict)

listf = f2.readlines()  


# Total  resources used
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict2 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=6)
print (values)
print (values_dict2)

listf = f3.readlines()  

# Total  resources used
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict3 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=12)
print (values)
print (values_dict3)

listf = f4.readlines()  


# Total  resources used
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict4 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=16)
print (values)
print (values_dict4)
listf = f5.readlines()  

# Total  resources used
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict5 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=24)
print (values)
print (values_dict5)
listf = f6.readlines()  

# Total  resources used
info = (listf[76].rstrip()).replace("|", "")
values = [int(s) for s in info.split() if s.isdigit()]
values_dict6 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=32)
print (values)
print (values_dict6)

    
## Plot charts.
plt.figure(1)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"],
values_dict3["bitwidth"],values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]],
[values_dict["bram"], values_dict2["bram"], values_dict3["bram"], values_dict4["bram"],values_dict5["bram"],values_dict6["bram"], ],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("BRAM")


plt.figure(2)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"] ], [values_dict["dsp"],
values_dict2["dsp"], values_dict3["dsp"], values_dict4["dsp"],values_dict5["dsp"],values_dict6["dsp"]],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("DSP")

plt.figure(3)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]  ], [values_dict["ff"],
values_dict2["ff"], values_dict3["ff"], values_dict4["ff"],values_dict5["ff"],values_dict6["ff"] ],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("FF")


plt.figure(4)
plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]  ], [values_dict["ff"],
values_dict2["lut"], values_dict3["ff"], values_dict4["lut"],values_dict5["lut"],values_dict6["lut"] ],'ro' )
plt.xlabel("X label")
plt.ylabel("Y label")
plt.title("LUT")
#







# Show plots
plt.show()
#f = plt.bar(range(len(all_values)), all_values.values(), align='center')
#plt.xticks(range(len(all_values)), all_values.keys())


## Close files.
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
