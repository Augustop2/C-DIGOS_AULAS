num = int(input('digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('analisando o valor {}'.format(num))
print(' a unidade é: {}'.format(u))
print('a dezena é: {}'.format(d))
print('a centena é: {}'.format(c))
print('a milhar é: {}'.format(m))
