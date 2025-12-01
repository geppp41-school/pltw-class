
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector2, Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D

@gdclass
class slime(Node2D):

	# define properties like this
	animated_body:  AnimatedSprite2D = None # type: ignore
	target: Node2D = None  # type: ignore

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.animated_body = self.get_node("AnimatedSprite2D")  # type: ignore
		self.animated_body.play("Moving")
		if(self.get_parent() != None):
			self.target = self.get_parent().get_node("Player")  # type: ignore
		self.position = Vector2.new3(100,100)
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here

	def _physics_process(self, delta: float) -> None:
		if self.target != None:
			angle = self.position.angle_to_point(self.target.position) # get angle to player
			direction = Vector2.RIGHT.rotated(angle)# get direction to player
			velocity = direction * 16 # sets speed
			self.position += velocity*delta #moves position depending on time between frames or delta 
		pass

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
