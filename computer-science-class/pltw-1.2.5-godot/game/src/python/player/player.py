import json
from py4godot import gdclass
from py4godot.classes.Engine import Engine
from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.Node2D import Node2D
from py4godot.classes.Input import Input
from py4godot.classes.core import PackedStringArray, Vector2
from py4godot.enums.enums import Key

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
    __multy_shot: int = 0 # the amount of extra projectiles the player can shoot


    #exp
    __exp: float = 0.0
    __exp_for_next_level: float = 100.0

    __exp_modifier: float = 1.0
    
    # other
    __selected_cards = 0
    __unselected_cards = 0
    __cards: list = []
    __input_instance: Input = Input().instance()

    def _ready(self) -> None:
        pass

    def _process(self, delta: float) -> None:
        if(self.is_selecting_card()):
            Engine.instance().set_time_scale(0)
        else:
            Engine.instance().set_time_scale(1)
        
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

        if(self.__input_instance.is_key_pressed(Key.KEY_A)):
            position_change.x += 1
            self.get_children()[0].flip_h = True

        self.__moving = True if(position_change.x != 0 and position_change.y != 0) else False

        

        return super()._physics_process(delta)
    
    def _input(self, event: InputEvent) -> None:

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
                    self.__health_modifier += float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "multy_shot"):
                    self.__multy_shot = self.__multy_shot + int(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "collection_range"):	
                    self.__collection_range_modifier = self.__collection_range_modifier + float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "exp_gain"):
                    self.__exp_modifier = self.__exp_modifier + float(stat_as_dict.get("change"))
                elif(stat_as_dict.get("stat") == "attack_size"):
                    self.__attack_size = self.__attack_size + float(stat_as_dict.get("change"))
        
    

