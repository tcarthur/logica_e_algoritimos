#Indentificação do aluno
print('Nome: Arthur Tavares Carvalho\n'
      'RU: 4158824')


#lista De armazenamento de produtos
listaDeProdutos = []

#Função para Cadastrar Produtos
def cadastrarProduto(codigo):
  print('BEM-VINDO AO CADASTRO DE PRODUTO')
  print('O Codigo do produto a ser cadastrado é: {}'.format(codigo))
  #PERGUNTE O NOME DO PRODUTO
  nomeProduto = input('Digite o nome do Produto:\n>>>')
  #PERGUNTE O NOME DO FABRICANTE
  fabricante = input('Digite o nome do Fabricante:\n>>>')
  #PERGUNTE O VALOR DO PRODTUDO
  valorDoProduto = float(input('Digite o valor do produto:\n>>>'))
  #CADA PRODUTO CADASTRADO DEVE TER OS SEUS DADOS ARMAZENADOS NUM DICIONÁRIO 
  dicionarioDeProdutos = {'codigo' : codigo,
                          'nomeProduto' : nomeProduto,
                          'fabricante' : fabricante,
                          'valorProduto' : valorDoProduto,
                          }
  listaDeProdutos.append(dicionarioDeProdutos.copy())

#Função para Consultar Produtos
def consultarProduto():
  while True:
    try:
      print('BEM-VINDO A CONSULTA DE PRODUTO')
      opcaoConsultar = int(input('Entre com a opção desejada\n'
                        '1 - Consultar todos os Produtos\n'
                        '2 - Consultar por código\n'
                        '3 - Consultar por Fabricante\n'
                        '4 -  Retornar\n'
                        '>>>'))
  #Consultar todos os produtos
      if opcaoConsultar == 1:
        print('Bem-vindo a consultar todos')
        for produto in listaDeProdutos:
          for key, value in produto.items():
            print("{} : {}".format(key, value))
  #Consultar produtos por código
      elif opcaoConsultar == 2:
        print('Bem-vindo a consulta por código')
        entrada = int(input('Digite o Código do produto desejado\n>>>'))
        for produto in listaDeProdutos:
          if(produto['codigo'] == entrada):
              for key, value in produto.items():
                print("{} : {}".format(key, value))
  #Consultar Produtos por Fabricante
      elif opcaoConsultar == 3:
        print('Bem-vindo a consulta por fabricante')
        entrada = input('Digite o fabricante do produto desejado\n>>>')
        for produto in listaDeProdutos:
          if(produto['fabricante'] == entrada):
              for key, value in produto.items():
                print("{} : {}".format(key, value))
      elif opcaoConsultar == 4:
        break
  #Retornar
    except ValueError:
      print('Insira apenas valores disponíveis no menu')
  
  
#Função para remover produtos
def removerProduto():
  print('BEM-VINDO A REMOÇÃO DE PRODUTOS')
  #Dentro da função perguntar qual o código do produto que se deseja remover
  entrada = int(input('Digite o código do produto:\n>>>'))
  for produto in listaDeProdutos:
    if(produto['codigo'] == entrada):
      listaDeProdutos.remove(produto)

#Main do Código
print('Bem Vindo ao Controle de Estoque do Arthur Tavares')
codigoProduto = 0
while True:
  try:
    opcao = int(input('Digite a opção desejada:'
                      '\n 1- Cadastrar Produto '
                      '\n2- Consultar Produto'
                      '\n3 - Remover Produto'
                      '\n4 - Sair'
                      '\n >>'))
    if opcao == 1:
      codigoProduto += 1
      cadastrarProduto(codigoProduto)
    elif opcao == 2:
      consultarProduto()
    elif opcao == 3:
      removerProduto()
    elif opcao == 4:
      print('Programa Finalizado!')
      break
    else:
      print('Insira apenas os valores disponíveis no menu')
  except ValueError:
    print('Digite um valor válido')
    continue