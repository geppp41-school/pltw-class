from os import close
from tkinter import * # type: ignore
from tkinter import ttk


#https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events
class Window(Frame):## class class_name(different_class) is 
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
    
    def setBackgroundColor(self, color:str | tuple[(int, int, int)]) -> None:
        """sets the windows background color"""
        if(type(color) == tuple):
            hexString = "#"
            for i in range(3):
                if(color[i] > 255 or color[i] < 0):
                    raise ValueError("color value is above the maximum allowed integer input or below the minimum allowed integer input")
                else:
                    hexString += str(color[i].to_bytes()).replace("b\'\\x", "").replace("\'", "") 
            self.__Screen.configure(bg=hexString)
        elif(type(color) == str):
            self.__Screen.configure(bg=color)
        pass
    
# root = Tk()
# root.geometry("800x450")
# root.title("thing")
# # Bind the <Key> event to the print function
# # This means that whenever any key is pressed, print will be called.
# root.bind("<Key>", print("e"))
# root.mainloop()