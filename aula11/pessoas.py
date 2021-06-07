class Pessoa(object):
    nome = None

    def salvar(self, nome):
        self.nome = nome
        print(f'Salvando, {self.nome}')