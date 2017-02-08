# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento(object):

    __metaclass_ = ABCMeta

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

class Em_aprovacao(Estado_de_um_orcamento):
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception("Um orcamento em aprovação não pode ser finalizado")

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto(orcamento.valor * 0.05)
        

class Aprovado(Estado_de_um_orcamento):
    def aprova(self, orcamento):
        raise Exception("O orcamento já está aprovado")

    def reprova(self, orcamento):
        Exception("Um orcamento aprovado não pode ser cancelado")

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto(orcamento.valor * 0.02)

class Reprovado(Estado_de_um_orcamento):
    def aprova(self, orcamento):
        raise Exception("Um orcamento cancelado não pode ser aprovado")

    def reprova(self, orcamento):
        Exception("O orcamento já está cancelado")

    def finaliza(self, orcamento):
        Exception("O orcamento já está cancelado e se econtra finalizado")

    def aplica_desconto_extra(self, orcamento):
        Exception("O orcamento reprovado não recebe desconto extra")

class Finalizado(Estado_de_um_orcamento):
    def aprova(self, orcamento):
        raise Exception("Orcamento finalizado não pode ser aprovado")

    def reprova(self, orcamento):
        Exception("Orcamento finalizado não pode ser cancelado")

    def finaliza(self, orcamento):
        Exception("Orcamento finalizado não pode ser finalizado")

    def aplica_desconto_extra(self, orcamento):
        Exception("Orcamento finalizado não recebe desconto extra")


class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.__desconto_extra = 0.0
        self.estado_atual = Em_aprovacao()

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    def adiciona_desconto(self, desconto):
        self.__desconto_extra += desconto

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)

class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    orcamento.aplica_desconto_extra() 
    print orcamento.valor # imprime 522.5 porque descontou 5% de 550.0
    orcamento.aprova()

    orcamento.aplica_desconto_extra() 
    print orcamento.valor # imprime 512.05 porque descontou 2% de 522.5
    orcamento.finaliza()

    orcamento.aplica_desconto_extra()