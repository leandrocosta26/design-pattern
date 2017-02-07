# -*- coding: UTF-8 -*-
# calculador_de_desconto.py

from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_Descontos(object):

	def calcular(self, orcamento):
		return Desconto_por_cinco_itens(
					Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
				).calcula(orcamento)

if __name__  == "__main__" : 

	from orcamento import Orcamento, Item
	
	orcamento = Orcamento()
	orcamento.adiciona_item(Item("ITEM -1", 100.0))
	orcamento.adiciona_item(Item("ITEM -2", 50.0))
	orcamento.adiciona_item(Item("ITEM -3", 400.0))

	desconto = Calculador_de_Descontos().calcular(orcamento)
	print desconto