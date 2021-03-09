
# Crie um programa que:

# Crie uma matriz de dimensão 3x3

# Preencha a matriz com valores lídos pelo teclado

# No final, mostre a matriz na tela, com a formatação correta

matriz = [ [ 0, 0, 0 ] , [ 0, 0, 0 ] , [ 0, 0, 0 ] ]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz [linha] [coluna] = int ( input ( f' Digite um valor para [{linha}, {coluna}]: ' ) )

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()