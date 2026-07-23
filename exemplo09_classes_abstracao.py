from abc import ABC, abstractmethod


class FormaPagamento(ABC):

    @abstractmethod
    def pagar(self):
        pass

class Pix(FormaPagamento):
    def pagar(self):
        print("Pagamento realizado por Pix.")

class Cartao(FormaPagamento):
    def pagar(self):
        print("Pagamento realizado com cartão.")


pix = Pix()
cartao = Cartao()

pix.pagar()
cartao.pagar()

#Abstração é um conceito da programação orientada a objetos usado para criar uma classe-modelo que define regras para outras #classes.
#
#No Python, usamos ABC para criar uma classe abstrata e @abstractmethod para indicar métodos que devem ser obrigatoriamente #implementados pelas classes filhas.
#
#A classe abstrata serve como base e normalmente não é utilizada para criar objetos diretamente.
