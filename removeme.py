import matplotlib.pyplot as plt
import pylab
import os
import fnmatch
from pprint import pprint
import re
import numpy as np


N = 3
ind = np.arange(N)  # the x locations for the groups
width = 0.14       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [4, 9, 2]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [1,2,3]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [11,12,13]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')
fvals = [15,7,7]
rects3 = ax.bar(ind+width*3, fvals, width, color='y')
gvals = [15,16,8]
rects4 = ax.bar(ind+width*4, gvals, width, color='c')





ax.set_ylabel('Scores')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('2011-Jan-4', '2011-Jan-5', '2011-Jan-6') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('y', 'z', 'k') )

plt.show()
