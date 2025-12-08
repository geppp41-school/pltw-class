from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.Node import Node
import src.python.registry as registry
@gdclass
class game(Node):

	# define properties like this
	# define signals like this


	def _ready(self) -> None:
		registry.register("slime", "res://scene/enemy/slime/slime.tscn")
		
		registry.register("player", "res://scene/Player/player.tscn")
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
