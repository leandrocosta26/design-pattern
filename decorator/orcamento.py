from abc import ABCMeta, abstractmethod
# -*- coding: UTF-8 -*-

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


class Em_aprovacao(EstadoDoOrcamento):
    pass

class Aprovado(EstadoDoOrcamento):
    pass

class Reprovado(EstadoDoOrcamento):
    pass

class Finalizado(EstadoDoOrcamento):
    pass


class Orcamento(object):

    def __init__(self):
        self.__itens = []

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total

    def obter_itens(self):

        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

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