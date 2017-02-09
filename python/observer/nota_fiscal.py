# -*- coding=Utf-8 -*-

from datetime import date

class NotaFiscal(object):

	def __init__(self, titulo, itens, descricao='', data_vencimento=date.today(), observers=[]):
		self.__titulo = titulo
		self.__itens = itens
		self.__descricao = descricao
		self.__data_vencimento = data_vencimento

		for obs in observers:
			obs(self)

	@property
	def titulo(self):
		return self.__titulo

class Item(object):
	def __init__(self, nome, valor):
		self.nome = nome
		self.valor = valor

if __name__ == "__main__":

	from observer import imprime, envia_por_email, compartilha_no_docs

	itens = []
	itens.append(Item("Teste", 10.00))
	itens.append(Item("Teste2", 80.00))

	nota_fical = NotaFiscal('leleco note', itens, observers=[imprime, envia_por_email, compartilha_no_docs])