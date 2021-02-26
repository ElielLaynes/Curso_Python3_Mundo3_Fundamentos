
# Crie um programa que:

    #   Vai ler vários números
    #  colocar em uma lista
    # perguntar se o usuário quer continuar

# Depois mostre:

    #   A) Quantos números foram digitados
    #   B) A lista de valores:
    #       - Ordenada
    #       - De forma Decrescente
    #   C) Se o valor 5 foi digitado
    #       - Se está na lista
    #       - se não está na lista


valores = list()

while True:
    numeros = int ( input ( 'Digite um valor: ' ) )
    valores.append(numeros)

    resposta = str ( input ( 'Quer Continuar? [S/N]: ' ) ).upper()
    if resposta == 'N':
        break
    
# ----------------------------------------------

print(f'\nVocê Inseriu {len(valores)} Valores à Lista.\n')

valores.sort(reverse=True)
print(f'Os valores em Ordem Descecente são: {valores} \n')

if 5 in valores:
    print('\nO valor 5 FAZ PARTE da Lista\n')
else:
    print('O valor 5 NÃO FAZ Parte Lista.\n')


