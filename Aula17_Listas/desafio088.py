'''
- Faça um programa que:

    Ajude um jogador da mega sena a criar palpites

    O programa vai:

        1) Perguntar quantos jogos serão gerados

        2) sortear 6 números entre 1 e 60 para cada jogo

        3) cadastrando tudo em uma lista composta

'''
from time import sleep
from random import randint

cont = 0
lista_jogos = []
jogos = []

print('-' * 40)
print(f'\n  SORTEADOR DE NÚMEROS DA MEGA SENA    \n')
print('-' * 40, '\n')

num_jogos = int ( input ( 'Quantos Jogos você quer Sortear? ' ) )

total = 1
while total <= num_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista_jogos: 
            lista_jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    lista_jogos.sort()
    jogos.append(lista_jogos[:])
    lista_jogos.clear()
    total += 1

sleep(0.5)    
print('\n', '-=' * 3, f' SORTEANDO {num_jogos} JOGO(s) ', '-=' * 3, '\n')

sleep(2)
for indice , lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)