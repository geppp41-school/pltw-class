from turtle import speed
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3, Vector2
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Sprite2D import Sprite2D

@gdclass
class fireball(Node2D):

	# define properties like this
	life_span : float = 5
	speed: float = 16.0
	direction: float = 0.0
	noise_offset : Vector3 = Vector3.new3(0, 0, 0)#32x for 1 second, -32y for 1 second

	# define signals like this
	
	
	def _ready(self) -> None:
		self.noise_object:Sprite2D = self.get_node("Sprite2D")
		self.time_passed = 0.0
		self.noise_offset = Vector3.new3(16*self.life_span, -16*self.life_span, 0)
		self.set_meta("direction", 0.0)
		self.set_meta("speed", 16.0)
		self.set_meta("damage", 50)
		if(self.get_parent().get_node("player") != None):
			self.position = self.get_parent().get_node("player").position
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		self.time_passed += delta
		self.noise_offset += Vector3.new3(-16*delta, 16*delta, 0)
		self.noise_object.texture.noise.offset = self.noise_offset
		if(self.time_passed >= self.life_span):
			self.queue_free()
		self.position += Vector2.RIGHT.rotated(self.get_meta("direction")).normalized()*self.get_meta("speed")*delta
		pass
		# put dynamic code here

	
	

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
