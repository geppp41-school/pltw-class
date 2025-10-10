from os import close
from tkinter import * # type: ignore
from tkinter import ttk


#https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
class Window:
    '''The class for the window'''

    def __init__(self, Title : str = "", Resolution : str = "800x450"):
        '''Creates the window'''
        #seting up the private varuables
        self.__bindedKeys = []
        self.__keysPressed = []
        self.__Screen = Tk()#create screen

        #seting up the screen
        self.__Screen.title(Title)
        self.__Screen.geometry(Resolution)#set resolution
        
        self.__Screen.bind("<Key>", lambda key : self.__keysPressed.append(key.keycode))#checks what keys are pressed
        self.__Screen.bind("<KeyRelease>", lambda key : self.__keysPressed.remove(key.keycode))
    
    def changeScreenSize(self, size : str) -> None:
        """change the screen size"""
        self.__Screen.geometry(size)

    def bindKey(self, Key : str, func) -> None:
        """bind a key to a function"""
        self.__Screen.bind(Key, func)
        self.__bindedKeys.append("Key")

    def unbindKey(self, Key) -> None:
        """unbind a key"""
        self.__Screen.unbind(Key)

    def mainLoop(self):
        """main loop"""
        self.__Screen.mainloop()

    def quit(self, exitCode : int = 0) -> None:
        """quit the program"""
        self.__Screen.destroy()
        quit(exitCode)
    
    def setBackground(self, color:str) -> None:
        self.__Screen.configure(background=color)
        pass
    
# root = Tk()
# root.geometry("800x450")
# root.title("thing")
# # Bind the <Key> event to the print function
# # This means that whenever any key is pressed, print will be called.
# root.bind("<Key>", print("e"))
# root.mainloop()