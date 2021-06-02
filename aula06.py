def somar(numero1, numero2):
    print(numero1 + numero2)

def subtrair(numero1, numero2):
    print(numero1 - numero2)

def imprime_parametros(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

somar(valor1, valor2)
subtrair(valor1, valor2)

imprime_parametros(nome="Ana", sobrenome="Maria")
