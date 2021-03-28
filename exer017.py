from math import hypot
cat1 = float(input(' digite o cateto oposto: '))
cat2 = float(input(' digite o cateto adjacente: '))
h = hypot(cat1, cat2)
print('a hipotenusa do triangulo é: {:.2f}'.format(h))
