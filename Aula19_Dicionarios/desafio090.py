''''
Faça um programa que leia:

    - nome de uma aluno
    - media de um aluno

Guardando também a situação em um dicionário

No final, mostre o conteúdo da estrutura na tela

Para esse exercício, considerar, média => 7 = Aprovado | média < 7 = Reprovado

'''

infos = dict()

infos['nome'] = str(input( 'Nome: ' ))
infos['media'] = float(input(f'Média de {infos["nome"]}: '))

if infos['media'] >= 7.0:
    infos['situacao'] = 'Aprovado'
else:
    infos['situacao'] = 'Reprovado'

print('\n', '-' * 40, '\n')

print(f'O Nome é: {infos["nome"]}')
print(f'A Média de {infos["nome"]} é: {infos["media"]}')
print(f'A situação de {infos["nome"]} é: \033[1;40m {infos["situacao"]} \033[m')
