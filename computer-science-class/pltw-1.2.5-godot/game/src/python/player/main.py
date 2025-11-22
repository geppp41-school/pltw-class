
from py4godot.functions import print_verbose
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.Input import Input
from py4godot.enums.enums import Key
from py4godot.classes.core import Vector2, Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.signals import signal, SignalArg
@gdclass
class main(Node2D):

	speed: int = 16
	maxHealth: int = 100
	health: int = 100
	


	def _ready(self) -> None:
		self.input_instance = Input.instance()
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		moveVector:Vector2 = Vector2.new3(0,0)
		
		if(self.input_instance.is_physical_key_pressed(Key.KEY_W)):
			moveVector.y -= 1
		if(self.input_instance.is_physical_key_pressed(Key.KEY_A)):
			moveVector.x -= 1
		if(self.input_instance.is_physical_key_pressed(Key.KEY_S)):
			moveVector.y += 1
		if(self.input_instance.is_physical_key_pressed(Key.KEY_D)):
			moveVector.x += 1
		
		self.position += (moveVector*delta)*self.speed
		
		# put dynamic code here
	
	
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
