'''
            VARIÁVEIS COMPOSTAS

-> TUPLAS

    >>>> AS TUPLAS SÃO IMUTÁVEIS, OU SEJA, NÃO PODEM TER SEUS ELEMENTOS ALTERADOS OU SUBSTITUÍDOS <<<<

    Tupla é uma variável composta que pode receber vários valores ao mesmo tempo.

        variável = ('item 1' , 'item 2' , ... , 'item N')

        * Do python 3.5 em diante, não é necessário colocar parenteses para iniciar uma tupla 8

    
-> As tuplas suportam fatiamento, bem como fatiamos as string, utilizando os índices do python

Exemplo: Considerando a tupla abaixo

    lanche = ('Hamburgues', 'suco', 'pizza', 'pudim')

para imprimir apenas o lance na posição de índice 2

    print(lanche[2])

        - Esse print retornaria o item da tupla no índice 2 dela, como o índice em python começa em zero, nesse caso o item retornado na posição de indice 2 da lista seria a PIZZA,

    print(lanche[ 0:2 ])
    print(lanche[ 1: ])
    print(lanche[ -1 ])


Lendo o Comprimento da tupla usando len()

len(lanhe) # comprimento da tupla, e retorna QUANTOS elementos a tupla tem, nesse caso 4


-> Tupla com o Loop For

para cara comida em lanche, imprima a comida:

    for comida in lanche:
        print(comida)

        então ele vai correr a tupla e retonar da uma das comidas armazenadas na lista

'''


# Exemplos Práticos


lanche = ('Hamburguer' , 'Suco' , 'Pizza' , 'Pudim')

print(f'\n Toda a Tupla de elementos: {lanche} \n')           # Imprime a tupla toda

print(lanche[1])        # Apenas o elemento de índice 1 = Suco
print(lanche[-2])       # O penultimo elemento da tupla = Pizza
print(lanche[1:3])      # entre o indíce 1 e 3 = Suco e Pizza
print(lanche[2:])       # Do índice 2 até o final = Pizza e Pudim
print(lanche[:2])       # Do início até o índice de número 2 = Hambuguer e Suco
print(lanche[-2:])      # Do íncide -2 até o final = Pizza e Pudim

print()
# Usando o loop For para iterações na tupla
print('Usando o loop For para iterações na tupla')
#opcão 1 - lendo os elementos e imprimindo na tela
print('\n opcão 1 - lendo os elementos e imprimindo na tela \n')
for comida in lanche:
    print(f' Eu vou comer {comida}')

print()

#opção 2 - lendo a tupla, contando os elementos e printando os índices das posiçoes
print('\n opção 2 - lendo a tupla, contando os elementos e printando os índices das posiçoes \n')
for comida in range(0, len(lanche)):
    print(comida)

print()

#opção 3 - lendo os elementos na posição do contador para imprimir os elementos da lista em vez dos índices
print('\nopção 3 - lendo os elementos na posição do contador para imprimir os elementos da lista em vez dos índices\n')
for comida in range(0, len(lanche)):
    print(lanche[comida])

print()

#opcao 4 - Imprimindo a os resulados da tupla com o item e sua posição de índice
print('\nopcao 4 - Imprimindo a os resulados da tupla com o item e sua posição de índice\n')
for comida in range(0, len(lanche)):
    print(f' Vou comer {lanche[comida]} na POSIÇÃO {comida}')

print()


# Opção 5 - Usando a função enumerate() - que também fornece o elemento e a posição do mesmo
print('\nOpção 5 - Usando a função enumerate() - que também fornece o dado e a posição\n')

for posicao , comida in enumerate(lanche):
    print(f'Na POSIÇÃO {posicao}, Temos a Comida: {comida}')



# UTILIZANDO O MÉTODO sorted() para ORGANIZAR uma tupla
# Ordena em ordem alfaberica e crescente

lanche = ('Hamburguer' , 'Suco' , 'Pizza' , 'Pudim')

print(sorted(lanche))


# JUNTANDO DUAS TUPLAS

# funciona como se fosse concatenar as duas tuplas.
# Importante: a + b NÃO É a mesma coisa que b + a. Fomam tuplas diferentes
a = (2, 4, 6)
b = (1, 5, 8, 4)
c = a + b
print(c)

# Contando quantas vezes um elementos aparece em uma tupla que foi concatenada
# Utilizando o método count() para contar quantas vezes um elemento aparece dentro da tupla
print(c.count(4))

# Utlizando o a função index() para encontrar o índice de posição do elemento dentro da tupla
# Aqui ele aponta apenas a primeira ocorrencia. Ou seja, se tiver mais de um na tupla ele vai mostar apenas onde começar o primeiro elemento e chamar e mostar a índice dele
print(c.index(5))

# Para encontar o índice de mais um elemento que esteja repitido na tupla:
# Nesse exemplo, a tupla c tem 2 valores igual a 4, um no índece 1 e outro no índice 6.
# Como eu sei que o primeiro 4 está no índice 1 e peço pra ele producurar do segundo elemento em diante
# nesse caso abaixo: Procute o elemento 4 na tupla, do índice 2 em diante, visto que o primeiro já foi achado no índece 1. E aí ele vai retornar o índice 6, onde está novamente o elemento 4 dentro da tupla

print(c.index(4 , 2))

# As tuplas, diferentes dos vetores que só aceitam dados de um tipo, elas aceitam dados de vários tipos dentro delas

pessoa = ('Eliel' , 26 , 'M' , 78.4)
print(pessoa)

# Para apagar qualquer variável e não somente uma tupla, podemos usar a função del()
pessoa = ('Eliel' , 26 , 'M' , 78.4)
del(pessoa)
