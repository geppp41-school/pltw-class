from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D

@gdclass
class fireball(Node2D):

	# define properties like this
	life_span : float = 10
	noise_offset : Vector3 = Vector3.new3(0, 0, 0)

	# define signals like this
	
	
	def _ready(self) -> None:
		self.noise_object = self.get_node("CPUParticles2D")
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
