
# Crie uma programa que tenha um tupla totalmente preenchida com uma contagem por extenso de ZERO até VINTE

# O programa deverá:

    # Ler um número pelo teclado (entre 0 e 20)
    # Motrá-lo por EXTENSO


num_extenso = ('ZERO' , 'UM' , 'DOIS' , 'TRÊS' , 'QUATRO' , 'CINCO' , 'SEIS' , 'SETE' , 'OITO' , 'NOVE' , 'DEZ' ,'ONZE' , 'DOZE' , 'TREZE' , 'QUATORZE' , 'QUINZE' , 'DEZESSEIS' , 'DEZESETE' , 'DEZOITO' , 'DEZENOVE' , 'VINTE')


while True:
    num_usario = int ( input ( 'Digite um Número entre 0 e 20: ' ) )
    if num_usario < 0 or num_usario > 20:
        num_usario = int ( input ('Tente Novamente. Digite um número entre 0 e 20: '))
   
    for indice in range(0, len(num_extenso)):
           if num_usario == indice:
               print(num_extenso[indice])