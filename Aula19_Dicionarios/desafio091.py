''''
Crie um programa onde:

    - 4 Jogadores joguem um dado e tenha resultados ALEATÓRIOS(random)
    - Guarde esses resultados em um dicionário

    No final:

    - Coloque esse dicionário em ORDEM(Pesquisar como fazer isso)
    - Sabendo que o VENCEDOR tirou o MAIOR NÚMERO no dado.

'''

from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
rank = list()

jogadores['jogador_1'] = randint(1, 6)
jogadores['jogador_2'] = randint(1, 6)
jogadores['jogador_3'] = randint(1, 6)
jogadores['jogador_4'] = randint(1, 6)

# Resultado das jogas
print()
print('Jogadores escolhendo Seus Números:', '\n')
sleep(1.5)
for jogador, jogada in jogadores.items():
    print(f'O {jogador} jogou: {jogada}')
    sleep(1)

# Colocando a lista em ordem de valores
# A função itemgetter ordena em chaves(0) e valores(1)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)


print('\nRanking de Vitória: \n')
sleep(2)
#Printando o ranking e qual jogador venceu
for item, valor in enumerate(rank):
    print(f'{item + 1}º lugar: {valor[0]} com {valor[1]} \n')
    