from Water import Water
from Charizard import Charizard
from Blastoise import Blastoise

class Wartortle(Water):
    def __init__(self, name, catch_rate, pokemon_type, level, hit_points, attack_power, defense_power):
        super().__init__(name,catch_rate,pokemon_type)
        if not isinstance(level,int):
            raise TypeError("level must be int")
        if not 16 <= level <= 31:
            raise ValueError("Wartortle level must be 16-31")
        self.__level = level

        if not isinstance(hit_points,int):
            raise TypeError("hitpoints must be int")
        if not 59 <= hit_points <= 78:
            raise ValueError("Wartortle hitpoints must be 59-78")
        self.__starting_life = hit_points
        self.__hit_points = hit_points

        if not isinstance(attack_power,int):
            raise TypeError(" attackpower must be int")
        if not 63 <= attack_power <= 82:
            raise ValueError("Wartortle attackpower must be 63-82")
        self.__attack_power = attack_power

        if not isinstance(defense_power,int):
            raise TypeError("defense_power must be int")
        if not 80 <= defense_power <= 99:
            raise ValueError("Wartortle defencepower must be 80-99")
        self.__defence_power = defense_power

    def get_starting_life(self):
        return self.__starting_life
    def get_level(self):
        return self.__level
    def get_hit_points(self):
        return self.__hit_points

    def get_defence_power(self):
        return self.__defence_power
    def get_attack_power(self):
        return self.__attack_power

    def __repr__(self):
        return "The Wartortle " + self.get_name() + " of level " + str(self.get_level()) + " with " + str(self.get_hit_points()) + " HP"

    def can_fight(self):
        if self.get_starting_life()//10 < self.get_hit_points():
            return True
        else:
            return False

    def get_damage(self, other):
        if self.get_pokemon_type() in other.get_effective_against_me():
            return int((((2*self.get_level()/5)+2)*(self.get_attack_power()/other.get_defence_power())*2)-1)
        else:
            return int((((2*self.get_level()/5)+2)*(self.get_attack_power()/other.get_defence_power())*0.5)-1)

    def attack(self,other):
        if self.can_fight() and other.can_fight():
            self.__hit_points -= self.get_starting_life()//10
            other.absorb(self.get_damage(other))

    def absorb(self, damage):
        self.__hit_points -= damage

    def level_up(self, level_gain):
        if not isinstance(level_gain, int):
            raise TypeError("level gain must be int")
        if 1 <= level_gain <= 16:
            self.__level += level_gain
            if self.get_level() > 31:
                return self.evolve()

    def evolve(self):
        HP = max(self.get_hit_points()+20, 80) #check if need to be 20/15
        return (Blastoise(self.get_name(),self.get_catch_rate(), self.get_pokemon_type(), self.get_level(), HP, self.get_attack_power()+20, self.get_defence_power()+20))















