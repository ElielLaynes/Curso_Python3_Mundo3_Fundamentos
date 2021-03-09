
# Crie um programa onde o usuários possa:

#   Digitar 5 valores numéricos

#   Cadastrar os valores em uma lista
        #   Já na posição correta de inserção (sem usar a função .sort() )

#   Mostre a lista ordenada na tela


lista_num = []

for cont in range(0, 5):
    num = int ( input( 'Digite um Valor: ' ) )

    if cont == 0 or num > lista_num[-1]:
        lista_num.append(num)
        print('Adicionado ao Final da Lista!')
    else:
        pos = 0
        while pos < len(lista_num):
            if num <= lista_num[pos]:
                lista_num.insert(pos, num)
                print(f'Adicionado na Posição {pos} da Lista.')
                break
            pos += 1

print('-' * 30)
print(f'Os valores digitados foram: {lista_num} ')