
import random
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
	speed: int = 30
	_can_move:bool = True
	target_angle:float = 0
	# define signals like this



	def _ready(self) -> None:
		self.animated_body = self.get_node("AnimatedSprite2D")  # type: ignore
		self.animation_node = self.get_node("AnimationPlayer")
		#self.animated_body.play("Moving")
		self.animation_node.play("slime/moving")
		if(self.get_parent() != None):
			self.target = self.get_parent().get_pyscript().get_player()
		self.position = Vector2.new3(random.randint(-300,300),random.randint(-300,300))
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		
		# put dynamic code here
		pass

	def _physics_process(self, delta: float) -> None:
		#check if there is a target
		#check if the slime can mvoe
		#check if the slime is moving
		if(self.animated_body.frame == 0 or self.animated_body.frame >= 6):
			self._can_move = False
			self.target_angle = self.position.angle_to_point(self.target.position)
		else:
			self._can_move = True
			
		
		if(self.has_target() and self.can_move()):
			move_direction = Vector2.RIGHT.rotated(self.target_angle)
			velocity = move_direction * self.speed
			self.position += velocity * delta
		
		pass
		# if self.target != None and self._can_move:
		# 	angle = self.position.angle_to_point(self.target.position) # get angle to player
		# 	direction = Vector2.RIGHT.rotated(angle)# get direction to player
		# 	velocity = direction * self.speed # sets speed
		# 	self.position += velocity*delta #moves position depending on time between frames or delta 
		# pass

	def has_target(self) -> bool:
		return self.target != None
	def can_move(self) -> bool:
		return self._can_move
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
