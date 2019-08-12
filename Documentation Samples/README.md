## Title: Creating a simple GUI application using Python

The purpose of this file is to explain step-by-step how create a simple GUI application using Python from scratch. 

## Software Requirements
Python 3+

## Install libraries
The following two libraries are needed to be able to run GUI on python and access images. 

Tkinter and PIL (Python imaging library)

To install, in the terminal type:
sudo pip install pil
sudo pip install tkinter

Tkinter is a GUI (Graphical user interface) widget set for Python to be able to create a more innovative application. 

Tkinter is not the only GuiProgramming toolkit for Python. It is however the most commonly used.
<<insert image 1>>

## Step 1 - Creating a window and label

import tkinter
from tkinter import*
import PIL

root = Tk() #creates teh window
root.wm_title("Simple GUI") #display a title on the title bar
root.geometry('500x300+300+300')#the dimensions of the window

#add a label
label1 = Label(root, text = "Simple GUI app")
#display - Xaxis, Yaxis and side
label1.pack(padx=10, pady=5, side=LEFT)

root.mainloop()#start monitoring and updating the GUI - This is the last line of the script

![test](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image2.png)


