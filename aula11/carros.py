class Carro(object):

    def __init__(self, caminho):
        self.caminho = caminho

    def andar(self, caminho):
        self.caminho = caminho
        print(f'Andando pela {self.caminho}')


class Fusca(Carro):

    def __init__(self, caminho):
        self.caminho = caminho

    def correr(self, caminho):
        self.caminho = caminho
        super(Fusca, self).andar()


class Ferrari(Carro):

    def __init__(self, caminho):
        self.caminho = caminho

    def andar(self):
        print(f"Correndo muito")
