from math import cos, sin
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
	damage_modifier = 0.0
	damage_mutiplier = 1.0
	size = 0.5
	size_modifier = 1.0
	noise_offset : Vector3 = Vector3.new3(0, 0, 0)#32x for 1 second, -32y for 1 second
	

	# define signals like this
	
	
	def _ready(self) -> None:
		self.noise_object:Sprite2D = self.get_node("Sprite2D")
		self.time_passed = 0.0
		self.noise_offset = Vector3.new3(16*self.life_span, -16*self.life_span, 0)
		if(self.get_parent().get_node("player") != None):
			self.position = self.get_parent().get_node("player").position
			
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		self.scale = Vector2.new3(self.size * self.size_modifier, self.size * self.size_modifier)
		self.time_passed += delta
		self.noise_offset += Vector3.new3(-16*delta, 16*delta, 0)
		self.noise_object.texture.noise.offset = self.noise_offset
		if(self.time_passed >= self.life_span):
			self.queue_free()
		self.position += Vector2.new3(
			1*cos(self.direction)-0*sin(self.direction),
			1*sin(self.direction)+0*cos(self.direction)
			).normalized()*self.speed*delta
		#self.position += Vector2.RIGHT.rotated(self.direction).normalized()*self.speed*delta
		pass
		# put dynamic code here

	def set_speed(self, speed):
		self.speed = speed

	def set_direction(self, direction):
		
		self.direction = direction
		self.position += Vector2.new3(
			1*cos(self.direction)-0*sin(self.direction),
			1*sin(self.direction)+0*cos(self.direction)
			).normalized()*16
		
	def set_damage_modifier(self, modifier):
		self.damage_modifier = modifier
	def set_damage_mutiplier(self, mutiplier):
		self.damage_mutiplier = mutiplier
	def set_size(self, size):
		self.size_modifier = size

	def get_damage(self):
		return (50+self.damage_modifier)*self.damage_mutiplier
	
	

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
