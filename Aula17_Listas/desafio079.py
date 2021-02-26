
# Crie um programa onde:

    # O usuário possa digitar vários valores núméricos
    # Cadastre os valores em uma lista

    # Se o número já existir
        #   NÃO adicionar na lista

# Exibir saídas com:

    # Todos os VALORES ÚNICOS digitados.
    # Em ordem crescente.

valores = list()


while True:
    numeros = ( int ( input ( 'Adicione um Valor a Lista: ' )))

    if numeros not in valores:
        valores.append(numeros)
        print('Valor Adicionado com Sucesso! =D')
    else:
        print('Valor Duplicado!')

    resposta = str ( input ( 'Quer Continuar? [S/N]: ' )  ).upper()
    if resposta == 'N':
        break

valores.sort()
print(f'Você Adiciou os Valores: {valores}')