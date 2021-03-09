''''
fazer um programa que pergunte:

- nome
- ano de nascimento
- carteira de trabalho, 
    se não tiver digite 0
        se digitar zero break e print() o resultado

    se tiver carteira de trabalho, fazer mais duas perguntas:
        - Ano de contraração
        - Salário

No final mostrar:

- nome
- idade
- Carteira de trabalho
- Ano de contratação 
- salário
- com quantos anos ou quando vai se aposentar

'''

from datetime import datetime

ano_atual = datetime.now().year

dados = dict()

dados['nome'] = str( input('Nome: ') )

nasc = int ( input('Ano de Nascimento: '))
dados['idade'] = ano_atual - nasc

dados['CTPS'] = int( input( 'Carteira de Trabalho [Se não Tiver, Digite 0]: ' ))

if dados['CTPS'] != 0:
    dados['ano de contratacao'] = int ( input('Ano de Contratação: '))
    dados['salario'] = float( input( 'Salário: R$ ' ))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contratacao'] + 35) - datetime.now().year)

if dados['CTPS'] == 0:
    print(f'O Nome tem valor: {dados["nome"]} ')
    print(f'A idade tem valor: {dados["idade"]}')
    print(f'A CPTS tem valor: {dados["CTPS"]}')
else:
    print(f'O Nome tem valor: {dados["nome"]} ')
    print(f'A idade tem valor: {dados["idade"]}')
    print(f'A CPTS tem valor: {dados["CTPS"]}')
    print(f'O Salário tem valor: R$ {dados["salario"]:.2f}')
    print(f'Vai se aposentar com (valor): {dados["aposentadoria"]} anos')

    