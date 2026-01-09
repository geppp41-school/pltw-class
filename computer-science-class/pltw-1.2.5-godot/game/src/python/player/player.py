import json
import math
from typing import get_type_hints
from py4godot import gdclass
from py4godot.classes.Area2D import Area2D
from py4godot.classes.Engine import Engine
from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.InputEventMouseButton import InputEventMouseButton
from py4godot.classes.InputEventMouseMotion import InputEventMouseMotion
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Input import Input
from py4godot.classes.Panel import Panel
from py4godot.classes.ResourceLoader import ResourceLoader
from py4godot.classes.ShaderMaterial import ShaderMaterial
from py4godot.classes.Sprite2D import Sprite2D
from py4godot.classes.core import PackedStringArray, Vector2
from py4godot.enums.enums import Key
from py4godot.classes.RayCast2D import RayCast2D

@gdclass
class player(Node2D):
    #base player stats

    #movement
    __speed: int = 32
    __moving: bool = False

    #hp stuff
    __hp: float = 100.0
    __max_hp: float = 100.0
    __armor: int = 100

    __hp_modifier: float = 1.0 # the modifier for the maximum hp of the player


    #attacks
    __attack_cooldown: float = 2.0 # the length of the cooldown
    __cooldown_time_passed: float = 2.0 # the time passed sience the last cooldown
    __remaining_projectiles: int = 1
    
    __cooldown_modifier = 1.0 # the duration modifier of the cooldown
    __damage_modifier: int = 0 # the amount of damage to be added to the base damage
    __damage_mutiplier: float = 1.0 # the amount that the damage should be mutiplied by 
    __attack_size_modifier: float = 1.0 # incrase the attack size of the fireball
    __multy_shot: int = 3 # the amount of extra projectiles the player can shoot

    __spread: float = 15


    #exp
    __exp: float = 0.0
    __exp_for_next_level: float = 100.0
    __level: int = 1
    __exp_modifier: float = 1.0
    __collection_range_modifier = 1.0
    
    # other
    __selected_cards = 0
    __unselected_cards = 0
    __last_unselected_card_count = 0
    __cards: list = []
    __input_instance: Input = Input().instance()

    __left_mouse_button_pressed = False

    def _ready(self) -> None:
        self.aim_wheel:Sprite2D = self.get_node("aim_wheel")
        self.fireball = ResourceLoader.instance().load("res://scene/projectiles/fireball.tscn")
        self.level_up_menu = ResourceLoader.instance().load("res://scene/Player/level_up.tscn")
        self.level_up_menu_instance = self.level_up_menu.instantiate()
        self.add_child(self.level_up_menu_instance)
        self.level_up_menu_instance.visible = False
        self._mouse_position = Vector2.new3(0,0)
        self.aim_wheel_shader:ShaderMaterial = self.aim_wheel.get_material()
        self.camera = self.get_node("Camera2D")
        self.exp_bar:Panel = self.camera.get_node("Hud").get_node("fill")


    def _process(self, delta: float) -> None:
        if(self.__collection_range_modifier*50 != self.get_node("pickup_range/hitbox").get_shape().radius):
            self.get_node("pickup_range/hitbox").get_shape().radius = self.__collection_range_modifier*50
        if(self.is_selecting_card()):

            Engine.instance().set_time_scale(0)
        else:
            Engine.instance().set_time_scale(1)


        relitive_mouse_position = self._mouse_position + self.position
        angle = self.get_angle_to(relitive_mouse_position)
        self.aim_wheel.rotation = (angle+(math.pi/2))
        self.__cooldown_time_passed += delta
        self.__cooldown_time_passed = min(self.__cooldown_time_passed, self.__attack_cooldown*self.__cooldown_modifier)

        self.aim_wheel_shader.set_shader_parameter("fill_percent", round(self.__cooldown_time_passed/(self.__attack_cooldown*self.__cooldown_modifier), 2))

        self.aim_wheel_shader = self.aim_wheel.get_material()
        if(self.__left_mouse_button_pressed and self.__cooldown_time_passed >= self.__attack_cooldown*self.__cooldown_modifier):
            self.fire_fireball(self.__multy_shot+1)
            self.__cooldown_time_passed = 0

        while self.__exp >= self.__exp_for_next_level:
           
            self.__unselected_cards += 1
            self.__level += 1
            self.__exp -= self.__exp_for_next_level
            self.__exp_for_next_level = 100.0*(pow(1.25, self.__level-1))
            self.__last_unselected_card_count = self.__unselected_cards
        
        
        if(self.__unselected_cards > 0):
            self.get_children().pop_back().visible = True # type: ignore
            # if(self.__last_unselected_card_count > self.__unselected_cards):
            #     self.__last_unselected_card_count = self.__unselected_cards
            #     self.level_up_menu_instance.call("roll_cards") # type: ignore
        elif(self.level_up_menu_instance.visible):
            self.level_up_menu_instance.visible = False
            self.process_buffs()



        self.exp_bar.set_size(Vector2.new3(200*(self.__exp/self.__exp_for_next_level), self.exp_bar.size.y))

        if(self.exp_bar.size.x > 0):
            new_bar_position = Vector2.new3(60+((200-self.exp_bar.size.x)/2), self.exp_bar.position.y)
            self.exp_bar.set_position(new_bar_position)

        

        
        
        return super()._process(delta)
    
    def _physics_process(self, delta: float) -> None:
        # movement handeling 
        position_change = Vector2.new3(0, 0)

        if(self.__input_instance.is_key_pressed(Key.KEY_W)):
            position_change.y -= 1

        if(self.__input_instance.is_key_pressed(Key.KEY_S)):
            position_change.y += 1

        if(self.__input_instance.is_key_pressed(Key.KEY_A)):
            position_change.x -= 1
            #flips the direction that the player is facing
            self.get_children()[0].flip_h = True

        if(self.__input_instance.is_key_pressed(Key.KEY_D)):
            position_change.x += 1
            self.get_children()[0].flip_h = False

        self.__moving = True if(position_change.x != 0 or position_change.y != 0) else False
        self.position += (position_change.normalized()*delta) * self.__speed
        

        return super()._physics_process(delta)
    
    def _input(self, event: InputEvent) -> None:
        if(event.get_type() == InputEventMouseMotion.get_type()):
            eventMouseMotion:InputEventMouseMotion = InputEventMouseMotion.cast(event)
            self._mouse_position = eventMouseMotion.position-Vector2.new3(320, 240)
            
        elif(event.get_type() == InputEventMouseButton.get_type()):
            eventMouseButton:InputEventMouseButton = InputEventMouseButton.cast(event)

            if(eventMouseButton.is_pressed() and eventMouseButton.get_button_index() == 1):
                self.__left_mouse_button_pressed = True
            elif(eventMouseButton.is_released() and eventMouseButton.get_button_index() == 1):
                self.__left_mouse_button_pressed = False

        # TODO: remake the aimwheel moving
        # TODO: remake the fireball shooting 

        return super()._input(event)
    

    

    def is_moving(self):
        """
        used to check if the player is moving
        """
        return self.__moving
    
    def get_damage_modifier(self):
        """
        used by attacks to get modifications to their base damage
        """
        return self.__damage_modifier
        
    
    def get_damage_mutiplier(self):
        """
        used by attacks to get the damage mutiplier
        """
        return self.__damage_mutiplier
    
    def get_attack_size_modifier(self):
        """
        used by attacks to get the modifier for attack size
        
        used by running varuable.call("get_attack_size_modifier", args)
        """
        return self.__attack_size_modifier
    
    # TODO: add create card 
    def add_card(self, stats):
        """
        used to add a card to the players selected cards

        :param stats: the card to be added to the list of cards the player has
        """
        self.__cards.append({"stats": stats})
        self.__unselected_cards -= 1
        self.__selected_cards += 1

    def is_selecting_card(self):
        return True if self.__unselected_cards > 0 else False


    

    def process_buffs(self):
        """
        used to process the buffs that come from the cards
        """

        self.__exp_modifier = 1.0
        self.__damage_modifier = 0
        self.__damage_mutiplier = 1.0
        self.__attack_size_modifier = 1.0
        self.__cooldown_modifier = 1.0
        self.__hp_modifier = 1.0
        self.__multy_shot = 0
        


        for item in self.__cards:
            stats:PackedStringArray = item.get("stats") # type: ignore
            for x in range(stats.size()):
                stat_as_dict = json.loads(stats.get(x))
                if(stat_as_dict.get("stat") == "attack_cd"):
                    self.__cooldown_modifier = self.__cooldown_modifier - float(stat_as_dict.get("change"))
                    self.__cooldown_modifier = max(self.__cooldown_modifier, 0.25)
                elif(stat_as_dict.get("stat") == "damage"):
                    if(float(stat_as_dict.get("change")) > 1):
                        self.__damage_modifier = self.__damage_modifier + float(stat_as_dict.get("change")) # type: ignore
                    else:
                        self.__damage_mutiplier = self.__damage_mutiplier + float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "hp"):
                    self.__hp_modifier += float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "multy_shot"):
                    self.__multy_shot = self.__multy_shot + int(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "collection_range"):	
                    self.__collection_range_modifier = self.__collection_range_modifier + float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "exp_gain"):
                    self.__exp_modifier = self.__exp_modifier + float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "attack_size"):
                    self.__attack_size_modifier = self.__attack_size_modifier + float(stat_as_dict.get("change"))
        
    def fire_fireball(self, count:int):
        projectiles = []
        for i in range(count):
            projectiles.append(self.fireball.instantiate())
        
        if(self.get_parent() != None):
            for i in range(count):
                self.get_parent().add_child(projectiles[i])
                
        else:
            for i in range(count):
                self.add_child(projectiles[i])

        for i in range(count):
            debug_direction = RayCast2D.new()
            debug_direction.target_position = Vector2.new3(0, -50)
            projectiles[i].call("set_speed", 100)
            
            
            projectiles[i].call(
                "set_direction", 
                self.aim_wheel.get_rotation()-(math.pi/2)-math.radians(self.__spread*(count/2.0)-(self.__spread*i))
            )
            debug_direction.rotation = self.aim_wheel.get_rotation()-math.radians(self.__spread*(count/2.0)-(self.__spread*i))
                #self.add_child(debug_direction)
                #print(f"spawning fireball {i} at angle {self.aim_wheel.get_rotation()+(self.__spread*(count/2)-(self.__spread*i))}")
                #projectiles[i].call("set_direction", self.aim_wheel.get_rotation()-((90/count)*(i+1)))
            projectiles[i].call("set_damage_modifier", self.__damage_modifier)
            projectiles[i].call("set_damage_mutiplier", self.__damage_mutiplier)
            projectiles[i].call("set_size", self.__attack_size_modifier)
        pass


    def _on_player_hitbox_area_entered(self, area:Area2D):
        if(area.get_name().contains("exp")):
            self.__exp += area.get_parent().call("get_exp_value")*self.__exp_modifier
            area.get_parent().call("collected")
        pass
    

