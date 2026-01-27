
import queue
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Sprite2D import Sprite2D
from random import randint
import math

@gdclass
class world(Sprite2D):

	# define properties like this
	test_int: int = 5
	test_float: float = 5.2
	test_bool: bool = True
	test_vector: Vector3 = Vector3.new3(1,2,3)

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.parent = self.get_parent()
		self.player = self.get_parent().get_node("player")
		self.time_passed = 0
		self.current_play_time = 0


		print(self.get_parent())
		
		for i in range(100):
			self.parent.call("spawn_slime", self.position)
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		if(self.player == None):
			self.player = self.get_parent().get_node("player")
		else:
			self.position = self.player.position
			self.texture.noise.offset = Vector3.new3(self.position.x, self.position.y, 0)

		self.time_passed += delta
		self.current_play_time += delta
		#makes more enemies spawn at once the longer the game has run for. also makes enemies spawn faster 
		if(self.time_passed >= 1.0*math.pow(0.9, self.current_play_time/60) ):
			for i in range(randint(1, round(self.current_play_time/20) if self.current_play_time > 20 else 1)):
				self.parent.call("spawn_slime", self.position)
				self.time_passed = 0.0
				


		pass
		# put dynamic code here

	
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
