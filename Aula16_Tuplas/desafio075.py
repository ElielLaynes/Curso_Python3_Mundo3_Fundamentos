
# Desenvolva um programa que :

#   leia QUADRO VALORES pelo teclado
#   garde-os em uma TUPLA

# Depois, mostre:

#       A) Quantas vezes apareceu o valor 9
#       B) Em que posição foi digitado o primeiro valor 3
#       C) Quais foram os números PARES?

valores = ( int ( input('Digite um Número: ')),
            int ( input('Digite um Número: ')),
            int ( input('Digite um Número: ')),
            int ( input('Digite um Número: ')))

print(valores)
print(valores.count(9))
if 3 in valores:
    print(f'{valores.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')
print()
for v in valores:
    if v % 2 == 0:
        print(f'Os valores pares foram: {v}')