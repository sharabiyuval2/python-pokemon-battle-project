from Pokemon import Pokemon
from Charmeleon import Charmeleon
from Charmander import Charmander
from Charizard import Charizard
from Pikachu import Pikachu
from Wartortle import Wartortle
from Blastoise import Blastoise
from Squirtle import Squirtle
from Trainer import Trainer

class Battle():
    def __init__(self, trainer1, trainer2):
        if not isinstance(trainer1, Trainer):
            raise TypeError("trainer1 must be trainer")
        self.__trainer1 = trainer1

        if not isinstance(trainer2, Trainer):
            raise TypeError("trainer2 must be trainer")
        self.__trainer2 = trainer2

    def dual_battle(self,trainer1_pokemon_id, trainer2_pokemon_id):
        counter = 0
        poke1 = self.__trainer1.get_pokemon_lst()[trainer1_pokemon_id]
        poke2 = self.__trainer2.get_pokemon_lst()[trainer2_pokemon_id]
        while poke1.can_fight() and poke2.can_fight():
            # print("in round : " + str(counter))
            poke1.attack(poke2)
            if poke2.can_fight():
                poke2.attack(poke1)
            counter += 1
        self.__trainer1.change_pokemon_lst(poke1, trainer1_pokemon_id)
        self.__trainer2.change_pokemon_lst(poke2, trainer2_pokemon_id)
        if poke1.can_fight():
            return (counter, 1)
        elif poke2.can_fight():
            return (counter, 2)
        else:
            return (counter, 0)

    def num_of_poke_can_fight(self,trainer):
        can_fight = 0
        for poke in trainer.get_pokemon_lst():
            if poke.can_fight():
                can_fight += 1
        return can_fight

    def get_first_can_fight(self,trainer):
        for i in range(trainer.__len__()):
            if trainer.get_pokemon_lst()[i].can_fight():
                return i
        return -1

    def get_strongest_against(self,trainer,pokemon):
        max_damage = 0
        strongest_poke_index = -1
        for i in range(trainer.__len__()):
            if trainer.get_pokemon_lst()[i].can_fight() and trainer.get_pokemon_lst()[i].get_damage(pokemon) > max_damage:
                strongest_poke_index = i
                max_damage = trainer.get_pokemon_lst()[i].get_damage(pokemon)
        return strongest_poke_index

    def tie(self):
        poke1_index = self.get_first_can_fight(self.__trainer1)
        poke2_index = self.get_strongest_against(self.__trainer2, self.__trainer1.get_pokemon_lst()[poke1_index])
        return (poke1_index, poke2_index)

    def total_battle(self):
        total_rounds = 0
        winner = 0
        poke1_index, poke2_index = None, None
        while self.num_of_poke_can_fight(self.__trainer1) > 0 and self.num_of_poke_can_fight(self.__trainer2) > 0:
            if winner == 0: # tie
                poke1_index, poke2_index = self.tie()
            elif winner == 1: # poke1 win
                poke2_index = self.get_strongest_against(self.__trainer2, self.__trainer1.get_pokemon_lst()[poke1_index])
            else: # poke2 win - winner == 2
                poke1_index = self.get_strongest_against(self.__trainer1, self.__trainer2.get_pokemon_lst()[poke2_index])

            round_in_battle, winner = self.dual_battle(poke1_index, poke2_index)
            total_rounds += round_in_battle

        if self.num_of_poke_can_fight(self.__trainer1) == 0 and self.num_of_poke_can_fight(self.__trainer2) == 0:
            print("The battle ended with a draw")
            return
        if self.num_of_poke_can_fight(self.__trainer1) > 0:
            print("Trainer " + self.__trainer1.get_name() + " won the battle in " + str(total_rounds) + " rounds")
            return
        print("Trainer " + self.__trainer2.get_name() + " won the battle in " + str(total_rounds) + " rounds")








