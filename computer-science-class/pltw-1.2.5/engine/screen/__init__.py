import tkinter as tk
from tkinter import Event
from tkinter import Misc
from tkinter import ttk
from turtle import color
from typing import Any, List
from PIL import Image, ImageTk
from engine.util.types import TexturedObject
import time

_root = tk.Tk()
_root.geometry("640x480")
__loadedObjects = {"TexturedObject": []}
_actionQueue: List[tuple[Any, dict]] = []

def ResolveQueue():
    global _actionQueue
    for action in _actionQueue:
        action[0](action[1])
    _actionQueue = []
    _root.after(1, ResolveQueue)

def __setBackground(color):
    _root.configure(bg=color)

def setBackground(color):
    _actionQueue.append((__setBackground, color))

# def __loadTexture(texturePath):
#     image = Image.open(texturePath)
#     tk_image = ImageTk.PhotoImage(image)
#     __loadedTextures[texturePath] = tk_image
#     image_lable = tk.Label(root, image=tk_image)
#     image_lable.place(x=0, y=0)

def __loadTexture(texturePath):
    global __loadedObjects
    __loadedObjects["TexturedObject"].append(TexturedObject(_root, texturePath["texture"]))
    #__loadedObjects.append(TexturedObject(root, texturePath))

def loadTexture(texturePath, name=f"TexturedObject{__loadedObjects["TexturedObject"].count(type(TexturedObject))+1}"):
    global _actionQueue
    
    args = {
        "name": name,
        "texture": texturePath
    }
    _actionQueue.append((__loadTexture, args))
    pass
def get_test_object():
    global __loadedObjects
    if len(__loadedObjects["TexturedObject"]) > 0:
        return __loadedObjects["TexturedObject"][0]
    return None

def close_window():
    global running
    running = False
    _root.destroy()

_root.protocol("WM_DELETE_WINDOW", close_window)

ResolveQueue()
timeOne = time.time()
timeTwo = time.time()
def update():
    global timeOne, timeTwo
    #timeTwo = time.time()
    #print('\033c', end='', flush=True)
    #if((timeTwo-timeOne) != 0):
    #    print("fps: "+str(1/(timeTwo-timeOne)))
    #timeOne = timeTwo
    for obj in __loadedObjects["TexturedObject"]:
        obj.place()
    _root.update()
    _root.after(1, update)
    

def mainLoop():
    _root.mainloop()

