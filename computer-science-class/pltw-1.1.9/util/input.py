from tkinter import Canvas
import turtle


class input:

    _Pressed = 1
    _Released = 0

    def __init__(self, screen : turtle.TurtleScreen):
        self.__screen : turtle.TurtleScreen = screen
        self.__canvas : Canvas = self.__screen.getcanvas()
        self.__keyState : dict[str, int] = {}

        self.__canvas.master.bind("<KeyPress>", lambda key : self.__setKeyState(key.keysym, 1))
        #self.__canvas.master.bind('<KeyRelease>', lambda key : print(key))#have to use master because the turtle object keeps messing with any binded functions
        self.__canvas.master.bind("<KeyRelease>", lambda key : self.__setKeyState(key.keysym, 0))
        
        pass

    def isKeyPressedInt(self, keyCode:str) -> int:
        """
        returns the state of the pressed key as an int  
        """
        if not keyCode in self.__keyState:
            self.__setKeyState(keyCode, 0)
        return self.__keyState[keyCode]


    def isKeyPressedBool(self, keyCode:str) -> bool:
        """
        returns the state of the pressed key as a boolean 
        """
        if not keyCode in self.__keyState:
            self.__setKeyState(keyCode, 0)
        return True if self.__keyState[keyCode] == 1 else False

    def __setKeyState(self, keyCode:str, state:int):
        """
        states
            1 = pressed
            0 = released
        """
        self.__keyState[keyCode] = state
        pass