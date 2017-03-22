# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:59:38 2017

@author: 3670055
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

ax = plt.axes(xlim=(0, 20), ylim=(0, 20))

size = 0.1
xcenter = 5
ycenter = 5
radius=1

n=10

liste_patch=[]

for p in range(n):
    patch = plt.Circle((0,0), size, fc='b')
    liste_patch.append(patch)

def init():
    #ax.add_patch(patch)
    return liste_patch

def animate(t):   
    i=1
    for p in liste_patch:   
        x, y = p.center
        x = xcenter + i*radius * np.sin(np.radians(t+i))
        y = ycenter + i*radius * np.cos(np.radians(t+i))
        p.center = (x, y)
        i=i+1
    return liste_patch

anim = animation.FuncAnimation(fig, animate, 
                               init_func=init, 
                               frames=360, 
                               interval=20,
                               blit=True)
plt.show()