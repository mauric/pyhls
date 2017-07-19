#!/usr/bin/python3

#
# This script plot all the report information from VIVADO HLS synthesis
#

import re # Support for regular expression (RE)
import matplotlib.pyplot as plt
import pylab
import os
import fnmatch
from pprint import pprint
import re


titles = {"Performance Estimates", "Utilisztion Estimates" , "Interface"} 
keywords = {"Timing", "Latency", "Detail"} # id with '+'
keyworks_sub = {"Register", "Multiplexer", "Expression", "FIFO", "Memory",
                   "DSP48", "Instance"}
## Find files in my directory
#project_dir = os.path.dirname(os.path.abspath(__file__)
fileNames = []
fileOpen = []
reg = re.compile('syn')
words = []
os.chdir("/udd/mcaceres/.workspaceviv/convhls/scripting_conv")
data_dir = "/udd/mcaceres/.workspaceviv/convhls/scripting_conv"

for root, dirnames, filenames in os.walk(data_dir):
	for filename in fnmatch.filter(filenames, '*.rpt'):
		file = os.path.join(root, filename) 
		words = file.split('/')
		if 'report' in words:
			fileNames.append(file)
			fileOpen.append(open(file, 'r'))

    
pprint(fileNames)
pprint(fileOpen)

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

#######################################
### Process Resources information 
######################################


# Total  resources used
for file in fileOpen:
	listf = file.readlines()  
	## Find differents section and extract information
	
	
	
	info = (listf[76].rstrip()).replace("|", "")

	values = [int(s) for s in info.split() if s.isdigit()]
	values_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=4)
	print (values)
	print (values_dict)
	
	latency=(listf[31].rstrip()).replace("|", "")
	latenval = [int(s) for s in latency.split() if s.isdigit()]
	latenval_dict = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
	print (latenval)
	print (latenval_dict)

#
## Total  resources used
#listf = f2.readlines()  
#info = (listf[76].rstrip()).replace("|", "")
#values = [int(s) for s in info.split() if s.isdigit()]
#values_dict2 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=6)
#print (values)
#print (values_dict2)
#latency=(listf[31].rstrip()).replace("|", "")
#latenval = [int(s) for s in latency.split() if s.isdigit()]
#latenval_dict2 = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
#print (latenval)
#print (latenval_dict2)
#
## Total  resources used
#listf = f3.readlines()  
#info = (listf[76].rstrip()).replace("|", "")
#values = [int(s) for s in info.split() if s.isdigit()]
#values_dict3 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=12)
#print (values)
#latency=(listf[31].rstrip()).replace("|", "")
#latenval = [int(s) for s in latency.split() if s.isdigit()]
#latenval_dict3 = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
#print (latenval)
#print (latenval_dict3)
#
#
## Total  resources used
#listf = f4.readlines()  
#info = (listf[76].rstrip()).replace("|", "")
#values = [int(s) for s in info.split() if s.isdigit()]
#values_dict4 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=16)
#print (values)
#print (values_dict4)
#latency=(listf[31].rstrip()).replace("|", "")
#latenval = [int(s) for s in latency.split() if s.isdigit()]
#latenval_dict4 = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
#print (latenval)
#print (latenval_dict4)
#
#
## Total  resources used
#listf = f5.readlines()  
#info = (listf[76].rstrip()).replace("|", "")
#values = [int(s) for s in info.split() if s.isdigit()]
#values_dict5 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=24)
#print (values)
#print (values_dict5)
#latency=(listf[31].rstrip()).replace("|", "")
#latenval = [int(s) for s in latency.split() if s.isdigit()]
#latenval_dict5 = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
#print (latenval)
#print (latenval_dict5)
#
## Total  resources used
#listf = f6.readlines()  
#info = (listf[76].rstrip()).replace("|", "")
#values = [int(s) for s in info.split() if s.isdigit()]
#values_dict6 = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=32)
#print (values)
#print (values_dict6)
#latency=(listf[31].rstrip()).replace("|", "")
#latenval = [int(s) for s in latency.split() if s.isdigit()]
#latenval_dict6 = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
#print (latenval)
#print (latenval_dict6)
#

########################
#   
### Plot charts.
#
########################

#plt.figure(1)
#plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"],
#values_dict3["bitwidth"],values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]],
#[values_dict["bram"], values_dict2["bram"], values_dict3["bram"],
#values_dict4["bram"],values_dict5["bram"],values_dict6["bram"], ],'ro--' )
#plt.xlabel("X label")
#plt.ylabel("Y label")
#plt.title("BRAM")
#pylab.savefig('figure1.pdf')
#
#plt.figure(2)
#plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
#values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"] ], [values_dict["dsp"],
#values_dict2["dsp"], values_dict3["dsp"],
#values_dict4["dsp"],values_dict5["dsp"],values_dict6["dsp"]],'ro--' )
#plt.xlabel("X label")
#plt.ylabel("Y label")
#plt.title("DSP")
#pylab.savefig('figure2.pdf')
#
#plt.figure(3)
#plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
#values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]  ], [values_dict["ff"],
#values_dict2["ff"], values_dict3["ff"], values_dict4["ff"],values_dict5["ff"],values_dict6["ff"]
#],'ro--' )
#plt.xlabel("X label")
#plt.ylabel("Y label")
#plt.title("FF")
#pylab.savefig('figure3.pdf')
#
#
#plt.figure(4)
#plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
#values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]  ], [values_dict["lut"],
#values_dict2["lut"], values_dict3["lut"], values_dict4["lut"],values_dict5["lut"],values_dict6["lut"]
#],'ro--' )
#plt.xlabel("X label")
#plt.ylabel("Y label")
#plt.title("LUT")
#pylab.savefig('figure4.pdf')
#
#
#plt.figure(5)
#plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
#values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]  ],
#[latenval_dict["latenmax"],
#latenval_dict2["latenmax"], latenval_dict3["latenmax"],
#latenval_dict4["latenmax"],latenval_dict5["latenmax"],latenval_dict6["latenmax"]],'ro--' )
#plt.xlabel("X label")
#plt.ylabel("Y label")
#plt.title("LATENCY")
#pylab.savefig('figure5.pdf')
#
#plt.figure(6)
#plt.plot([ values_dict["bitwidth"],values_dict2["bitwidth"], values_dict3["bitwidth"],
#values_dict4["bitwidth"],values_dict5["bitwidth"],values_dict6["bitwidth"]],
#[latenval_dict["intermax"],
#latenval_dict2["intermax"], latenval_dict3["intermax"],
#latenval_dict4["intermax"],latenval_dict5["intermax"],latenval_dict6["intermax"]],'ro--' )
#plt.xlabel("X label")
#plt.ylabel("Y label")
#plt.title("INTERVAL")
##
#pylab.savefig('figure6.pdf')
#
#
#
#
#
## Show plots
#plt.show()
##f = plt.bar(range(len(all_values)), all_values.values(), align='center')
##plt.xticks(range(len(all_values)), all_values.keys())
#
#
### Close files.
#f1.close()
#f2.close()
#f3.close()
#f4.close()
#f5.close()
#f6.close()
