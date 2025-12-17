from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Engine import Engine



@gdclass
class level_up_menu(Node2D):

	# define properties like this
	card_1: AnimatedSprite2D
	card_2: AnimatedSprite2D
	card_3: AnimatedSprite2D
	card_weights = [125, 75, 60, 50, 25, 10, 5, 1]
	card_rarities = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic", "Ultimate", "Godly"]#might also add primed variants

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.card_1 = self.get_node("card_1")
		self.card_2 = self.get_node("card_2")
		self.card_3 = self.get_node("card_3")
		parent:Node2D = self.get_parent()
		print(parent.call("get_luck"))
		Engine.instance().set_time_scale(0)
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		
		pass
		# put dynamic code here

	def get_card_weights_after_luck(self):
		
		luck = self.get_parent().call("get_luck")
		if(luck == 0):
			return self.card_weights
		else:
			w = self.card_weights
			return [w[0]*(0.25*luck), w[1]-3*luck, w[2]+2*luck, w[3], w[4]*(2*luck), w[5]*(1.75*luck), w[6]*(1.5*luck), w[7]*(1.25*luck)]
		pass
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
