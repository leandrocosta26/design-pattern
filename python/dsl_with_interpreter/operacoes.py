from abc import ABCMeta, abstractmethod
from pdb import set_trace

class Numero(object):

	def __init__(self, numero):
		self.__numero = numero

	def avalia(self):
		return self.__numero

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

class Subtracao(Operacoes):

	def __init__(self, operacoes_esquerda, operacoes_direita):
		super(Subtracao, self).__init__(operacoes_esquerda, operacoes_direita)

	def avalia(self):
		return Numero(self.operacoes_esquerda.avalia() - self.operacoes_direita.avalia())

class Soma(Operacoes):

	def __init__(self, operacoes_esquerda, operacoes_direita):
		super(Soma, self).__init__(operacoes_esquerda, operacoes_direita)

	def avalia(self):
		return Numero(self.operacoes_esquerda.avalia() + self.operacoes_direita.avalia())	


if __name__ == "__main__":
	operacoes_esquerda = Subtracao(Numero(100), Numero(10)).avalia()
	print operacoes_esquerda.avalia()
	operacoes_direita = Soma(Numero(100), Numero(10)).avalia()
	print operacoes_direita.avalia()
	rest_expression = Soma(operacoes_esquerda, operacoes_direita).avalia()
	print rest_expression.avalia()