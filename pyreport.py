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
import numpy as np

titles = {"Performance Estimates", "Utilisztion Estimates" , "Interface"} 
keywords = {"Timing", "Latency", "Detail"} # id with '+'
keyworks_sub = {"Register", "Multiplexer", "Expression", "FIFO", "Memory",
                   "DSP48", "Instance"}

########################
#
# Open files 
#
########################	

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

number_solutions = len(fileNames)
resources = []
latency = []
resources_utilization = []
timing = []
file_index = 0
file_index_x = 0
all_bit_width = []
########################
#
# Extract information 
#
########################	

for file in fileOpen:
	
	# Resources
	listf = file.readlines()
	info = (listf[76].rstrip()).replace("|", "")
	values = [int(s) for s in info.split() if s.isdigit()]
	bitw =[int(s) for s in re.findall(r'\d+',fileNames[file_index])][0] 
	resources.append(dict(bram=values[0], dsp=values[1],ff=values[2],
	lut=values[3],bitwidth=bitw))
	if bitw not in all_bit_width: all_bit_width.append(bitw) 
	pprint (resources)
	file_index = file_index + 1

	# Resources Utilization
	info = (listf[80].rstrip()).replace("|", "")
	values = [int(s) for s in info.split() if s.isdigit()]
	bitw =[int(s) for s in re.findall(r'\d+',fileNames[file_index_x])][0] 
	resources_utilization.append(dict(bram=values[0], dsp=values[1],ff=values[2],
	lut=values[3],bitwidth=bitw))
	pprint (resources_utilization)
	file_index_x = file_index_x + 1

    #Latency	
	info = (listf[31].rstrip()).replace("|", "")
	print(info)
	values = [int(s) for s in info.split() if s.isdigit()]
	latency.append(dict(latenmin=values[0],latenmax=values[1],intermin=values[2],intermax=values[3],bitwidth=bitw))
	pprint(latency)
	
	#Timing
	info = (((listf[22].rstrip()).replace("|", "")).replace("ap_clk","")).rstrip()
	print(info)
	values = re.findall('([\d.]+)', info)
	print(values)
	timing.append(dict(target=float(values[0]), estimates = float(values[1]), uncertainty =
	float(values[2]), bitwidth=bitw))
	pprint(timing)
	file.close()

########################
#
# Analyse possible solutions separately  
#
########################	
timing_test = sorted(timing, key=lambda k: k['bitwidth'])

## Possible timing solutions
for i in range(len(fileNames)):
	if timing_test[i]['estimates'] < timing[i]['target']:
		print("Posible solution")
		timing_test[i]['possible'] = 1
	else:
		timing_test[i]['possible'] = 0
		print("Solution not possible")

## Possible resources solutions
	if any(v > 100 for v in resources_utilization[i].values()):
		resources_utilization[i]['possible']=0
		print("Solution impossible: not enough resources")
	else:
		resources_utilization[i]['possible'] = 1

#############################
#
# Find possible and optimal solutions 
#
#############################	

## Optimal solution in terms of timing and resources
timing_opt = []
resources_opt = []
possible_solutions = []
# Test optimal timing
for solution in range(number_solutions):
	#TODO add test resources_utilization reources utilzation
	if (timing_test[solution]['possible']== 1 and
	resources_utilization[solution]['possible'] == 1):
	#FIX this works if we suppose that list are in the same order
		print("here are a possible solution")
		tmp_opt = 0
		print(tmp_opt)
		timing_opt.append(timing_test[solution])
		resources_opt.append(resources_utilization[solution])


"""
# Search here and optimal solution between all the possibles
		if tmp_opt > timing_test[solution]['estimates']:
			print("this is a worst solution")
		elif tmp_opt < timing_test[solution]['estimates']:
			print("optimal solution here")
			if timing_opt:
				if timing_test[solution]['bitwidth'] == timing_opt[-1]['bitwidth']:
					print("switch solution")
					timing_opt.pop()
				timing_opt.append(timing_test[solution])
			elif not timing_opt:
				print("add solution")
				timing_opt.append(timing_test[solution])
		elif tmp_opt == timing_test[solution]['estimates']:
			print("start a timing optimal search") 
		else: print("there is a criteria not covered")# other criteria
"""
print(timing_opt)

########################
#
# Store Data in order
#
########################	

## Vectors to store information in the right order before plot it
bw = []
bram = []
ff = []
lut = []
dsp = []
data = [dsp,bram,ff,lut]
timing_values = []
timing_possible_values = []
latency_values = []
throughput_values = []
timing_data = [timing_values, latency_values, throughput_values]
timing_target_values = []
resources_bak = resources
resources_ls = sorted(resources, key=lambda k: k['bitwidth'])
timing_opt = sorted(timing_opt, key=lambda k: k['bitwidth'])
resources_graph = resources_ls

# All possible solution 
for i in range(len(resources_ls)):
	# Resources usage (absolute)
	bw.append(resources_ls[i]["bitwidth"])
	bram.append(resources_ls[i]["bram"]) 
	ff.append(resources_ls[i]["ff"])
	lut.append(resources_ls[i]["lut"])
	dsp.append(resources_ls[i]["dsp"])
	resources_graph[i].pop('bitwidth')
	timing_values.append(timing_test[i]["estimates"])
	timing_target_values.append(timing_test[i]["target"])
	latency_values.append(latency[i]["latenmax"])
	throughput_values.append(latency[i]["intermax"])


