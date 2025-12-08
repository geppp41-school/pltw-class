from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.Node import Node

@gdclass
class game(Node):

	# define properties like this
	# define signals like this
	player = None
	start_screen:Node = Node.new()

	def _ready(self) -> None:
		self.player = ResourceLoader.instance().load("res://scene/start_screen.tscn").instantiate()
		self.start_screen = ResourceLoader.instance().load("res://scene/start_screen.tscn").instantiate()
		self.add_child(self.start_screen)
		#self.get_node("start_screen").get_node("play_button").connect("pressed", self.play)
		self.play_button = self.get_node("start_screen").get_node("play_button")
		self.play_button.pressed.connect(self.play)
		
		
		
		
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		pass
		# put dynamic code here

	def _input(self, event: InputEvent) -> None:
		return super()._input(event)
	
	def play(self):
		self.start_screen.queue_free()
		print("Play was pressed")
		pass

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
