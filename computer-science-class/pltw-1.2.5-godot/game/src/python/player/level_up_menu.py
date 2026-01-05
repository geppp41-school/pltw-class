import json
from random import choice, choices, randint, uniform
from typing import Any
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Array, PackedStringArray, Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Engine import Engine
from py4godot.classes.FileAccess import FileAccess
from py4godot.classes.FileAccess import ModeFlags


@gdclass
class level_up_menu(Node2D):
    def _ready(self):
        self.card_1: AnimatedSprite2D = self.get_node("card_1")
        self.card_2: AnimatedSprite2D = self.get_node("card_2")
        self.card_3: AnimatedSprite2D = self.get_node("card_3")
        self.card_weights = []
        self.card_rarities = []
        self.card_object = None
    pass