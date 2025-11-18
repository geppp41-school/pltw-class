import tkinter as tk
from tkinter import Event
from tkinter import Misc
from tkinter import ttk
from turtle import color
from typing import Any, List
from PIL import Image, ImageTk

__root = tk.Tk()
__root.geometry("640x480")
__loadedTextures = {}
_actionQueue: List[Any] = []

def ResolveQueue():
    global _actionQueue
    for action in _actionQueue:
        action[0](action[1])
    _actionQueue = []
    __root.update()
    __root.after(50, ResolveQueue)

def __setBackground(color):
    __root.configure(bg=color)

def setBackground(color):
    _actionQueue.append((__setBackground, color))

def __loadTexture(texturePath):
    image = Image.open(texturePath)
    tk_image = ImageTk.PhotoImage(image)
    __loadedTextures[texturePath] = tk_image
    image_lable = tk.Label(__root, image=tk_image)

def loadTexture(texturePath):
    _actionQueue.append((__loadTexture, texturePath))
    pass

def close_window():
    global running
    running = False
    __root.destroy()

__root.protocol("WM_DELETE_WINDOW", close_window)

ResolveQueue()

def update():

    __root.update()

def mainLoop():
    __root.mainloop()

