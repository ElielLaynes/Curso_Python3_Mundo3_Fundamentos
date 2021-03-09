'''
         ESTRUTURA DE DADOS - DICIONÁRIOS

Dicionários são estruturas de dados onde podemos armazenar informações com índices líterais, ou seja, podemos personalizar o índice da estrutura de dados, em vez de, 0, 1, 2, 3, colocar um nome como, idade, peso, pessoa, cabelo, enfim, podemos dar qualquer nome para o índice.

Os dicinários são indicados pela abertura e fechamento de chaves {} ou dict{}

Exemplo:

Uma estutura de dados dicionário, composta pela informação nome e idade, ficaria parecida com isso:

dados = {'nome': 'Eliel' , 'idade': 26 }

Para mostrar na tela o índice nome ou idade, é só apontar o índice da estrutra no print(). Veja:

print(dados[nome]) --> Mostraria na tela o nome = Eliel
print(dados[idade]) -- Mostraria na tela a idade = 26


        >>>>>>>> INSERINDO UM NOVO ÍNDICE DE DADOS NO DICIONÁRIO <<<<<<<<<<

Para inserido um novo índice de dados no dicionário é fácil:

dados['sexo'] = 'M'

E o dicionários de dados ficaria assim:

dados = {'nome': 'Eliel', 'idade': 26, 'sexo': 'M'}


>>>>>>> APAGANDO DADOS DE UM DICIONÁRIO >><<<<<<<<<

Para apagar é só usar o do comando del, dessa forma:

del dados['idade'] ---> Vai apagar a informação de idade do dicionário.


---------------------------

Os dicionários são didividos em chaves, valores e items, vejamos o exemplos abaixo:


dados = {'nome': 'Eliel', 'idade': 26, 'sexo': 'M'}

print(dados.values()) ---> Retorna apenas os valores, nesse caso = 'Eliel', 26, 'M'
print(dados.keys())   ---> Retorna apenas as chaves, nesse caso = 'nome', 'idades', 'sexo'
print(dados.items())  ---> Retorna cada chave com seu respectivo valor, 
                            nesse caso = 'nome': 'Eliel', 'idade': 26, 'sexo': 'M'



>>>>>>>>>>>>>>>. UTILIZANDO LOOP FOR PARA PERCORRER UM DICIONÁRIO <<<<<<<<<<<<<<

Podemos utilizad o o loop for para percorres e imprimir os chaves, valores ou items de um dicionários, exemplo:

    for keys, values in dados.items():
        print(keys, values)

O retorno vai ser:
nome Eliel
idade 26
sexo M


---------------------------------------------

Assim como tudo em python, os dicionários também podem ser aninhados ou adicionanos dentro de outras estruturas como listas e tuplas, exemplo:

abaixo vemos uma lista com 3 indícies e esses índices da lista tem como conteúdos dicionários de informações

pessoas = [{'nome': 'Eliel', 'idade': 26, 'sexo': 'M'},
           {'nome': 'Ana', 'idade': 29, 'sexo': 'F'},
           {'nome': 'Mari', 'idade': 27, 'sexo': 'f'}]

para mostrar informações específicas na tela é só usar o índice da lista e as chaves dos dicionários, exemplo:

print(pessoas[0]['nome'])  --> Retorno igual = Eliel
print(pessoas[2]['sexo'])  --> Retorno igual = F
print(pessoas[1]['idade']) --> Retorno igual = 29
'''

#       Exemplos Práticos
'''
pessoas = {'nome': 'Eliel', 'idade': 26, 'sexo': 'M'}

print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
# print formatado
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # Importante se atentar as aspas duplas. Como está dentro de aspas simples, precisa de aspas duplas para funcionar na hora de referenciar o índice do dicionário


#       MOSTRANDO AS KEYS, VALUES E ITEMS

print(pessoas.keys())       #--> Retorna as chaves
print(pessoas.values())     #--> Retorna os valores
print(pessoas.items())      #--> Retorna as chaves e valores

print('\n', '-' * 50, '\n')


# UTILIZANDO LOOP FOR PARA PERCORRES O DICIONARIOS E PRINTAR OS DADOS

for key in pessoas.keys():
    print(f'chave = {key}')

print()
for value in pessoas.values():
    print(f'valor = {value}')


print()
for key, value in pessoas.items():
    print(f'Chave e Valor: {key} = {value} ')
print()

# ----------------------------------------------------------------

del pessoas['sexo'] # Exclui o índice sexo do dicionário

pessoas['nome'] = 'Mariana'     # Altera o índice nome de Eliel para Mariana

print()
for key, value in pessoas.items():
    print(f'Chave e Valor: {key} = {value} ')
print()

# ---------------------------------------------------------------
#      >>>>>>>> ADICONANDO ITEM NO DICIONÁRIO   <<<<<<<<<<<<

# É muito fácil também.

pessoas['peso'] = 78.6      # Adiciona o item peso no final do dicionário.

print()
for key, value in pessoas.items():
    print(f'Chave e Valor: {key} = {value} ')
print()


# Criando uma LISTA  com DICIONÁRIOS DENTRO
print()
brasil = list() 

estado_1 = {'uf': 'Paraná', 'sigla': 'PR'}
estado_2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado_1)
brasil.append(estado_2)

print('\n','Lista com os dicionários dentro: ', brasil)
print('\n', 'Dicionário com apenas 1 estado: ', estado_1)
print('\n', 'Dicionário com apenas 1 estado: ', estado_2)

print('\n', 'lista pos Zero(0), dicionário índice uf = ' , brasil[0]['uf'])
print('\n', 'lista pos um(1), dicionário índice sigla = ', brasil[1]['sigla'])

print()

.'''

#   >>>>>>>. ADICONADO ELEMENTOS A UM DICIONÁRIO E COLOCANDO DENTRO DE UMA LISTA

estados = dict()
brasil = list()

for contador in range(0, 3):
    estados['uf'] = str( input( 'Qual seu Estado? [ex.: São Paulo]:' ) )
    estados['sigla'] = str( input( 'Sigla do Estado [ex.: SP]: ' ))

    brasil.append(estados.copy())   # O método copy(), funciona para o dicionario, assim como a cópia de lista 
                                    # com fatiamento funciona nas listas. lista[:] = cópia de lista
                                    # Desse modo é criado uma cópia dos dicionários na lista e não uma ligação
                                    # Entre elas
print(brasil)

# Usando for para manipular a lista e os dicionários dentro da lista.
for estado in brasil:
    print(estado)

print()
for estado in brasil:   # for da lista

    for chave, valor in estado.items(): # for do dicionário
        print(f'{chave} = {valor}')


    for chave in estado.keys():
        print(f'chave: {chave}')


    for valor in estado.values():
        print(f'{valor}', end=' | ')

print()

