"""Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""


def prob_um(a, b):
    return (2*a) * (b/2)


def prob_dois(a, c):
    return (3*a) + c


def prob_tres(c):
    return c**3


def main():
    num_int1 = int(input("Digite um numero inteiro: "))
    num_int2 = int(input("Digite outro numero inteiro: "))
    num_real = float(input("Digite um numero real: "))

    print(f'Resultados: \n{prob_um(num_int1, num_int2)}\n{prob_dois(num_int1, num_real)}\n{prob_tres(num_real)}')


main()
