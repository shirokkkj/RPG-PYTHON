from random import randint

lista_de_monstros = []

def generate_monsters():
    level = randint(0, 150)
    monsters = {
        'Name':   f'Monstro #{level}',
        'Level':  level,
        'Dano':   level * 20,
        'Life':   level * 15
    }
    
    lista_de_monstros.append(monsters)

def criar_mais_monstro():
    for x in range(5):
        generate_monsters()

criar_mais_monstro()