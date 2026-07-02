import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[0,1,2,3,4]
y=[0,2,4,4,4]
plt.plot(x,y,label="2x",color='green',marker='.',linestyle='--',linewidth=2,markersize=10,markeredgecolor='blue')
#plt.plot makes the graph .
#marker is the points representing the values .
#label='2x' add a mini label on graph . to use it we have to write down the plt.legend(). like we did in line no.14.

#there's another way to write plot's style in short way:
#plt.plot(x,y,'r.-',label='2x')
#here 'r.-' is in the format of [color][marker][line]


plt.title("simple graph",fontdict={'fontname':'Comic Sans MS','fontsize':12,'fontweight':'bold','color':'red'})
#fontdict contains the style for title of graph. fontname is the font style.
plt.xlabel("X-axis",fontdict={'fontsize':10})#label for X-axis.
plt.ylabel("Y-axis",fontdict={'fontsize':10})#label for Y-axis.

plt.xticks([0,1,2,3,4])#set the positions of the ticks on the X-axis
plt.yticks([0,2,4,6,8])#set the positions of the ticks on the Y-axis
#ticks are numbers or marks shown on the axis.
plt.legend()
plt.show()
#plt.show print/show the graph