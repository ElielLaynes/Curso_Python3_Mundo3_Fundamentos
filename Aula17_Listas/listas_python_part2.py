'''
        >>>>>>>>>>>>>>>>>>>> LISTA COMPOSTAS <<<<<<<<<<<<<<<<<<<<<

Lista compostas, ou listas dentro de lista, é uma estrutra de lista que aninha uma dentro da outra.

Exemplo:

    pessoas = [ [ 'Eliel', 25 ] , [ 'Mariana', 28 ] , [ 'Ana', 21 ] ]

Acima temos a lista pessoa e dentro dela temos outras 3 lista com nome e idade de pessoas.

    se executessemos uma saída como:

        print(pessoas[0][0])

    A saída seria igual a = 'Eliel'

        Visto que a solicitação foi que retornace o valor do índice 0 da lista pessoas e o índice 0 da lista aninhada na posição zero também.

        da mesmo forma que pessoas[2][1] retona 21, idade do item no índice 2 da lista pessoas e no ítem de 1 dentro da lista de lista de pessoas.

    Da mesma forma que o comando print(pessoa[1]) retorna tudo do item 1 de pessoas, nesse caso = ['Mariana', 28]
'''

# Exemplos Práticos


# Ligação entre listas
teste = list()
teste.append('Eliel')
teste.append(26)

teste1 = list()
teste1.append(teste) # passando a lista 1 para a lista 2 dessa maneira, cria-se uma ligação

teste[0] = 'Ana'
teste[1] = 28

teste1.append(teste)
print(teste1)


# Criando uma CÓPIA da lista

teste = list()
teste.append('Eliel')
teste.append(26)

teste1 = list()
teste1.append(teste[:]) # passando a assim:lista1[:] cria-se uma cópia de lista

teste[0] = 'Ana'
teste[1] = 28

teste1.append(teste[:])
print(teste1)

# Consultando elementos de listas aninhadas

galera = [ [ 'Eliel', 26 ], [ 'Mariana', 27 ], [ 'João', 19 ], [ 'Débora', 22 ] ]

print(f'Toda a Lista: {galera}')
print(f'item de índice 1 e 1: {galera[1][1]}')
print(f'item de índice 0 e 0: {galera[0][0]}')
print(f'item de índice 2 e 1: {galera[2][1]}')
print(f'item de índice 3 e 1: {galera[3][1]}')
print(f'item de índice 1 e 0: {galera[1][0]}')
print(f'item de índice 2 e 0: {galera[2][0]}')
print(f'item de índice 3 e 0: {galera[3][0]}')
print('-' * 40)

# Imprimindo em forma de lista com loop for

# imprimento lista
for pessoa in galera:
    print(pessoa)

print('-' * 30)

# Se quiser APENAS os NOMES:
for pessoa in galera:
    print(pessoa[0])

print('-' * 30)

# Da mesma forma se quiser APENAS IDADES:
for pessoa in galera:
    print(pessoa[1])

print('-' * 30)

# PRINT FORMATADO
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de Idade.')


# Capiturando o dado e colocando em uma lista temporária

pessoas = list()    # Lista Final
dados = list()      # Lista temporária

for cont in range(0, 3):
    dados.append( str ( input ( 'Nome: ' ) ) )
    dados.append( int ( input ( 'Idade: ' ) ) )

    pessoas.append(dados[:])     # Fazendo a cópia da lista dados[:] para lista pessoas
    dados.clear()               # Limpando a lista temporária dados

print(pessoas)

# Usando loop for e if para montar uma condição de análise de idade
maior = menor = 0

for pessoa in pessoas:
    if pessoa[1] >= 21: # Se elemento no índice 1 da lista = idade for mairo que 21
        print(f'{pessoa[0]} é Maior de Idade.')  #pessoa[0] = nome da pessoa
        maior += 1
    else:
        print(f'{pessoa[0]} é Menor de Idade.')
        menor += 1

print(f'Na Lista há: {maior} Maior(es) e {menor} Menor(es) de Idade.')