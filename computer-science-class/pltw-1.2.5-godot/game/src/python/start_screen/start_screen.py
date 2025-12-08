from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Control import Control

@gdclass
class start_screen(Control):

	# define properties like this
	

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.background = self.get_node("background")
		self.screen_player = self.get_node("sprite")
		self.screen_player.play("moving")
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		if(self.background != None):
			self.background.texture.noise.offset += Vector3.new3(0.04, 0, 0)
		pass
		# put dynamic code here

	def _on_play_button_pressed(self):
		print("Button was pressed")
		pass
	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
