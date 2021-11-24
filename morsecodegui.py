from tkinter import *


# Create a class for the window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master


        # Heading Label
        heading = Label(self, text="Welcome to my morse code application.")
        heading.grid(row = 0, column = 0)

        # Code Entry
        codeInput = StringVar()
        codeEntry = Entry(self, textvariable= codeInput)
        codeEntry.grid(row=1, column=0)
        
        # Code Submit Button
        codeSubmitButton = Button(self, text="Submit", command=self.clickCodeSubmitButton)
        codeSubmitButton.grid(row=1, column=1)

        # Show submitted code
        label = Label(root, textvariable=codeInput)
        label.grid(row=3, column=0)

        # Quit Button
        quitButton = Button(self, text="Quit", command=self.clickQuitButton)
        quitButton.grid(row=2,column=2)


    def clickCodeSubmitButton(self):


        '''
        translate codeInput and display on ___
        '''
        # Clear the Code Entry

    def clickQuitButton(self):
        exit()





# initialize tkinter & create window
root = Tk()
app = Window(root)

root.wm_title("Morse Code") # set window title

root.mainloop() # show window