class Visitor(object):

    def visita_soma(self, soma):

        print '(',
        soma.operacoes_esquerda.aceita(self)
        print '+',
        soma.operacoes_direita.aceita(self)
        print ')',

    def visita_subtracao(self, subtracao):
        print '(',
        subtracao.operacoes_esquerda.aceita(self)
        print '-',
        subtracao.operacoes_direita.aceita(self)
        print ')',

    def visita_numero(self, numero):

        print numero.avalia(),