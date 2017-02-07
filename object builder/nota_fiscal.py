# -*- coding=Utf-8 -*-

from datetime import date

class NotaFiscal(object):

	def __init__(self, titulo, itens, descricao='', data_vencimento=date.today()):
		self.__titulo = titulo
		self.__itens = itens
		self.__descricao = descricao
		self.__data_vencimento = data_vencimento

class Item(object):
	def __init__(self, nome, valor):
		self.nome = nome
		self.valor = valor

if __name__ == "__main__":

	from object_builder import ObjectBuilder

	itens = []
	itens.append(Item("Teste", 10.00))
	itens.append(Item("Teste2", 80.00))

	nota_fical = NotaFiscal('leleco note', itens)
	nota_com_builder = ObjectBuilder().com_titulo('Teste').com_itens(itens).constroi()

	print type(nota_fical)
	print type(nota_com_builder)