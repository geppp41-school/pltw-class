import tkinter as tk
from tkinter import Event
from tkinter import Misc
from typing import Any, List

_screen = tk.Tk()
_actionQueue: List[Any] = []

def ResolveQueue():
    global _actionQueue
    for action in _actionQueue:
        action()
    _actionQueue = []
    _screen.after(50, ResolveQueue)

_screen.mainloop()