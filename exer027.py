n = str(input(' digite seu  nome:  ')).strip()
nome = n.split()

print('seu primeiro no,e: {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[len(nome)-1]))


ent = str(input('digite seu nome: ')).strip()

nome1 = ent.split()
print(nome1[0])
print(' seu ultimo nome é: {}'.format(nome1[len(nome1)-1]))

entrada = str(input(' digite um numero: ')).strip()
r = entrada.split()
print(r)