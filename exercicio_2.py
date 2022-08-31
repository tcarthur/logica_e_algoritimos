#Indentificação do aluno
print('Nome: Arthur Tavares Carvalho'
      'RU: 4158824')


#Cardápio
print('--------------------   Cardápio  -----------------------')

print('| Código | | Descrição | | Pizza Média | | Pizza Grande |')

print('|   21   | |Napolitana | |   R$20,00   | |    R$26,00   |')

print('|   22   | |Margherita | |   R$20,00   | |    R$26,00   |')

print('|   23   | |Calabresa  | |   R$25,00   | |    R$32,50   |')

print('|   24   | |Toscana    | |   R$30,00   | |    R$39,00   |')

print('|   25   | |Portuguesa | |   R$30,00   | |    R$39,00   |')

print('----------------------------------------------------------')


#Cardápio M
tamanho_M = {
  '21':['Napolitana',20.00],
  '22':['Margherita',20.00],
  '23':['Calabresa',25.00],
  '24':['Toscana',30.00],
  '25':['Portuguesa',30.00],
}


#Cardápio G
tamanho_G = {
  '21':['Napolitana',26.00],
  '22':['Margherita',26.00],
  '23':['Calabresa',32.50],
  '24':['Toscana',39.00],
  '25':['Portuguesa',39.00],
}


#Váriavel do valor
valor = 0 

#Escolha o tamanho
while True:
  tamanho = input('Qual tamanho da Pizza ( M/G)? ').upper()

  if tamanho == ('M'):
    codigo = int(input('Qual o código da pizza que deseja? '))
    if codigo == 21:
      valor += tamanho_M['21'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_M['21'][0]))
    elif codigo == 22:
      valor += tamanho_M['22'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_M['22'][0]))
    elif codigo == 23:
      valor += tamanho_M['23'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_M['23'][0]))
    elif codigo == 24:
      valor += tamanho_M['24'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_M['24'][0]))
    elif codigo == 25:
      valor += tamanho_M['25'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_M['25'][0]))
    else:
      print('Código de pizza inválida, escolha novamente')
      continue

    #Novo Pedido M
    print('Deseja pedir mais alguma coisa?')
    novo_pedido_M = int(input('1 - Sim | 0 - Não: '))
    if novo_pedido_M == (1):
      continue
    elif novo_pedido_M ==(0):
      print('O valor total do seu pedido foi de {:.2f}R$ ,muito obrigado utilizar nossos serviços,tenha um ótimo dia!'.format(valor))
      break
    else:
      print('Resposta inválida')
      continue

    #Tamanho G
  elif tamanho == ('G'):
    codigo = int(input('Qual o código da pizza que deseja? '))
    if codigo == 21:
      valor += tamanho_G['21'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_G['21'][0]))
    elif codigo == 22:
      valor += tamanho_G['22'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_G['22'][0]))
    elif codigo == 23:
      valor += tamanho_G['23'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_G['23'][0]))
    elif codigo == 24:
      valor += tamanho_G['24'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_G['24'][0]))
    elif codigo == 25:
      valor += tamanho_G['25'][1]
      print('Você pediu uma pizza de {}'.format(tamanho_G['25'][0]))
    else:
      print('Código de pizza inválido, escolha novamente')
      continue
    
    #Novo Pedido G
    print('Deseja pedir mais alguma coisa?')
    novo_pedido_G = int(input('1 - Sim | 0 - Não: '))
    if novo_pedido_G == (1):
      continue
    elif novo_pedido_G == (0):
      print('O valor total do seu pedido foi de {:.2f}R$ ,muito obrigado utilizar nossos serviços,tenha um ótimo dia!'.format(valor))
      break
    else:
      print('Resposta Inválida')
      continue
  else:
    print('Entrada Inválida, escolha o tamanho (M/G): ')
    continue