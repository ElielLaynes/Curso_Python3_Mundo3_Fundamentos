
# Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tablea do COMPEONATO BRASILEIRO na ordem de colocação

# depois Mostre

#   A) Apenas os 5 PRIMEIROS colocados. - fatiamento
#   B) Os ÚLTIMOS 4 colocados da tabela - Fatinamento (-1) 
#   C) Uma lista em ORDEM ALFABÉTICA - sorted()
#   D) Em que POSIÇÃO na Tabela está o time do SANTOS

equipes = ( 'Flamengo' , 'Internacional' , 'Atlético-MG' , 'São-Paulo' , 'Fluminense' , 'Grêmio' , 'Palmeiras' , 'Santos' , 'Athletico-PR' , 'Corinthians' , 'Bragantino' ,'Ceará SC' , 'Atlético-GO' , 'Sport Recife' , 'Bahia' , 'Fortaleza' , 'Vasco da Gama' , 'Goiás' , 'Coritiba' , 'Botafogo' )

print(f'\nCassificação do Brasileirão 2021: {equipes}\n')
print(f'\nOs 5 primeiros são {equipes[:5]}')
print(f'\nOs 4 últimos são {equipes[-4:]}')
print(f'\nTimes em Ordem Alfabética: {sorted(equipes)} \n')
print(f'\nO Santos está na {equipes.index("Santos") + 1} posição no Brasileirão. \n')

