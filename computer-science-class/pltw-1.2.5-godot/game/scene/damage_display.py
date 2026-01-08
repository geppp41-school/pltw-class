
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector2
from py4godot.classes.Node2D import Node2D
from py4godot.classes.RichTextLabel import RichTextLabel

@gdclass
class damage_display(Node2D):

	time_tell_despawn = 3
	text_node: RichTextLabel = RichTextLabel()

	def _ready(self) -> None:
		self.text_node = self.get_node("TextLabel")
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		#self.modulate.a = 255*(self.time_tell_despawn/3)
		self.time_tell_despawn -= delta
		if(self.time_tell_despawn <= 0):
			self.queue_free()
			
		pass
		# put dynamic code here

	def set_damage_display_text(self, damage: float, position):
		self.position = position
		self.text_node.append_text(str(damage))
		
		pass

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
