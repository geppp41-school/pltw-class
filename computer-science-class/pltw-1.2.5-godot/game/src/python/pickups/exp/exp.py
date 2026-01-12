from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3, Vector2
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Area2D import Area2D
import random
@gdclass
class exp(Node2D):

	# define properties like this
	

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.target = None
		
		self.set_meta("collected", False)
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		if(self.get_meta("collected")):
			self.queue_free()
		pass
		# put dynamic code here
	def _physics_process(self, delta: float) -> None:
		if(self.target != None):
			target_angle = self.position.angle_to_point(self.target.position)
			move_direction = Vector2.RIGHT.rotated(target_angle)
			velocity = move_direction * max(48, self.position.distance_to(self.target.position))
			self.position += velocity * delta
		return super()._physics_process(delta)

	def _pick_up_range_entered(self, area:Area2D):
		item_name = str(area.get_name())
		if(item_name == "pickup_range"):
			self.target = area.get_parent()
			
		pass

	def collected(self):
		self.queue_free()
	
	def get_exp_value(self):
		return self.get_meta("exp_value")

	
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
