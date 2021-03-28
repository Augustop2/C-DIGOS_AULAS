v = float(input(' digite a velocidade:  '))
print( ' a velocidade foi de: {:.0f} km/h'.format(v))
if v < 80:
    print(' ')
else:
    print('você foi multado')
multa = (v - 80)* 7
print(' o valor da multa é de: R$ {:.2f}'.format(multa))




