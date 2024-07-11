from random import randint
level = randint(0, 50)

class Player:
    def __init__(self, nome: str, idade: int, classe: str, dano: int, vida: int, xp: int):
        self.classe = classe
        self.idade  = idade
        self.nome   = nome
        self.dano   = dano
        self.vida   = vida
        self.xp     = xp

bardo = Player(nome='Bardinho Do Orion', idade=300, classe='Bardo', dano=randint(0, 1000), vida=100 * level, xp=5)