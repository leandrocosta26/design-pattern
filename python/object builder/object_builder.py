# -*- coding=Utf-8 -*-
from datetime import date
from nota_fiscal import NotaFiscal

class ObjectBuilder(object):

	def __init__(self):
		self.__titulo = None
		self.__itens = None
		self.__descricao = None
		self.__data_vencimento = None

	def com_titulo(self, titulo):
		self.__titulo = titulo
		return self

	def com_itens(self, itens):
		self.__itens = itens
		return self

	def com_descricao(self, descricao):
		self.__descricao = descricao
		return self

	def com_data_vencimento(self, data):
		self.__data_vencimento = data
		return self

	def constroi(self):
		if self.__titulo is None:
			raise Exception("Titulo não pode estar vazio")

		if self.__itens is None:
			raise Exception("Itens não pode sem vazio")

		if self.__descricao is None:
			self.__descricao = ''

		if self.__data_vencimento is None:
			self.__data_vencimento = date.today()

		return NotaFiscal(titulo=self.__titulo, itens=self.__itens, descricao=self.__descricao, data_vencimento=self.__data_vencimento)