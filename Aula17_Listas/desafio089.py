'''
Crie um programa:

    Leia o nome de um aluno
    leia duas notas do aluno

    guarde em uma lista composta

    no final mostre:
        Um boletim contendo:

            A média de cada um

            permita que o usuário possa mostrar as notas de cada aluno individualmente

'''

alunos = list()


while True:
    nome = str ( input ( 'Qual seu Nome: ' ) )
    nota1 = float ( input ( 'Nota 1: ' ) )
    nota2 = float ( input ( 'Nota 2: ' ) )
    media = (nota1 + nota1) / 2

    alunos.append( [ nome, [ nota1, nota2 ], media] )

    resp = str ( input ( 'Quer Continuar? [S/N] ' ) )
    if resp in 'Nn':
        break

print('-=' * 30)
print(f'{"No.":<4} {"NOME":<10} {"Média":>8}')
print('-' * 26)

for indice, aluno in enumerate(alunos):
    print(f'{indice:<4} {aluno[0]:<10} {aluno[2]:>8.1f} \n')

print(alunos)

while True:
    print('_' * 35)
    opcao = int ( input ( 'Mostrar Notas de Qual Aluno? [999 Para Sair]: ' ) )
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(alunos) - 1:
        print(f'Notas de {alunos[opcao][0]} são {alunos[opcao][1]}')
        