
# Crie um programa que

# tenha uma tupla única com nomes de produtos e seus respectivos preços

# No final mostre uma listagem de preços organizados em forma tabular

listagem = ('Shampoo', 23.40,
            'Desodorante', 15.78,
            'Sabonete', 4.25,
            'Condicionardor', 22.90,
            'Máscara de Hidratação', 38.75,
            'Finalizador', 18.50,
            'Óleo de reconstrução', 29.30,
            'Pente', 20,
            'Secador', 367.90,
            'Serum Capilar', 124.90,
            'Hidratante Corporal', 54.29)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}:' , end='')
    else:
        print(f'R${listagem[item]:>7.2f}')
print('-' * 40)