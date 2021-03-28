from random import  randint
computador = randint(0 , 10)#faz o computador gerar um numero aleatóri de 0 a 5#

print(' voou pensar em um numero...')

jogador1 = input( 'pense em um numero e digite: ')
if jogador1 == computador:
    print(' parabens vc ganhou')
else:
    print(' ganhei vc errou!!!')



