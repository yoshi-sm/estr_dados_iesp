"""Entrei no banco e quero saber o meu tempo médio de espera.
Faça um programa que calcule e mostre a média aritmética de um cliente, baseado
nos tempos de espera dos clientes anteriores (máximo 5  clientes). """


def main1():
    cliente = 1
    tempo = 0
    quant = int(input("Digite a quantidade de clientes: "))
    while cliente < quant + 1:
        tempo += int(input(f"Digite o tempo de espera do cliente {cliente} em minutos (inteiro): "))
        cliente += 1

    print(f"O tempo médio é de {tempo/quant} minutos")


main1()


def main2():
    tempo = 0
    quant = int(input("Digite a quantidade de clientes: "))
    for i in range(quant):
        tempo += int(input(f"Digite o tempo de espera do cliente {i+1}: "))
    print(f"O tempo médio é de {tempo / quant} minutos")


main2()
