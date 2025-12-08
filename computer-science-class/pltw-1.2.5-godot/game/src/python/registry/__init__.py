from typing import Any
from py4godot.classes import *
from py4godot.classes.Input import Input
from py4godot.classes.Node import Node
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.classes.core import *
from py4godot.classes.Object import Object


_register:dict[str, Any] = {}
input:Input = Input().instance()

def register(name:str, path:str):
    _register[name] = ResourceLoader.instance().load(path)
    pass

def getSceen(name:str) -> Any:
    if(_register.__contains__(name)):
        return _register.get(name)
    else:
        raise KeyError(f"the item {name} does not currently exist in the registry")
    

register("fireball", "res://scene/projectiles/fireball.tscn")