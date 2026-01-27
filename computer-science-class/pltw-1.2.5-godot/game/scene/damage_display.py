
import math
from py4godot.methods import private
from py4godot.signals import signal, SignalArg
from py4godot.classes import gdclass
from py4godot.classes.core import Vector2
from py4godot.classes.Node2D import Node2D
from py4godot.classes.RichTextLabel import RichTextLabel
from py4godot.classes.Label import Label
from py4godot.classes.core import Color

@gdclass
class damage_display(Node2D):

	life_span = 5
	time_passed = 0
	

	def _ready(self) -> None:
		self.modulate.a = 155
		pass
		# put initialization code here

	def _process(self, delta:float) -> None:
		#self.modulate.a = 255*(self.time_tell_despawn/3)
		
		## makes the damage display slowly fade 
		self.time_passed += delta
		self.modulate = Color.new4(1.0, 1.0, 1.0, ((255*(math.pow(math.e, -2*self.time_passed)))/255))
		
		
		
		#self.modulate.a = ((255*(math.pow(math.e, -2.8*self.time_passed)))/255)
		#print(self.modulate.a)
		
		if(self.time_passed >= self.life_span):
			self.queue_free()
			
		pass
		# put dynamic code here

	def set_damage_display_text(self, damage: float, position, doged):
		## moves the damage display and sets its text
		self.position = position
		self.get_node("Label").text = str(round(damage, 2)) if not doged else "missed"
		
		pass

	# Hide the method in the godot editor
	@private
	def test_method(self):
		pass
