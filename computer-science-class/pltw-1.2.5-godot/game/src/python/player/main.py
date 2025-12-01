
from py4godot.functions import print_verbose
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.core import Vector2
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Input import Input
from py4godot.enums.enums import Key

@gdclass
class main(Node2D):

	# define properties like this
	speed: int = 32
	health: int = 100
	max_health: int = 100
	modifiers: dict = {}
	input_instance: Input = Input().instance()
	_moving:bool = False


	def _ready(self) -> None:
		
		
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass


		# put dynamic code here
	def _physics_process(self, delta: float) -> None:
		positiopnChange = Vector2.new3(0,0)
		
		if(self.input_instance.is_key_pressed(Key.KEY_W)):
			positiopnChange.y -= 1
		if(self.input_instance.is_key_pressed(Key.KEY_S)):
			positiopnChange.y += 1
		if(self.input_instance.is_key_pressed(Key.KEY_A)):
			positiopnChange.x -= 1
			self.get_children()[0].flip_h = True
		if(self.input_instance.is_key_pressed(Key.KEY_D)):
			positiopnChange.x += 1
			self.get_children()[0].flip_h = False

		if(positiopnChange.x == 0 and positiopnChange.y == 0):
			self.__moving = False
		else:
			self.__moving = True

		self.position += (positiopnChange.normalized()*delta) * self.speed
		return super()._physics_process(delta)
	
	def is_moving(self) -> bool:
		return self.__moving
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
