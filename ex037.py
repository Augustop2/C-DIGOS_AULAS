valor_casa =float(input(' qual o valor do imóvel?:   '))
if valor_casa == '':
    valor_casa = float(input( ' qual o valor do imóvel?:'))
salario = float(input(' qual a sua renda ?: '))
while salario == '':
    salario = float(input(' qual sua renda?: '))
tempo = (input(' em quantos anos vc pretende parcelar?:  '))
while tempo == '':
    tempo = input('em quantos anos vc pretende parcelar?: ')
parcela = valor_casa / (tempo * 12)
print(' o valor da parcela é de R${:.2f}'.format(parcela))
if parcela > (salario /100 *30):
    print('sinto muito mas seu meprestimo não foi aprovado.')
elif parcela < (salario / 100 * 30):
    print(' parabéns seu emprestimo fooi aprovado !!!!!')


