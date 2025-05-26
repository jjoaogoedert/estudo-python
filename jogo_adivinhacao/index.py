import random

class NumeroAleatorio():
    numero_ale = random.randint(0,5)

    def __init__(self):
        self.numero_ale = random.randint(0,5)

    def gerarNovoNumero(self):
        self.numero_ale = random.randint(0,5)

    @staticmethod
    def validaNumero(numero):
        try:
            numero = int(numero)
            return True
        except ValueError:
            return False

    def validaAcerto(self,numero):
        if numero == self.numero_ale:
            return True
        else:
            return False