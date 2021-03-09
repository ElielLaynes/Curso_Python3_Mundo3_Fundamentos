
# Crie um programa que vai:

#       Ler vários números
#       E perguntar se o usuário quer continuar a cada repetição

#       Crie 3 listas:

#       1 - Receber todos os valores;
#       2 - Receber apenas valores pares;
#       3 - Receber apenas valores ímpares;

#   No final mostre o restultado das 3 listas na tela


total_num = []
par = []
impar = []

while True:
    num = int ( input ( 'Digite um Número: ' ) )
    total_num.append(num)

    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

    resposta = str ( input ( 'Quer Continuar? [S/N]: ' ) )
    if resposta in 'Nn':
        break

print('-' * 30)

print(f'Lista Completa: {total_num}')
print(f'Lista de Pares: {par}')
print(f'Lista de Ímpares: {impar}')