
# Crie um programa que 

#    Tenha uma tupla com várias palavras(sem acentos)
#   Mostrar para cada palavra na tupla, quais são suas vogais

palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar','trabalhar','mercado','programador','futuro')

for p in palavras:
    print(f'\n Na palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}' , end='  ')
