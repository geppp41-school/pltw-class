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
		self.card_object = self.load_level_cards()
		self.parent:Node2D = self.get_parent()
		print(self.card_weights)
		print(self.card_rarities)
		self.roll_cards()
		

	def roll_cards(self) -> None: 
		print("rolling cards")
		#sets card rarities
		self.card_1.set_frame(self.card_rarities.index(choices(self.card_rarities, self.card_weights)[0]))
		self.card_2.set_frame(self.card_rarities.index(choices(self.card_rarities, self.card_weights)[0]))
		self.card_3.set_frame(self.card_rarities.index(choices(self.card_rarities, self.card_weights)[0]))

		#sets the cards title according to rarity 
		self.card_1.get_node("name").set_text(self.card_rarities[self.card_1.get_frame()])
		self.card_2.get_node("name").set_text(self.card_rarities[self.card_2.get_frame()])
		self.card_3.get_node("name").set_text(self.card_rarities[self.card_3.get_frame()])

		self.set_card_text(self.card_1)
		self.set_card_text(self.card_2)
		self.set_card_text(self.card_3)
		
		

		pass

	def set_card_text(self, card:AnimatedSprite2D):
		#set the amount of different buffs the card will have 
		count = 0
		if(card.get_frame() < 2):
			count = 1
		elif(card.get_frame() == 2):
			count = randint(1, 2)
		elif(card.get_frame() < 4):
			count = 2
		elif(card.get_frame() < 7):
			count = randint(2,3)
		else:
			count = 3

		print(count)

		#changes the amount of visible modifier texts
		if(count == 1):
			card.get_node("modifier_1").visible = True
			card.get_node("modifier_2").visible = False
			card.get_node("modifier_3").visible = False
		elif(count == 2):
			card.get_node("modifier_1").visible = True
			card.get_node("modifier_2").visible = True
			card.get_node("modifier_3").visible = False
		else:
			card.get_node("modifier_1").visible = True
			card.get_node("modifier_2").visible = True
			card.get_node("modifier_3").visible = True
		
		for i in range(count):
			card_rarity:dict[Any, Any] | Any = self.card_object.get(self.card_rarities[card.get_frame()])
			possible_stats = card_rarity.get("stats")
			stat = choice(list(possible_stats.keys()))# type: ignore
			min = possible_stats.get(stat).get("min") #type: ignore
			max = possible_stats.get(stat).get("max") # type: ignore
			change = 0

			if(len(min) == 1):
				
				
				change = round(uniform(min[0], max[0]), 2)
				
				text = f"+{change*100}% {self.get_stat_name_from_var(stat)}"
			else:
				mod = randint(0, 1)
				
				if(mod == 0):
					
					change = round(uniform(min[0], max[0]), 2)
					text = f"+{change} {self.get_stat_name_from_var(stat)}"
				else:
					
					change = round(uniform(min[1], max[1]), 2)
					text = f"+{change*100}% {self.get_stat_name_from_var(stat)}"
			
			if(i == 0):
				card.get_node("modifier_1").text = text
				print("changing modifier 1 text")
			elif(i == 1):
				print("changing modifier 2 text")
				card.get_node("modifier_2").text = text
			elif(i == 3):
				print("changing modifier 3 text")
				card.get_node("modifier_3").text = text
			meta = card.get_meta("stats")
			meta.append("{\"stat\": \"" + stat+ "\", \"change\":" +  str(change) + "}")
			card.set_meta("stats", meta)



	def load_level_cards(self):
		file:FileAccess = FileAccess.open("res://src/python/player/level_cards.json", ModeFlags.READ)
		jsonObject:dict = json.loads(file.get_as_text())
		self.card_rarities = list(jsonObject.keys())
		for i in range(len(self.card_rarities)):
			self.card_weights.append(jsonObject.get(self.card_rarities[i]).get("weight")) # type: ignore
		file.close()
		return jsonObject
	
	def get_stat_name_from_var(self, var):
		if(var == "attack_cd"):
			return "Attack CD"
		elif(var == "damage"):
			return "Damage"
		elif(var == "attack_size"):
			return "Attack Size"
		elif(var == "multi_shot"):
			return "Multi Shot"
		elif(var == "dodge"):
			return "Dodge"
		elif(var == "hp"):
			return "HP"
		elif(var == "collection_range"):
			return "Pickup Range"
		elif(var == "exp_gain"):
			return "Exp Gain"
		
	def _on_card_1_pressed(self):
		self.parent.call("add_card", self.card_1.get_meta("stats"))
		pass

	def _on_card_2_pressed(self):
		self.parent.call("add_card", self.card_2.get_meta("stats"))
		pass

	def _on_card_3_pressed(self):
		self.parent.call("add_card", self.card_3.get_meta("stats"))
		pass
	pass


	
