import math
from py4godot.classes.Area2D import Area2D
from py4godot.classes.CanvasItemMaterial import CanvasItemMaterial
from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.InputEventMouseMotion import InputEventMouseMotion
from py4godot.classes.Material import Material
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.functions import print_verbose
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.Sprite2D import Sprite2D
from py4godot.classes.core import Vector2
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Input import Input
from py4godot.enums.enums import Key
from py4godot.classes.ShaderMaterial import ShaderMaterial
from py4godot.classes.InputEventMouseButton import InputEventMouseButton
from py4godot.classes.Panel import Panel
from random import random


@gdclass
class player(Node2D):

	# define properties like this
	speed: int = 32
	health: int = 100
	max_health: int = 100
	armor : float = 100
	modifiers: list = []
	input_instance: Input = Input().instance()
	_moving:bool = False
	cooldown = 2.0
	attack_cooldown = 2.0
	exp: float = 45.0
	exp_to_next_level: float = 50.0
	level: int = 1
	luck: int = 0


	def _ready(self) -> None:
		self.aim_wheel:Sprite2D = self.get_node("aim_wheel")
		self.fireball = ResourceLoader.instance().load("res://scene/projectiles/fireball.tscn")
		self.level_up_menu = ResourceLoader.instance().load("res://scene/Player/level_up.tscn")
		self._mouse_position = Vector2.new3(0,0)
		self.aim_wheel_shader:ShaderMaterial = self.aim_wheel.get_material()
		self.camera = self.get_node("Camera2D")
		self.exp_bar:Panel = self.camera.get_node("Hud").get_node("fill")
		pass

	def _process(self, delta:float) -> None:
		relitive_mouse_position = self._mouse_position + self.position
		angle = self.get_angle_to(relitive_mouse_position)
		self.aim_wheel.set_rotation(angle+(math.pi/2))
		self.cooldown += delta
		self.cooldown = min(self.cooldown, self.attack_cooldown)
		
		self.aim_wheel_shader.set_shader_parameter("fill_percent", round(self.cooldown/self.attack_cooldown, 2))
		
		self.aim_wheel_shader = self.aim_wheel.get_material()
		if(self.exp >= self.exp_to_next_level):
			self.level += 1
			self.exp -= self.exp_to_next_level
			self.exp_to_next_level = ((50.0/2)*pow(self.level, 2))+((25.0-(50.0/2))*self.level)
			self.add_child(self.level_up_menu.instantiate())
			
		self.exp_bar.set_size(Vector2.new3(200*(self.exp/self.exp_to_next_level), self.exp_bar.size.y))
		
		
		if(self.exp_bar.size.x > 0):

			new_bar_position = Vector2.new3(60+((200-self.exp_bar.size.x)/2), self.exp_bar.position.y)
			self.exp_bar.set_position(new_bar_position)

		
		
		
		
		#self.aim_wheel.transform.rotated(self.aim_wheel.get_angle_to(self._mouse_position))
		pass


	
	def _input(self, event: InputEvent) -> None:
		if(event.get_type() == InputEventMouseMotion.get_type()):
			eventMouseMotion:InputEventMouseMotion = InputEventMouseMotion.cast(event)
			test = eventMouseMotion.position-Vector2.new3(320,240)
			#print(math.atan(test.y/test.x))
			self._mouse_position = eventMouseMotion.position-Vector2.new3(320,240)
		elif(event.get_type() == InputEventMouseButton.get_type()):
			eventMouseButton:InputEventMouseButton = InputEventMouseButton.cast(event)
			#print(f"{eventMouseButton.as_text()}: {eventMouseButton.is_pressed()}, {eventMouseButton.get_button_index()}")
			#button indexes |  1: left mouse button | 2: right mouse button | 3: scroll wheel press | 4-5 scrolling up and down
			if(eventMouseButton.is_pressed() and eventMouseButton.get_button_index() == 1 and self.cooldown >= self.attack_cooldown):
				projectile:Node2D = self.fireball.instantiate()
				if(self.get_parent() != None):
					self.get_parent().add_child(projectile)
				else:
					self.add_child(projectile)
				projectile.set_meta("speed", 100)
				projectile.set_meta("direction",self.aim_wheel.get_rotation()-(math.pi/2))
				
				self.cooldown = 0.0
			pass
			#self.aim_wheel_shader.set_shader_parameter("fill_percent", random())
		
			
		
		return super()._input(event)
	
	

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
	
	def _on_player_hitbox_area_entered(self, area:Area2D):
		if(area.get_name().contains("exp")):
			self.exp += area.get_parent().get_meta("exp_value")
			area.get_parent().set_meta("collected", True)
			pass
		pass

	def get_luck(self):
		return self.luck
	
	def add_card(self, rarity, stats):
		self.modifiers.append({"rarity": rarity, "stats": stats})

	@private
	def test_method(self):
		pass
