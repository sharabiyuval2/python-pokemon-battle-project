from copy import deepcopy
from Pokemon import Pokemon
class Trainer():
    def __init__(self, name, age,exp_modifier,pokemons_list = None):
        if not isinstance(name,str):
            raise TypeError("name must be str")
        self.__name = name

        if not isinstance(age,int):
            raise TypeError("trainer age must be int")
        if not 16 <= age <= 120:
            raise ValueError("trainer age must be 16-120")
        self.__age = age

        if not isinstance(exp_modifier,float):
            raise TypeError("exp_modifier must be float")
        if not 1.5 <= exp_modifier <= 12.5:
            raise ValueError("exp modifier must be 1.5-12.5")
        self.__exp_modifier = exp_modifier

        if pokemons_list == None:
            pokemons_list = []
        if not isinstance(pokemons_list, list):
            raise TypeError("pokemon list must be list")
        for pokemon in pokemons_list:
            if not isinstance(pokemon, Pokemon):
                raise TypeError("list must be made of pokemons")
        self.__pokemon_list = pokemons_list

    def get_pokemon_lst(self):
        return deepcopy(self.__pokemon_list)

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_exp_modifier(self):
        return self.__exp_modifier

    def __len__(self):
        return len(self.get_pokemon_lst())

    def __repr__(self):
        str1 = "The Trainer " + self.get_name() + " is " + str(self.get_age()) + " years old and has the following pokemons (" + str(len(self.get_pokemon_lst())) + " in total):"
        for pokemon in self.get_pokemon_lst():
            str1 += "\n    " + str(pokemon)
        return str1

    def change_pokemon_lst(self, pokemon, pokemon_id):
        if pokemon_id < 0 or pokemon_id >= len(self):
            raise ValueError("pokemon_id value is not ok")
        if not isinstance(pokemon,Pokemon):
            raise TypeError("pokemon type must be pokemon")
        self.__pokemon_list[pokemon_id] = pokemon

    def catch_pokemon(self,pokemon):
        capture_chances = ((pokemon.get_catch_rate() * self.get_exp_modifier() * (100 - pokemon.get_hit_points())/100)/100)
        if capture_chances > 0.5:
            self.__pokemon_list.append(pokemon)
            print(self.get_name() + " caught " + pokemon.get_name())
        else:
            print(self.get_name() + " couldn't catch " + pokemon.get_name())

    def total_hp(self):
        total_hp = 0
        for pokemon in self.get_pokemon_lst():
            total_hp += pokemon.get_hit_points()
        return total_hp

    #comparation operators
    def __eq__(self,other):
        if self.total_hp() == other.total_hp():
            return True
        else:
            return False

    def __ne__(self, other):
        if self.total_hp() != other.total_hp():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.total_hp() > other.total_hp():
            return True
        else:
            return False

    def __lt__(self, other):
        if self.total_hp() < other.total_hp():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.total_hp() >= other.total_hp():
            return True
        else:
            return False

    def __le__(self, other):
        if self.total_hp() <= other.total_hp():
            return True
        else:
            return False

    def __add__(self, other):
        new_name = ""
        if self.total_hp() >= other.total_hp():
            new_name = self.get_name() + "-" + other.get_name()
        else:
            new_name = other.get_name() + "-" + self.get_name()
        new_age = (self.get_age() + other.get_age())//2
        new_experience = (self.get_exp_modifier() + other.get_exp_modifier())/2
        new_pokemon_list = []
        if self.total_hp() >= other.total_hp():
            new_pokemon_list = self.get_pokemon_lst() + other.get_pokemon_lst()
        else:
            new_pokemon_list = other.get_pokemon_lst() + self.get_pokemon_lst()
        return Trainer(new_name, new_age, new_experience, new_pokemon_list)


    # def deal_most_dmg(self,pokemon):
    #     dmg = []
    #     for poke in self.get_pokemon_lst():
    #         dmg.append(poke.get_damage(pokemon))
    #     maxim = max(dmg)
    #     return dmg.index(maxim)










