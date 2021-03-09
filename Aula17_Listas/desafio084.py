
# Faça um programa que:

#   leia nome e peso de várias pessoas
#   guarde tudo em uma lista
#   Pergunte se quer continuar [s/n]

# Depois mostre:

#       A) QUANTAS pessoas foram cadastradas;
#       B) Uma listagem com as pessoas mais pesadas;
#       C) Uma listagem com as pessoas mais leves.


lista_temporaria = []
dados_principal = []

maior_peso = menor_peso = 0

while True:
    lista_temporaria.append( str ( input ( 'Qual seu Nome?  ') ) )
    lista_temporaria.append( float ( input ('Qual seu Peso? ') ))

    if len(dados_principal) == 0:
        maior_peso = menor_peso = lista_temporaria[1]
    else:
        if lista_temporaria[1] > maior_peso:
            maior_peso = lista_temporaria[1]
        if lista_temporaria[1] < menor_peso:
            menor_peso = lista_temporaria[1]

    dados_principal.append(lista_temporaria[:])
    lista_temporaria.clear()
    
    resp = str ( input ( 'Quer Continuar? [S/N]' ) )
    if resp in 'Nn':
        break
  
print('_' * 40)
print(f'Total de Cadastro foi: {len(dados_principal)} pessoas.')

print(f'O Maior Peso foi: {maior_peso}Kg. Peso de: ', end='')
for pessoa in dados_principal:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]} ', end='')
print()


print(f'O Menor Peso foi: {menor_peso}Kg. Peso de: ', end='')
for peso in dados_principal:
    if peso[1] == menor_peso:
        print(f'{peso[0]} ', end='')
print()        


