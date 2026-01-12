import math
import random
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Node2D import Node2D
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.classes import PackedScene

@gdclass
class test(Node2D):

	# define properties like this
	test_int: int = 5
	test_float: float = 5.2
	test_bool: bool = True
	test_vector: Vector3 = Vector3.new3(1,2,3)
	player = None
	time_passed = 0.0
	

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.current_play_time= 0
		self.slimeScene = ResourceLoader.instance().load("res://scene/enemy/slime/slime.tscn")
		#self.fireball = ResourceLoader.instance().load("res://scene/projectiles/fireball.tscn").instantiate()
		self.add_child(ResourceLoader.instance().load("res://scene/Player/player.tscn").instantiate())
		self.exp = ResourceLoader.instance().load("res://scene/exp/green_exp.tscn")
		#self.add_child(self.exp.instantiate())
		self.player = self.get_node("player")
		self.enemies = 0
		
		for i in range(25):
			self.add_child(self.slimeScene.instantiate())
			self.enemies += 1
		#self.add_child(self.fireball)
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		self.time_passed += delta
		self.current_play_time += delta
		if(self.time_passed >= 2.0*math.pow(0.9, self.current_play_time/60) and self.enemies < 1000):
			for i in range(random.randint(1, round(min(self.current_play_time/20, 1000-self.enemies)) if self.current_play_time > 20 else 1)):
				self.add_child(self.slimeScene.instantiate())
				self.time_passed = 0.0
				self.enemies += 1
		pass
		# put dynamic code here
	def get_player(self):
		return self.player
	
	def enemy_died(self):
		self.enemies -= 1

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
