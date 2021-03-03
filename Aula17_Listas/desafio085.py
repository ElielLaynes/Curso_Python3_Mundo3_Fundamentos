
# Crie um programa onde o úsuário possa digitar:

#   Sete valores numérios
#   Cadastrar em uma única lista e separar os valores de pares e ímpares

#   No final:

#   Mostre os valores pares e ímpares em ordem CRESCENTE


lista_parimpar = [ [], [] ]

cont = 0
while cont < 7:
    cont += 1
    numero = int ( input ( 'Digite um Número: ' ))

    if numero % 2 == 0:
        lista_parimpar[0].append(numero)
    else:
        lista_parimpar[1].append(numero)

lista_parimpar[0].sort()
lista_parimpar[1].sort()

print(f' Os valores Pares foram: {lista_parimpar[0]}')
print(f' Os valores ïmpares foram: {lista_parimpar[1]}')


#print(f'Os Números Pares foram: {lista_parimpar[0]}')
#print(f'Os Números ïmpares foram: {lista_parimpar[1]}')