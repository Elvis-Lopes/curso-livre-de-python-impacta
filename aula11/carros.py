class Carro(object):

    def __init__(self, caminho):
        self.caminho = caminho


    def andar(self):
        self.caminho = 'Rua'
        print(f'Andando pela {self.caminho}')

class Fusca(Carro):
    def __init__(self, caminho):
        self.caminho = caminho

    def correr(self):
        self.caminho = "pista"
        super(Fusca, self).andar()