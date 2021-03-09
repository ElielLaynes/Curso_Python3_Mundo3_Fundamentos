
# Criar uma matriz 3x3

#   Obter:

# A soma dos valores pares
# A soma dos valores da terceira coluna
# O Maior valor da segunda coluna

matriz = [ [0,0,0], [0,0,0], [0,0,0] ]

soma_par = 0
soma_colum3 = 0
maiorValor_colum2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int ( input ( f'Digite um valor para [{linha}, {coluna}]: ' ) )

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print('-' * 40)
print(f'A Soma dos valores Pares é: {soma_par}')

for linha in range(0, 3):
    soma_colum3 += matriz[linha][2]
print(f'A Soma da Terceira Coluna é: {soma_colum3}')

for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maiorValor_colum2:
        maiorValor_colum2 = matriz[1][coluna]
print(f'O Maior valor da Segunda Coluna é: {maiorValor_colum2}')