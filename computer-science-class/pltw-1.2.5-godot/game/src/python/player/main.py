
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D

@gdclass
class main(Node2D):

	# define properties like this

	# define signals like this
	


	def _ready(self) -> None:
		
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here
	
	
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
