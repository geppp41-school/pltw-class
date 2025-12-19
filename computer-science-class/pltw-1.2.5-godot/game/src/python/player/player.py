import json
import math
from py4godot.classes.Area2D import Area2D
from py4godot.classes.CanvasItemMaterial import CanvasItemMaterial
from py4godot.classes.Engine import Engine
from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.InputEventMouseMotion import InputEventMouseMotion
from py4godot.classes.Material import Material
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.functions import print_verbose
from py4godot.methods import private
from py4godot.classes import gdclass
from py4godot.classes.Sprite2D import Sprite2D
from py4godot.classes.core import PackedStringArray, Vector2
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
	health_modifier: float = 1.0
	max_health: int = 100
	armor : float = 100
	modifiers: list = []
	input_instance: Input = Input().instance()
	_moving:bool = False
	cooldown:float = 2.0
	attack_cooldown:float = 2.0
	cooldown_modifier:float = 1.0
	exp: float = 5000000.0
	exp_modifier:float = 1.0
	exp_to_next_level: float = 100.0
	base_damage: float = 50.0
	damage: float = 50.0
	damage_modifier:float = 1.0
	level: int = 1
	luck: int = 0
	selecting_card = False
	collection_range: float = 50
	collection_range_modifier: float = 1.1
	multy_shot: int = 0
	remaining_projectiles:int = 1
	attack_size = 1.0


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
		self.cooldown = min(self.cooldown, self.attack_cooldown*self.cooldown_modifier)

		self.get_node("pickup_range").get_node("CollisionShape2D").shape.set_radius(self.collection_range*self.collection_range_modifier)
		
		self.aim_wheel_shader.set_shader_parameter("fill_percent", round(self.cooldown/(self.attack_cooldown*self.cooldown_modifier), 2))
		
		self.aim_wheel_shader = self.aim_wheel.get_material()
		if(self.exp >= self.exp_to_next_level and not self.selecting_card):
			self.selecting_card = True
			self.level += 1
			self.exp -= self.exp_to_next_level
			#self.exp_to_next_level = ((25/2)*pow(self.level, 2))+((10-(25/2))*self.level)
			self.exp_to_next_level = 100.0*(pow(1.25, self.level-1))
			self.add_child(self.level_up_menu.instantiate())
			
		self.exp_bar.set_size(Vector2.new3(200*(self.exp/self.exp_to_next_level), self.exp_bar.size.y))
		
		
		if(self.exp_bar.size.x > 0):

			new_bar_position = Vector2.new3(60+((200-self.exp_bar.size.x)/2), self.exp_bar.position.y)
			self.exp_bar.set_position(new_bar_position)

		if(self.cooldown >= self.attack_cooldown*self.cooldown_modifier and self.remaining_projectiles <= 0):
			self.remaining_projectiles = 1+self.multy_shot
		
		
		
		
		#self.aim_wheel.transform.rotated(self.aim_wheel.get_angle_to(self._mouse_position))
		pass


	
	def _input(self, event: InputEvent) -> None:
		if(event.get_type() == InputEventMouseMotion.get_type() and not self.selecting_card):
			eventMouseMotion:InputEventMouseMotion = InputEventMouseMotion.cast(event)
			test = eventMouseMotion.position-Vector2.new3(320,240)
			#print(math.atan(test.y/test.x))
			self._mouse_position = eventMouseMotion.position-Vector2.new3(320,240)
		elif(event.get_type() == InputEventMouseButton.get_type() and not self.selecting_card):
			eventMouseButton:InputEventMouseButton = InputEventMouseButton.cast(event)
			#print(f"{eventMouseButton.as_text()}: {eventMouseButton.is_pressed()}, {eventMouseButton.get_button_index()}")
			#button indexes |  1: left mouse button | 2: right mouse button | 3: scroll wheel press | 4-5 scrolling up and down
			if(eventMouseButton.is_pressed() and eventMouseButton.get_button_index() == 1 and self.cooldown >= self.attack_cooldown*self.cooldown_modifier):
				projectile:Node2D = self.fireball.instantiate()
				if(self.get_parent() != None):
					self.get_parent().add_child(projectile)
				else:
					self.add_child(projectile)
				projectile.set_meta("speed", 100)
				projectile.set_meta("direction",self.aim_wheel.get_rotation()-(math.pi/2))
				projectile.set_meta("damage", self.damage*self.damage_modifier)
				projectile.set_meta("size", self.attack_size)
				print(projectile.get_meta("size"))
				self.remaining_projectiles = self.remaining_projectiles -1
				
				if(self.remaining_projectiles == 0):
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
			self.exp += area.get_parent().get_meta("exp_value")*self.exp_modifier
			area.get_parent().set_meta("collected", True)
			pass
		pass

	def get_luck(self):
		return self.luck
	
	def add_card(self, rarity, stats):
		self.modifiers.append({"rarity": rarity, "stats": stats})
		Engine.instance().set_time_scale(1)
		self.get_children().pop_back().queue_free()
		self.process_buffs()
		print("selected buff")
		self.selecting_card = False
		


	def process_buffs(self):
		self.exp_modifier = 1.0
		self.damage_modifier = 1.0
		self.damage = 50.0
		self.cooldown_modifier = 1.0
		self.health_modifier = 1.0
		self.collection_range_modifier = 1.0
		self.multy_shot= 0
		self.attack_size = 1.0
		
		for i in range(len(self.modifiers)):
			object:dict[str, PackedStringArray | str] = self.modifiers[i]
			stats:PackedStringArray = object.get("stats") # type: ignore
			for x in range(stats.size()):
				print(x)
				print(stats.get(x))
				stat_as_dict = json.loads(stats.get(x))
				if(stat_as_dict.get("stat") == "attack_cd"):
					self.cooldown_modifier = self.cooldown_modifier - float(stat_as_dict.get("change"))
					self.cooldown_modifier = max(self.cooldown_modifier, 0.25)
				elif(stat_as_dict.get("stat") == "damage"):
					if(float(stat_as_dict.get("change")) > 1):
						self.damage = self.damage + float(stat_as_dict.get("change"))
					else:
						self.damage_modifier = self.damage_modifier + float(stat_as_dict.get("change"))
				elif(stat_as_dict.get("stat") == "hp"):
					self.health_modifier += float(stat_as_dict.get("change"))
				elif(stat_as_dict.get("stat") == "multy_shot"):
					self.multy_shot = self.multy_shot + int(stat_as_dict.get("change"))
					print(stat_as_dict.get("change"))
				elif(stat_as_dict.get("stat") == "collection_range"):	
					self.collection_range_modifier = self.collection_range_modifier + float(stat_as_dict.get("change"))
				elif(stat_as_dict.get("stat") == "exp_gain"):
					self.exp_modifier = self.exp_modifier + float(stat_as_dict.get("change"))
				elif(stat_as_dict.get("stat") == "attack_size"):
					self.attack_size = self.attack_size + float(stat_as_dict.get("change"))
					print(self.attack_size)
			print(f"collection_range: {self.collection_range_modifier}")


	@private
	def test_method(self):
		pass
