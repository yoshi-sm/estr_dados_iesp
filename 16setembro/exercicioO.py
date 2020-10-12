"""Dada uma sequência de números inteiros, imprimir seus quadrados.
Entradas do programa:
        nº de início da sequência = 0
        nº de fim da sequência = 4
Saída do programa:
         sequência : 0, 1, 4, 9, 16"""


def main1():
    inicio = int(input("Digite o numero de inicio da sequencia: "))
    fim = int(input("Digite o numero final da sequencia: "))
    print(inicio ** 2, end='')
    inicio += 1
    while inicio <= fim:
        print(f", {inicio ** 2}", end='')
        inicio += 1
    print("\n\n")


main1()


def main2():
    inicio = int(input("Digite o numero de inicio da sequencia: "))
    fim = int(input("Digite o numero final da sequencia: "))
    print(inicio ** 2, end='')
    inicio += 1
    for i in range(inicio, fim + 1):
        print(f", {i ** 2}", end='')


main2()
