import json
from random import choice, choices
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Engine import Engine
from py4godot.classes.FileAccess import FileAccess
from py4godot.classes.FileAccess import ModeFlags


@gdclass
class level_up_menu(Node2D):

	# define properties like this
	card_1: AnimatedSprite2D
	card_2: AnimatedSprite2D
	card_3: AnimatedSprite2D
	card_weights = []
	card_rarities = []#might also add primed variants

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.card_1 = self.get_node("card_1")
		self.card_2 = self.get_node("card_2")
		self.card_3 = self.get_node("card_3")
		self.card_object = self.load_level_cards()
		parent:Node2D = self.get_parent()
		print(parent.call("get_luck"))
		Engine.instance().set_time_scale(0)
		
		self.card_1.set_frame(self.card_rarities.index(choices(self.card_rarities, self.card_weights)[0]))
		self.card_2.set_frame(self.card_rarities.index(choices(self.card_rarities, self.card_weights)[0]))
		self.card_3.set_frame(self.card_rarities.index(choices(self.card_rarities, self.card_weights)[0]))
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		
		pass
		# put dynamic code here

	def get_card_weights_after_luck(self) -> list[int]:
		
		luck = self.get_parent().call("get_luck")
		if(luck == 0):
			return self.card_weights
		else:
			w = self.card_weights
			return [w[0]*(0.25*luck), w[1]-3*luck, w[2]+2*luck, w[3], w[4]*(2*luck), w[5]*(1.75*luck), w[6]*(1.5*luck), w[7]*(1.25*luck)]
		pass

	def load_level_cards(self):
		file:FileAccess = FileAccess.open("res://src/python/player/level_cards.json", ModeFlags.READ)
		jsonObject:dict = json.loads(file.get_as_text())
		self.card_rarities = list(jsonObject.keys())
		for i in range(len(self.card_rarities)):
			self.card_weights.append(jsonObject.get(self.card_rarities[i]).get("weight")) # type: ignore

		return jsonObject
		# print(self.card_weights)
		# print(jsonObject.get("common").get("weight")) # type: ignore
		
		pass
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
