#!/usr/bin/python3

#
# This script plot all the report information from VIVADO HLS synthesis
#
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import re # Support for regular expression (RE)
import matplotlib.pyplot as plt
import pylab
import os
import fnmatch
from pprint import pprint
import re
import numpy as np

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
#os.chdir("/udd/mcaceres/.workspaceviv/convhls/scripting_conv")
#data_dir = "/udd/mcaceres/.workspaceviv/convhls/scripting_conv"
data_dir = "./"
for root, dirnames, filenames in os.walk(data_dir):
	for filename in fnmatch.filter(filenames, '*.rpt'):
		file = os.path.join(root, filename) 
		words = file.split('/')
		if 'report' in words:
			fileNames.append(file)
			fileOpen.append(open(file, 'r'))
		elif 'data' in words:
			fileNames.append(file)
			fileOpen.append(open(file, 'r'))
 
pprint(fileNames)
pprint(fileOpen)

resources = []
latency = []
resources_utilization = []
timing = []
file_index = 0
file_index_x = 0
for file in fileOpen:
	
	# Resources
	listf = file.readlines()
	info = (listf[76].rstrip()).replace("|", "")
	values = [int(s) for s in info.split() if s.isdigit()]
	resources.append(dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=[int(s) for s in re.findall(r'\d+',fileNames[file_index])][0]))
	pprint (resources)
	file_index = file_index + 1

	# Resources Utilization
	info = (listf[80].rstrip()).replace("|", "")
	values = [int(s) for s in info.split() if s.isdigit()]
	resources_utilization.append(dict(bram=values[0], dsp=values[1],ff=values[2],
	lut=values[3],bitwidth=[int(s) for s in re.findall(r'\d+',fileNames[file_index_x])][0]))
	pprint (resources_utilization)
	file_index_x = file_index_x + 1


        #Latency	
	info = (listf[31].rstrip()).replace("|", "")
	print(info)
	values = [int(s) for s in info.split() if s.isdigit()]
	latency.append(dict(latenmin=values[0],latenmax=values[1],intermin=values[2],intermax=values[3]))
	pprint(latency)
	
	#Timing
	info = (((listf[22].rstrip()).replace("|", "")).replace("ap_clk","")).rstrip()
	print(info)
	values = re.findall('([\d.]+)', info)
	print(values)
	timing.append(dict(target=values[0], estimates = values[1], uncertainty = values[2]))
	pprint(timing)
	file.close()

bw = []
bram = []
ff = []
lut = []
dsp = []
data = [dsp,bram,ff,lut]

resources = sorted(resources, key=lambda k: k['bitwidth'])
resources_graph = resources
for i in range(len(resources)):
	bw.append(resources[i]["bitwidth"])
	bram.append(resources[i]["bram"] ) 
	ff.append(resources[i]["ff"])
	lut.append(resources[i]["lut"])
	dsp.append(resources[i]["dsp"])
	resources_graph[i].pop('bitwidth')


## Resources Utilization sort data
ubw = []
ubram = []
uff = []
ulut = []
udsp = []
udata = [udsp,ubram,uff,ulut]

resources_utilization = sorted(resources_utilization, key=lambda k: k['bitwidth'])
resources_utilization_graph = resources_utilization
for i in range(len(resources_utilization)):
	ubw.append(resources_utilization[i]["bitwidth"])
	ubram.append(resources_utilization[i]["bram"] ) 
	uff.append(resources_utilization[i]["ff"])
	ulut.append(resources_utilization[i]["lut"])
	udsp.append(resources_utilization[i]["dsp"])
	resources_utilization_graph[i].pop('bitwidth')
	
	
########################
#
### Plot charts.
#
########################	
#for i in range(len(data)):
#	plt.figure(i)	
#	plt.plot(bw,data[i],'--ro')
#	plt.xlabel("X label")
#	plt.ylabel("Y label")
#	plt.title("Title")
#	pylab.savefig('figure5.pdf')
	

#for i in range(len(resources_graph)):
#	plt.figure(len(data)+i)
#	f = plt.bar(range(len(resources_graph[i])), resources_graph[i].values(), align='center')
#	plt.xticks(range(len(resources_graph[i])), resources_graph[i].keys())
	
ind = np.arange(len(fileNames))  # the x locations for the groups
width = 0.10       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

# Bram data
rects1 = ax.bar(ind, bram, width, color='r')

# FF data
rects2 = ax.bar(ind+width, ff, width, color='g')

# LUT data
rects3 = ax.bar(ind+width*2, lut, width, color='b')

# DSP  data 
rects4 = ax.bar(ind+width*3, dsp, width, color='y')

ax.set_ylabel('Scores')
ax.set_xticks(ind+width)
ax.set_xticklabels(bw )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('BRAM', 'FF', 'LUT','DSP') )

## Resources Plot data

figg = plt.figure()
ax = figg.add_subplot(111)

# Bram data
rects1 = ax.bar(ind, ubram, width, color='r')

# FF data
rects2 = ax.bar(ind+width, uff, width, color='g')

# LUT data
rects3 = ax.bar(ind+width*2, ulut, width, color='b')

# DSP  data 
rects4 = ax.bar(ind+width*3, udsp, width, color='y')

ax.set_ylabel('Percentage Utilization')
ax.set_xticks(ind+width)
ax.set_xticklabels(bw )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('BRAM', 'FF', 'LUT','DSP') )


plt.show()


#######################################
### Process Resources information Automatically 
#######################################
#flag_title = False
#flag_keyword = False
#flag_summary = False
#
## Total  resources used
#for file in fileOpen:
#	listf = file.readlines()  
#	for line in listf:
#		if line.startswith("== ") and !flag_title:
#			print(lineour
#			print ("Title  here---------------------")
#			# Into the title field 
#			flag_title = True
#		elif line.startswith('+ ') and flag_title:
#			print ("    Keyword here there are a field with information ")
#			flag_keyword = True
#			# Extract information from line and store
#			words = line.split(' ')
#			print(words[1])
#			dict_name = words[1]
#		elif line.startswith ("*") and flag_title:
#			flag_summary = True
#			dict_name = "summary"
#		elif line.startswith('+---') and flag_title and (flag_keyword or flag_summary):
#			print ("        Subkeyword here")
#			flag_table = True
#		elif flag_table = True and line.startswith("|"):
#			info = (line.rstrip()).replace("|", "") 
#	## Find differents section and extract information
#	info = (listf[76].rstrip()).replace("|", "")
#
#	values = [int(s) for s in info.split() if s.isdigit()]
#	values_dict = dict(bram=values[0], dsp=values[1],ff=values[2], lut=values[3],bitwidth=4)
#	print (values_dict)
#	
#	latency=(listf[31].rstrip()).replace("|", "")
#	latenval = [int(s) for s in latency.split() if s.isdigit()]
#	latenval_dict = dict(latenmin=latenval[0],latenmax=latenval[1],intermin=latenval[2],intermax=latenval[3])
#	print (latenval_dict)

###################################
