# -*- coding=Utf-8
from datetime import date

class Pedido(object):

	def __init__(self, nome, valor):
		self.__nome = nome
		self.__valor = valor
		self.__data = None
		self.__status = "NOVO"

	@property
	def nome(self):
		return self.__nome

	@property
	def valor(self, valor):
		return self.__valor

	def pagar(self):
		self.__status = "PAGO"

	def finaliza(self):
		self.__status = "FINALIZADO"
		self.__data = date.today()


class Command_list(object):

	def __init__(self):
		self.__commands = []

	def add_command(self, command):
		self.__commands.append(command)

	def processa_list(self):
		for list in self.__commands:
			list.executa()

if __name__ == "__main__":

	from command import Finalizar, Pagar

	command_list = Command_list()

	pedido_1 = Pedido("Leandro", 190)
	pedido_2 = Pedido("Caio", 1900)

	command_1 = Pagar(pedido_1)
	command_2 = Finalizar(pedido_1)

	command_3 = Pagar(pedido_2)
	command_4 = Finalizar(pedido_2)

	command_list.add_command(command_1)
	command_list.add_command(command_2)
	command_list.add_command(command_3)
	command_list.add_command(command_4)

	command_list.processa_list()