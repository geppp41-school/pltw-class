from py4godot import gdclass
from py4godot.classes.InputEvent import InputEvent
from py4godot.classes.Node2D import Node2D

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
    __cards: list = []

    def _ready(self) -> None:
        pass

    def _process(self, delta: float) -> None:
        return super()._process(delta)
    
    def _physics_process(self, delta: float) -> None:
        return super()._physics_process(delta)
    
    def _input(self, event: InputEvent) -> None:
        return super()._input(event)
    
    def add_card(self, card):
        """
        used to add a card to the players selected cards

        :param card: the card to be added to the list of cards the player has
        """
        pass

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
        
        pass

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

