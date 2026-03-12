from Charmeleon import Charmeleon
from Charmander import Charmander
from Charizard import Charizard
from Pikachu import Pikachu
from Wartortle import Wartortle
from Blastoise import Blastoise
from Squirtle import Squirtle
from Trainer import Trainer
from Battle import Battle

charmilious = Charmeleon("charmilious", 42, "fire", 19, 60, 71, 68)
warty = Wartortle("warty", 43, "water", 30, 78, 80, 93)
pika = Pikachu("pika", 40, "electric", 32, 35, 60, 40, 2)
charzy = Charizard("charzy", 45, "fire", 35, 95, 94, 83)
ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
charizardious = Charizard("charizardious", 45, "fire", 37, 93, 93,
82)
squirtly = Squirtle("squirtly", 41, "water", 9, 55, 49, 72)
blasty = Blastoise("blasty", 43, "water", 37, 82, 93, 113)
charmy = Charmander("charmy", 41, "fire", 15, 57, 63, 44)
misty = Trainer("misty", 18, 5.5, [charizardious, squirtly, blasty, charmy])
battle = Battle(misty, ash)
battle.total_battle()
print(misty)
print(ash)
ash = Trainer("ash", 18, 6.0, [charmilious, warty, pika, charzy])
misty = Trainer("misty", 18, 5.5, [charizardious, squirtly,
blasty, charmy])
battle = Battle(ash, misty)
battle.total_battle()
print(misty)
print(ash)

