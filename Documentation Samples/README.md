## Title: Creating a simple GUI application using Python

The purpose of this file is to explain step-by-step how create a simple GUI application using Python from scratch. 

## Software Requirements
Python 3+

## Prerequistes
Understanding of OOP concepts

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

Code sample in Python:
![Code to create a window and a label](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image1.png)

![output result for step 1](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image2.png)

## Step 2 - Creating a textbox and a button

Code sample in Python:
![Code to create a textbox and a button](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image4.png)

![output result for step 2](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image5.png)

## Step 3 - Controlling the button

The main purpose of any button is to actually do something when it is pressed. This is called an event. In the following example, when the user presses the submit button, the code will call the function submitButton and a message "Welcome <<name>>" is displayed.
  
Note: Modification to this line: submitButton = Button(root, text = "Submit", command = buttonSubmit)

![Code to create an event](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image6.png)

![output result for step 3](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image7.png)

## Step 4 - Creating a dropdown list with two items (Male and Female)

![Code to create a dropdown list with two items](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image8.png)

![output result for step 4](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image9.png)

## Step 5 - Adding an imagebox and displaying image depending on choice selected in Step 4

![Code to display image depending on choice](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image10.png)

![output result for step 4](https://github.com/lucienne1986/Python-Projects/blob/master/Documentation%20Samples/img/image11.png)

## Additional notes
Image paths need to be changed to your local path

## Download Original Copy
A copy of this code can be found on : Documentation Samples/pythonGUI.py





