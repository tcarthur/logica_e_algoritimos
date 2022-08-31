#Indentificação do aluno
print('Nome: Arthur Tavares Carvalho\n'
      'RU: 4158824')

#Início do Código
print('Bem-Vindo ao programa de Feijoada do Arthur Tavares')

#Função que definirá volume (ml) da Feijoada.
def volumeFeijoada():
  while True:
    try:
      print('Menu Volume Feijoada')
      volume = int(input('Entre com a quantidade desejada(ml)'))
      if volume < 300:
        print('Não aceutamos porções menores que 300ml ou maiores que 5L. Tente novamente!')
        continue
      elif volume > 5000:
        print('Não aceutamos porções menores que 300ml ou maiores que 5L. Tente novamente!')
        continue
      elif volume >= 300 or volume <= 5000:
        volume = float(volume) * 0.08
        return volume
    except ValueError:
      print('Insira valor numerico')
      continue
#Funcção que definirá qual o opção da Feijoada    
def opcaoFeijoada():
  while True:
    print('Menu Opção Feijoada')
    opcao = input('Escolha sua opção de Feijoada:\n b - Básica (feijão + paiol + costelinha)  \n p - Premium (Feijão + paiol +costelinha + partes de porco) \n s - Suprema (Feijão + paiol + costelinha + partes do porco charque + calabresa + bacon)\n')
    if opcao == 'b':
      multiplicador = 1.00
      return float(multiplicador)
    elif opcao == 'p':
      multiplicador = 1.25
      return float(multiplicador)
    elif opcao == 's':
      multiplicador = 1.50
      return float(multiplicador)
    else:
      print('Insira uma opção válida')
      continue
#Funcção para definir qual acompanhamento
def acompanhamentoFeijoada():
  valor_acompanhamento = 0
  while True:
    print('Menu Acompanhamento Feijoada')
    acompanhamento = float(input('Deseja alguma acompanhamento? \n 0- Não desejo mais acompanhamentos (encerrar o pedido) \n 1 - 200g de arroz \n 2 - 150g de farofa especial \n 3 - 100g de couve cozida \n 4 - 1 laranja descascada \n Resposta: ' )) 
    
    if acompanhamento == 1:
      valor_acompanhamento += 5.00
      continue
    elif acompanhamento == 2:
      valor_acompanhamento += 6.00
      continue
    elif acompanhamento == 3:
      valor_acompanhamento += 7.00
      continue
    elif acompanhamento == 4:
      valor_acompanhamento += 3.00
      continue
    elif acompanhamento == 0:
      return valor_acompanhamento
    else:
      print('Valor inválido')
      continue

volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()

#Calcular valor total do pedido
total = volume * opcao + acompanhamento
print('O valor a ser pago é R${:.2F} ( volume = {:.2F} * opcção {:.2F} + acompanhamento = {:.2F} )'.format(total,volume,opcao,acompanhamento))