#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

tree = ET.parse('books.xml')
root = tree.getroot()

#for child in root:
#    print(child.tag, child.attrib)
#    
#for book in root.iter('book'):
#    print(book.attrib)
#
#
#for description in root.iter('description'):
#    print(description.text)
#    
#for p in root.iter('price'):
#    print(p.text)

#plot a bar chart book name vs price
# frequencies 

# setting the ranges and no. of intervals 
range = (0, 100) 
bins = 10  
  
xaxis = []
yaxis = []


plt.xlabel("price")
plt.ylabel("book titles")

plt.title("Book titles vs prices")

for t in root.iter('title'):
    xaxis.append(t.text)

for p in root.iter('price'):
    yaxis.append(p.text)

y_pos = np.arange(len(xaxis))

plt.barh(y_pos, yaxis, align='center', alpha=0.5)
plt.yticks(y_pos, xaxis)

plt.legend()
plt.show()

