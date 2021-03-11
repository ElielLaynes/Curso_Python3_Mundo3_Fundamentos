'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. 

- O programa vai ler o nome do jogador e quantas partidas ele jogou. 
- Depois vai ler a quantidade de gols feitos em cada partida. 

No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

'''

jogador = dict()
partidas = list()

jogador['nome'] = str( input( 'Nome do Jogador: ' ))
total = int( input( f'Quantas Partidas o {jogador["nome"]} Jogou? ' ))

for p in range(0, total):
    partidas.append( int( input( f'Quantos Gols fez na partida {p + 1}: ' )))

print()
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)

print()
for c, v in jogador.items():
    print(f'O campo {c} tem valor {v}.')

print()
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

print()
for item, valor in enumerate(jogador['gols']):
    print(f'na partida {item + 1} fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print()