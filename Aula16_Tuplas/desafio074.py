
# Crie um programa que vai gerar:

#   CINCO NÚMEROS ALEATÓRIOS
#   Colocar numa tuplas

#   Mostrar a listagem de números
#   Indicar o MENOR Valor
#   Indicar o MAIOR Valor

from random import sample, randrange

gerador = sample(range(20), k=5)

print(f'Lista Gerada: {gerador}')
print(f'Maior Valor: {max(gerador)}')
print(f'Menor Valor: {min(gerador)}')