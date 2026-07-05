
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Resize your Graph
plt.figure(figsize=(5,3),dpi=300)#here figsize=(x,y) . we used to adjust the graph size.
#dpi = dots per inch(image resolution) , higher the dpi , higher the resolution

x=[0,1,2,3,4]
y=[0,2,4,4,4]
plt.plot(x,y,label="2x",color='green',marker='.',linestyle='--',linewidth=2,markersize=10,markeredgecolor='blue')
#plt.plot makes the graph .
#marker is the points representing the values .
#label='2x' add a mini label on graph . to use it we have to write down the plt.legend(). like we did in line no.14.

#there's another way to write plot's style in short way:
#plt.plot(x,y,'r.-',label='2x')
#here 'r.-' is in the format of [color][marker][line]


##Second Line
x2=np.arange(0,4.5,0.5)
plt.plot(x2[:6],x2[:6]**2,'r',label='x^2')
plt.plot(x2[5:],x2[5:]**2,'r--')


plt.title("simple graph",fontdict={'fontname':'Comic Sans MS','fontsize':12,'fontweight':'bold','color':'red'})
#fontdict contains the style for title of graph. fontname is the font style.

plt.xlabel("X-axis",fontdict={'fontsize':10})#label for X-axis.
plt.ylabel("Y-axis",fontdict={'fontsize':10})#label for Y-axis.

plt.xticks([0,0.5,1,1.5,2,2.5,3,3.5,4])#set the positions of the ticks on the X-axis
plt.yticks([0,2,4,6,8,10,12,14,16])#set the positions of the ticks on the Y-axis
#ticks are numbers or marks shown on the axis.


plt.legend()

plt.savefig('simple_graph.png', dpi=300)

plt.show()
#plt.show print/show the graph



### Bar Charts

labels=['A', 'B' , 'C']
values=[3,2,6,]

bars= plt.bar(labels,values)#bar chart
plt.figure(figsize=[10,5],dpi=300)
#plt.xlabel("X-axis",fontdict={'color':'r','fontsize':10})
#plt.ylabel("Y-axis",fontdict={'color':'r','fontsize':10})

bars[0].set_hatch('/')#pattern in bars
bars[1].set_hatch('\\')
bars[2].set_hatch('|')

##or :
#patterns=['/','\\','|']
#for bar in bars:
#      bar.set_hatch(patterns.pop(0))##here pop(0) tells to take pattern values from start .
plt.show()