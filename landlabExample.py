#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:43:21 2017

@author: lucienne
"""

import numpy
from landlab import RasterModelGrid
import matplotlib.pyplot as plt
from landlab.plot.imshow import imshow_grid

mg = RasterModelGrid((25, 40), 10.0)
z = mg.add_zeros('node', 'topographic__elevation')
#plt.plot(mg.node_x, mg.node_y, '.')
imshow_grid(mg, 'topographic__elevation')