#Indentificação do aluno
print('Nome: Arthur Tavares Carvalho'
      'RU: 4158824')

#Início do Código
print ('Bem Vindo a Loja do Arthur Tavares')

#Variável referente ao valor original
valororiginal = float( input('Informe o valor do produto: R$ '))

#Variável referente a quantidade
quantidade = int(input('Informe a quantidade desejada: '))

#Estrutura if/elif/else para verificar entrada do usuário
if 0 <= quantidade < 4:
  desconto = 0
elif 5 <= quantidade < 19: 
  desconto = 0.03
elif 20 <= quantidade < 99:
  desconto = 0.06
else:
  desconto = 0.10

#Cálculo do valor sem o desconto
semDesconto = valororiginal * quantidade

#Cálculo do desconto
comDesconto = semDesconto - (semDesconto * desconto)


#saída
print('O valor sem desconto foi R${:.2F}'.format(semDesconto))
print('O valor com desconto foi R${:.2F}'.format(comDesconto) + ('(desconto {:.2F}%)').format(desconto*100))

