from abc import ABC, abstractmethod
class Pokemon(ABC):
    def __init__(self,name,catch_rate):
        #input check
        if not isinstance(name, str):
            raise TypeError("pokemon name must be a str")
        if not isinstance(catch_rate,int):
            raise TypeError("pokemon catch rate must be int")
        if not 40 <= catch_rate <= 45:
            raise ValueError("catch rate must be 40-45")

        self.__name = name
        self.__catch_rate = catch_rate

    def get_name(self):
        return self.__name
    def get_catch_rate(self):
        return self.__catch_rate

    @abstractmethod
    def __repr__(self):
        pass
    @abstractmethod
    def absorb(self,damage):
        pass
    @abstractmethod
    def attack(self, other):
        pass
    @abstractmethod
    def can_fight(self):
        pass
    @abstractmethod
    def get_damage(self, other):
        pass
    @abstractmethod
    def get_defence_power(self):
        pass
    @abstractmethod
    def get_effective_against_me(self):
        pass
    @abstractmethod
    def get_effective_against_others(self):
        pass
    @abstractmethod
    def get_hit_points(self):
        pass
    @abstractmethod
    def get_pokemon_type(self):
        pass
    @abstractmethod
    def level_up(self, level_gain):
        pass