pbw = []
pbram = []
pff= []
plut = []
pdsp = []
timing_possible_target = []
# Data of only possible solution 
for i in range(len(timing_opt)):
	# Timing information
	timing_possible_values.append(timing_opt[i]["estimates"])
	timing_possible_target.append(timing_opt[i]["target"])
	pbw.append(resources_opt[i]["bitwidth"])
	pbram.append(resources_opt[i]["bram"]) 
	pff.append(resources_opt[i]["ff"])
	plut.append(resources_opt[i]["lut"])
	pdsp.append(resources_opt[i]["dsp"])




## Resources Utilization percentage 
ubw = []
ubram = []
uff = []
ulut = []
udsp = []
udata = [udsp,ubram,uff,ulut]
resources_utilization_ls = sorted(resources_utilization, key=lambda k: k['bitwidth'])
resources_utilization_graph = resources_utilization_ls

for i in range(len(resources_utilization_ls)):
	ubw.append(resources_utilization_ls[i]["bitwidth"])
	ubram.append(resources_utilization_ls[i]["bram"] ) 
	uff.append(resources_utilization_ls[i]["ff"])
	ulut.append(resources_utilization_ls[i]["lut"])
	udsp.append(resources_utilization_ls[i]["dsp"])
	resources_utilization_graph[i].pop('bitwidth')
	resources_utilization_graph[i].pop('bitwidth')


###############################
#
### Plot charts. Only bars. Only percentage
#
###############################

#for i in range(len(resources_graph)):
#	plt.figure(i)
#	f = plt.bar(range(len(resources_graph[i])), resources_graph[i].values(), align='center')
#	plt.xticks(range(len(resources_graph[i])), resources_graph[i].keys())

## Resources Utilization  Plot data
ind = np.arange(len(fileNames))  # the x locations for the groups
width = 0.20       # the width of the bars
fig = plt.figure()
ax = fig.add_subplot(311)
# Bram data
rects1 = ax.bar(ind, bram, width, color='r')
# FF data
rects2 = ax.bar(ind+width, ff, width, color='g')
# LUT data
rects3 = ax.bar(ind+width*2, lut, width, color='b')
# DSP  data
rects4 = ax.bar(ind+width*3, dsp, width, color='y')
ax.set_ylabel('Number of elements used')
ax.set_xticks(ind+width)
ax.set_xticklabels(bw )
ax.set_title('Resources usage (absolute values)')
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('BRAM', 'FF', 'LUT','DSP') )

## Resources Utilization  Plot data
#figg = plt.figure()
ax = fig.add_subplot(312)
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
ax.set_title('Resources usage (percentage)')
ax.set_xticklabels(bw )
ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('BRAM', 'FF', 'LUT','DSP') )

ax = fig.add_subplot(313)
# Estimates clock
rects1 = ax.bar(ind, timing_values , width, color='r')
# Target clock
rects2 = ax.bar(ind+width, timing_target_values, width, color='b')
ax.set_ylabel('ns')
ax.set_title('Clock of all solution')
ax.set_xticks(ind+width)
ax.set_xticklabels(bw)


## All Timing solution
width = 0.37
index = np.arange(len(timing_values))
figt = plt.figure()
ay = figt.add_subplot(111)
# Estimates clock
rects1 = ay.bar(index, timing_values , width, color='r')
# Target clock
rects2 = ay.bar(index+width, timing_target_values, width, color='b')
ay.set_ylabel('ns')
ay.set_title('Clock of all solution')
ay.set_xticks(index+width)
ay.set_xticklabels(bw)

## Possible Resources solution 
ind = np.arange(len(timing_opt))
width = 0.18
figp= plt.figure()
aa = figp.add_subplot(211)
# Bram data
rects1 = aa.bar(ind, pbram, width, color='r')
# FF data
rects2 = aa.bar(ind+width, pff, width, color='g')
# LUT data
rects3 = aa.bar(ind+width*2, plut, width, color='b')
# DSP  data 
rects4 = aa.bar(ind+width*3, pdsp, width, color='y')
aa.set_ylabel('Percentage Utilization')
aa.set_xticks(ind+width)
aa.set_title('Resources usage (percentage) real possible solution')
aa.set_xticklabels(pbw )
aa.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('BRAM', 'FF', 'LUT','DSP') )

aa = figp.add_subplot(212)
# Estimates clock
rects1 = aa.bar(ind, timing_possible_values , width, color='r')
# Target clock #FIXME no data charged for target in possible solution
rects2 = aa.bar(ind+width, timing_possible_target, width, color='b')
aa.set_ylabel('ns')
aa.set_title('Clock of all real possible solution')
aa.set_xticks(ind+width)
aa.set_xticklabels(pbw)






## Optimal Solution (possible + fast + less resouces consomption)




# Plot everything
plt.show()


## TODO store in a pdf file

