import tkinter as tk
from tkinter import Event
from tkinter import Misc
from tkinter import ttk
from turtle import color
from typing import Any, List
from PIL import Image, ImageTk
from engine.util.types import TexturedObject

root = tk.Tk()
root.geometry("640x480")
__loadedObjects = []
_actionQueue: List[Any] = []

def ResolveQueue():
    global _actionQueue
    for action in _actionQueue:
        action[0](action[1])
    _actionQueue = []
    root.update()
    root.after(50, ResolveQueue)

def __setBackground(color):
    root.configure(bg=color)

def setBackground(color):
    _actionQueue.append((__setBackground, color))

# def __loadTexture(texturePath):
#     image = Image.open(texturePath)
#     tk_image = ImageTk.PhotoImage(image)
#     __loadedTextures[texturePath] = tk_image
#     image_lable = tk.Label(root, image=tk_image)
#     image_lable.place(x=0, y=0)

def __loadTexture(texturePath):
    __loadedObjects.append(TexturedObject(root, texturePath))

def loadTexture(texturePath):
    _actionQueue.append((__loadTexture, texturePath))
    pass

def close_window():
    global running
    running = False
    root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)

ResolveQueue()

def update():
    for obj in __loadedObjects:
        obj.place()
    root.update()

def mainLoop():
    root.mainloop()

