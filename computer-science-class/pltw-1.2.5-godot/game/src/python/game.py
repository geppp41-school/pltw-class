from random import randint
from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.Node import Node
from py4godot.classes.core import Vector2


@gdclass
class game(Node):

	# define properties like this
	# define signals like this
	player:Node = Node.new()
	start_screen:Node = Node.new()
	spawned_enemies = 0

	def _ready(self) -> None:
		self.player = ResourceLoader.instance().load("res://scene/Player/player.tscn").instantiate()
		self.start_screen = ResourceLoader.instance().load("res://scene/start_screen.tscn").instantiate()
		self.world_one = ResourceLoader.instance().load("res://scene/worlds/world_one.tscn").instantiate()
		
		self.add_child(self.start_screen)
		#self.get_node("start_screen").get_node("play_button").connect("pressed", self.play)
		self.play_button = self.get_node("start_screen").get_node("play_button")
		self.play_button.pressed.connect(self.play)

		self.slime_scene = ResourceLoader.instance().load("res://scene/enemy/slime/slime.tscn")
		
		
		
		
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here

	def _input(self, event: InputEvent) -> None:
		return super()._input(event)
	
	def play(self):
		print("play button was pressed")
		self.start_screen.queue_free()
		self.add_child(self.world_one)
		self.add_child(self.player)
		
		pass

	def spawn_slime(self, player_position):
		if(self.spawned_enemies < 1000):
			slime = self.slime_scene.instantiate()
			slime.position = player_position + Vector2.new3(randint(300, 500), 0).rotated(randint(0, 360))
			self.add_child(slime)

	def enemy_died(self):
		self.spawned_enemies -= 1

	def get_player(self):
		return self.player

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
