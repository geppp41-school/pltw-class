from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector3
from py4godot.classes.Control import Control
from py4godot.classes.AnimatedSprite2D import AnimatedSprite2D

@gdclass
class start_screen(Control):

	# define properties like this
	

	# define signals like this
	test_signal = signal([SignalArg("test_arg", int)])


	def _ready(self) -> None:
		self.background = self.get_node("background")
		self.screen_player:AnimatedSprite2D = self.get_node("sprite")
		self.screen_player.play("moving")
		self.world =  ResourceLoader.instance().load("res://scene/game.tscn")
		self.playing = True
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		if(self.playing):
			if(self.background != None):
				self.background.texture.noise.offset += Vector3.new3(32*delta, 0, 0)
		
		pass

	
		

	def pause(self):
		self.background.texture.noise.offset = Vector3.new3(0,0,0)
		self.screen_player.stop()
		self.screen_player.frame = 0
		self.playing = False
		self.visible = False
		self.hide()

	def resume(self):
		self.playing = True
		self.screen_player.play("moving")
		self.visible = True
		self.show()

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
