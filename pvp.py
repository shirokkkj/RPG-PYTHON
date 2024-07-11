from npcs.monsters import *
from player.player import *
from xispe.xispe import *
from random import choice

def cabecalho():
        print('''
  ____ ___  __  __ ____    _  _____  
 / ___/ _ \|  \/  | __ )  / \|_   _| 
| |  | | | | |\/| |  _ \ / _ \ | |   
| |__| |_| | |  | | |_) / ___ \| |   
 \____\___/|_|  |_|____/_/   \_\_|.  
''')
        print('''
[1] - ATACAR
[2] - DEFENDER                   
[3] ESQUIVAR
''')

cabecalho()

bardo = bardo
combat_monster = lista_de_monstros[0]

while combat_monster['Life'] >= 0 and bardo.vida >= 0:
    esquiva = ['Esquivou', 'Não esquivou']
    choice_esquiva = choice(esquiva)

    acertou = [True, False]
    choice_acerto = choice(acertou)

    defendeu = [True, False]
    choice_defendeu = choice(defendeu)
    
    def escolha(monster):
        if op == 1:
                if choice_acerto:
                    monster['Life'] -= bardo.dano
                    return print(f'VIDA ATUAL DO MONSTRO: {monster['Life']}')
                else: 
                    bardo.vida -= monster['Dano']
                    return print(f'VOCÊ ERROU E FOI ACERTADO! SUA VIDA É: {bardo.vida}')
        if op == 2:
            if choice_defendeu:
                bardo.vida = bardo.vida
                return print('VOCÊ DEFENDEU! 0 DE DANO TOMADO!')
            else:
                bardo.vida -= monster['Dano']
                return print(f'O monstro te acertou! Sua vida agora é: {bardo.vida}')
        if op == 3:
            if choice_esquiva == 'Esquivou':
                bardo.vida = bardo.vida
                return print('VOCÊ ESQUIVOU! 0 DE DANO TOMADO!')
            else:
                bardo.vida -= monster['Dano']
                return print(f'O monstro te acertou! Você agora tem: {bardo.vida}')

    op = int(input(''))
   
    def combate():
        print(' B A R D O!')
        print('---' * 10)
        print(bardo.nome, bardo.vida, bardo.classe, bardo.dano)
        print('---' * 10)        
        escolha(combat_monster)
    combate()

if bardo.vida > 0:
    if monster['Level'] > 50:
         bardo.xp += 30
    else:
         bardo.xp += 10
    print(f'VOCÊ GANHOU! SEU XP AGORA É DE: {bardo.xp}')
else:
     print('Você morreu e não pôde ganhar XP.')
