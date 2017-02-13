from abc import ABCMeta, abstractmethod
from pdb import set_trace
from visitor import Visitor

class Numero(object):

	def __init__(self, numero):
		self.__numero = numero

	def avalia(self):
		return self.__numero

	def aceita(self, visitor):
		visitor.visita_numero(self)


class Operacoes(object):

	__metaClass__ = ABCMeta

	def __init__(self, operacoes_esquerda, operacoes_direita):
		self.__operacoes_esquerda = operacoes_esquerda
		self.__operacoes_direita = operacoes_direita

	@property
	def operacoes_esquerda(self):
		return self.__operacoes_esquerda

	@property
	def operacoes_direita(self):
		return self.__operacoes_direita

	@abstractmethod
	def avalia(self):
		pass

	@abstractmethod
	def aceita(self, visitor):
		pass

class Subtracao(Operacoes):

	def __init__(self, operacoes_esquerda, operacoes_direita):
		super(Subtracao, self).__init__(operacoes_esquerda, operacoes_direita)

	def avalia(self):
		return self.operacoes_esquerda.avalia() - self.operacoes_direita.avalia()

	def aceita(self, visitor):
		visitor.visita_subtracao(self)


class Soma(Operacoes):

	def __init__(self, operacoes_esquerda, operacoes_direita):
		super(Soma, self).__init__(operacoes_esquerda, operacoes_direita)

	def avalia(self):
		return self.operacoes_esquerda.avalia() + self.operacoes_direita.avalia()	

	def aceita(self, visitor):
		visitor.visita_soma(self) 


if __name__ == "__main__":
	expressao_esquerda = Subtracao(Numero(10), Numero(5))
	expressao_direita = Soma(Numero(2), Numero(10))
	expressao_conta = Soma(expressao_esquerda, expressao_direita)
	visitor = Visitor()
	expressao_conta.aceita(visitor)