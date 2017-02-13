# -*- coding=Utf-8 -*-

from datetime import date

class Contrato(object):

	def __init__(self, data, nome, titulo):
		self.__data = data
		self.__nome = nome
		self.__titulo = titulo
		self.__descricao = "CRIADO"

	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self, data):
		self.__data = data

	@property
	def nome(self):
		return self.__nome

	@property
	def descricao(self):
		self.descricao

	@descricao.setter
	def descricao(self, descricao):
		self.__descricao = descricao

	@nome.setter
	def nome(self, nome):
		self.__nome = nome

	@property
	def titulo(self):
		return self.__titulo

	@titulo.setter
	def titulo(self, titulo):
		self.__titulo = titulo	

	def restaurar_contrato(self, old_state):
		self.__data = old_state.data
		self.__nome = old_state.nome
		self.__titulo = old_state.titulo

	def create_state(self):
		return Estado(Contrato(data = self.data, nome = self.nome, titulo=self.titulo))

	def avanca(self):
		if self.descricao == "CRIADO":
			self.descricao = "EM APROVACAO"
		if self.descricao == "EM APROVACAO":
			self.descricao = "FILA PROCESSAMENTO"
		if self.descricao == "FILA PROCESSAMENTO":
			self.descricao = "APROVADO"

	def salva_estado(self):
		return Estado(Contrato(data=self.data, nome=self.nome, titulo=self.titulo))

class Estado(object):

	def __init__(self, contrato):
		self.__contrato = contrato

	@property
	def contrato(self):
		return self.__contrato
		

class Historico(object):

	def __init__(self):
		self.__historico_de_estado = []

	def add_estado(self, estado):
		self.__historico_de_estado.append(estado)

	def get_estado_by_index(self, index):
		return self.__historico_de_estado[index]

	def list_all(self):
		return self.__historico_de_estado

if __name__ == "__main__" : 

	historico = Historico()
	
	contrato = Contrato(data= date.today, nome="Edson Pita", titulo="Bradesco Seguros")
	historico.add_estado(contrato.salva_estado())

	contrato.avanca()
	historico.add_estado(contrato.salva_estado())

	contrato.avanca()
	historico.add_estado(contrato.salva_estado())

	print len(historico.list_all())

