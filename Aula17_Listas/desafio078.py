
# Faça um programa que 

    # Leia 5 valores pelo teclado
    # Guarde-os em uma lista

    # Mostre qual foi o MAIOR número
    # Mostre qual foi o MENOR número
    # Pisçoes na lista

valores = []
maior = menor = 0

for cont in range(0, 5):
    valores.append( int ( input ( f'Digite um Valor Para a Posição {cont}: ' ) ) )
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print(f'Valores Digitados: {valores}')

print(f'O maior valor foi {maior} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c} -- ', end='')

print(f'\nO menor valor digitado foi {menor} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c} -- \n', end='')