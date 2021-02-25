'''
                    >>>>>>. LISTAS EM PYTHON <<<<<<<<

-> Para declarar a lista, bastas abrir colchetes []. Exemplo var = []

    # Listas ao contrário de tuplas, São mutáveis e podem ser alteradas.

Exemplos:

    -> O camando abaixo, lanche[3] = 'Picole', vai substituir o elemento no índice 3, no caso o Pudim, pelo Picolé na lista.

    lanche = ['Hamburguer' , 'Suco', 'Pizza', 'Pudim' ]
    lanche[3] = 'Picole'


            >>>>>>>>> ADICIONANDO ELEMENTOS NA LISTA <<<<<<<<<<<<


-> Para adicionar elementos na lista 

    > Método .append('Elemento')
        Exemplo:
            lanche.append('Biscoito')

    * O comando .append() sempre adiciona o elemento NO FINAL DA LISTA

-> Método .insert(0, 'Elemento')
    Exemplo:
        lanche.insert(0, 'Biscoito')
    
    * o .insert() insere um elemento em qualquer lugar da lista. basta declara o indice da posição e o elemento a ser inserido, como no exemplo acima.


            >>>>>>>>>>> APAGANDO ELEMENTOS DA LISTA <<<<<<<<<<<

-> Apagando com o comando del

    del lache[3] --> apaga o item de índice 3 da lista

-> Apagadndo o método .pop()

    lanche.pop(3)

* O comando .pop() originalmente Tem a função de apagar o último elemento da lista. Mas pode ser usada para apagar outros elementos passando o parâmetro para ela, como no exemplo acima.

-> Apagando com o método .remove()

    lanche.remove('Pizza')

* No caso do método .remove() em vez do número do índice do elemento, é passado o nome do próprio elemento para fazer a exclusão


-> Removendo um item com condicional if

    # Se existir 'Pizza' na lista lanche:
    #           remova a 'Pizza' da lista lanche 

    -> Em Python

    if 'Pizza' in lanche:
        lanche.remove('Pizza')


        >>>>>>>>>>>>>>>>> CRIANDO LISTAS <<<<<<<<<<<<<<<<<<,

-> Criando listas através de ranges
Exemplo:

valores = list(range(4, 11))

-> Ordenando lista com função .sort()

        valores.sort() # ordena a lista do Menor para o Maior valor.

    -> Ordem - Maior para Menor
        Com a função .sort() chamando o parâmetro reverse=True os números são colocados na ordem inversa

        valores.sort(reverse=True) 

--> lendo o tamanho da lista com a função len()

    len(valores)  # nesse caso 5 elementos

'''

#                           Exemplos Práticos


num = [2, 5, 9, 1, 8, 3]          # Lista
num[2] = 3                  # lista na posição substituiu o 9 pelo 3
num.append(7)               # adicionando o número 7 na lista
num.sort()                  # organizando a lista do Menor para o Maior    
num.sort(reverse=True)      # organizando a lista do Maior para o Menor
num.insert(2, 2)            # Insere o número 0 na posição de índice 2
num.pop()                   # Elimina o último item da lista
num.pop(1)                  # Elimina o item no índice 1
num.remove(2)               # Se tiver 2 item iguais na lista, o remove elimina o primeiro apenas

if 4 in num:                # Utilizando o if in para eliminar o um elemento apenas
    num.remove(4)           # Se ele for encontra na lista
else:
    print('Não Achei o Número 4')

print(num)
print(f'Essa lista tem {len(num)} elementos.')  # Imprimindo a quantidade de elementos da lista com o função len()


# Exemplo 2

# declarando a lista vazia
valores = []

# adicionando valores a lista
valores.append(5)
valores.append(9)
valores.append(4)


# Para cada valor na lista valores, imprima o valor
for v in valores:
    print(v)

print()


# Para cada chave e valor em enumerate(valores) print a chave e o valor.  Nesse caso, a chave é correspondete ao índice no python e retorno o número do índice.

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

print('Cheguei ao final da lista')


 # >>>>>>>>>>>>>>>>>>>>> LENDO VALORES PELO TECLADO E ARMAZENANDO NA LISTA <<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Declarando uma lista vazia
valores = list()


# Repitindo o input de valor 5 vezes
for cont in range(0, 5):
    valores.append( int ( input ( 'Digite um valor: ') ) ) 

# Printando chaves e valores da lista
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')


# >>>>>>>>>>>>>>>>.. Ligação e copia de lista

# Quando se declara uma lista igual a outra, as listas criam uma ligação, que faz com que aplicada uma alteração a uma lista ela é replicada a outra lista também. Essa é a ligação entre lista.

# Exemplo:

a = [2, 3, 4, 7]
b = a                       # declarando a lista a na lista b
b[2] = 8                    # substituindo o valor 4 pelo valor 8 no segundo índice da lista b (impaca na lista a)
print(f'Lista A: {a}')
print(f'Lista B:{b}')


# >>>>>>>>>>>>>> COPIANDA UMA LISTA DA OUTRA

a = [2, 3, 4, 7]
b = a[:]                    # lista b recebe TODOS os itens de a. -> a[:]
b[2] = 8                    
print(f'Lista A: {a}')
print(f'Lista B:{b}')