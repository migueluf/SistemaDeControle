##Sistema de Gerenciamento de Estoque

class Produto:
  def __init__(self, id, nome, categoria_id, quantidade, preco):
    self.id = id
    self.nome = nome
    self.categoria_id = categoria_id
    self.quantidade = quantidade
    self.preco = preco

class Categoria:
  def __init__(self, id, nome):
    self.id = id
    self.nome = nome

class Movimentacao:
  def __init__(self, id, produto_id, quantidade, tipo_movimentacao, data):
    self.id = id
    self. produto_id = produto_id
    self.quantidade = quantidade
    self.tipo_movimentacao = tipo_movimentacao
    self.data = data

def cadastrar_produtos(produtos, contador_produtos):
  id = contador_produtos + 1
  nome = input('Nome do produto: ')
  categoria_id = int(input('ID da Categoria: '))
  quantidade = int(input('Insira a quantidade: '))
  preco = float(input('Insira o preço: '))
  produtos.append(Produto(id, nome, categoria_id,quantidade, preco))
  print("Produto cadastrado com sucesso!")
  return contador_produtos + 1

def consultar_produto_id(produtos, id):
  for produto in produtos:
    if produto.id == id:
      print(f'ID: {produto.id}, Nome: {produto.nome}, Categoria: {produto.categoria_id}, Quantidade: {produto.quantidade}, Preço: {produto.preco}')
      return

  print('Produto não encontrado!')
##Teste cadastro
produtos = []
contador = 0

contador = cadastrar_produtos(produtos, contador)

consultar_produto_id(produtos, contador)

 
  