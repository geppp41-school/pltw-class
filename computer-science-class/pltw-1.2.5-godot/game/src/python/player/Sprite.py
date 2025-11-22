
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector2, Vector3
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D

@gdclass
class Sprite(AnimatedSprite2D):

	# define properties like this
	

	# define signals like this
	


	def _ready(self) -> None:
		self.play("moving")
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass

	def die(self):
		self.position += Vector2.new3(-7, -16)
		# put dynamic code here
	
	
	
	

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
