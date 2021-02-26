
# Crie um programa que:

#   O usuário digite uma expressão qualquer que use parenteses

# O aplicativo deverá analisa se:
# 
#   A expressão passada está com os parênteses abertos e fechado na ordem correta

expressao = str ( input ( 'Digite a expressão: ' ))

paren = []

for simbolo in expressao:
    if simbolo == '(':
        paren.append('(')

    elif simbolo == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break

if len(paren) == 0:
    print('Sua Expressão é Válida!')
else:
    print('Sua Expressão está Errada!')


