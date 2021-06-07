from pessoas import Pessoa
from carros import Carro, Fusca, Ferrari


#p = Pessoa()
#p.nome = "João"
#print(p.nome)
#p.salvar()

#p = Pessoa()
#p.nome = 'José'
#p.salvar("João")

#c = Carro('Rua')
#c.andar()
#print(c.caminho)
#c.caminho = "Estrada"
#print(c.caminho)

f = Fusca("Praia")
print(f.caminho)
print(f.andar('avenida'))

ferrari = Ferrari("Avenida")
ferrari.andar()