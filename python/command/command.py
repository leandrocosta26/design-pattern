# -*- coding=Utf-8
from abc import ABCMeta, abstractmethod

class Command(object):

	__metaClass__ = ABCMeta

	def __init__(self, pedido):
		self.__pedido = pedido

	@property
	def pedido(self):
		return self.__pedido

	@abstractmethod
	def executa(self):
		pass

class Pagar(Command):

	def __init__(self, pedido):
		super(Pagar, self).__init__(pedido)

	def executa(self):
		self.pedido.pagar()

class Finalizar(Command):

	def __init__(self, pedido):
		super(Finalizar, self).__init__(pedido)

	def executa(self):
		self.pedido.finaliza()