
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D

@gdclass
class slime(Node2D):

	# define properties like this
	animated_body:  AnimatedSprite2D = None # type: ignore

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		animated_body = self.get_node("AnimatedSprite2D")  # type: ignore
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
