from Pokemon import Pokemon
from abc import ABC, abstractmethod
from copy import deepcopy

class Water(Pokemon):
    def __init__(self, name, catch_rate, pokemon_type):
        super().__init__(name, catch_rate)
        if pokemon_type != "water":
            raise ValueError("pokemon type must be water")
        self.__pokemon_type = pokemon_type
        self.__effective_against_me = ["electric"]
        self.__effective_against_others = ["fire"]

    def get_pokemon_type(self):
        return self.__pokemon_type

    def get_effective_against_me(self):
        return deepcopy(self.__effective_against_me)

    def get_effective_against_others(self):
        return deepcopy(self.__effective_against_others)

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def absorb(self, damage):
        pass

    @abstractmethod
    def attack(self, other):
        pass

    @abstractmethod
    def can_fight(self):
        pass

    @abstractmethod
    def get_damage(self,other):
        pass

    @abstractmethod
    def get_defence_power(self):
        pass

    @abstractmethod
    def get_hit_points(self):
        pass

    @abstractmethod
    def level_up(self, level_gain):
        pass


