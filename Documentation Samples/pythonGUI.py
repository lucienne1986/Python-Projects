import tkinter
from tkinter import*
import PIL
from PIL import Image
from PIL import ImageTk

root = Tk() #creates the window
root.wm_title("Simple GUI") #display a title on the title bar
root.geometry('500x300+300+300')#the dimensions of the window

#create a global variable which will be used in the function and in the main prog
global tkimage

##functions##
def buttonSubmit():
    #get the text from the textbox
    name = userInput.get()
    #create message
    labelShow = Label(root, text = "Welcome " + name)
    #display the message
    labelShow.pack(padx=18, pady=8, side=LEFT)

def showImage(value):
    if(value == "Male"):
        MaleImage = Image.open('/Users/lucienne/Desktop/man.jpg')
        tkimage = ImageTk.PhotoImage(MaleImage)
        label.config(image = tkimage)
        root.update() #to 'refresh' the window
      
    if(value == "Female"):
        FemaleImage = Image.open('/Users/lucienne/Desktop/woman.png')
        tkimage = ImageTk.PhotoImage(FemaleImage)
        label.config(image = tkimage)
        root.update() #to 'refresh' the window
        
        
#add a label
labelName = Label(root, text = "Input your name")
#display - Xaxis, Yaxis and side
labelName.pack(padx=10, pady=5, side=LEFT)

#add a textbox
userInput = Entry(root, width = 10)
#adjust the textbox settings
userInput.pack(padx=15, pady=8, side = LEFT)

#add a button with an event which is calling function buttonSubmit()
submitButton = Button(root, text = "Submit", command = buttonSubmit)
submitButton.pack(padx=15, pady=8, side=LEFT)

#add a list for gender
genderList=('Male', 'Female')
#store choice to a variable
menuChoice = tkinter.StringVar()

#add gender label
labelGender = Label(root, text = "Choose gender")
labelGender.pack(padx=15, pady=12, side=LEFT)

#add dropdown list and loop through the list declared above
userGender = OptionMenu(root, menuChoice, *genderList, command = showImage)
userGender.pack(padx=15, pady=12, side=LEFT)

#image section

genderImage = Image.open("/Users/lucienne/Desktop/noImage.png")
tkimage = ImageTk.PhotoImage(genderImage)
label = tkinter.Label(root, image=tkimage)
label.pack(padx=17, pady=5)



#start monitoring and updating the GUI - This is the last line of the script
root.mainloop()

