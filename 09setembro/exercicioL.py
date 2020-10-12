"""Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""


def main():

    produtoA = float(input("Digite o preço do produto A: "))
    produtoB = float(input("Digite o preço do produto B: "))
    produtoC = float(input("Digite o preço do produto C: "))

    if produtoA < produtoB and produtoA < produtoC:
        print('Você deve comprar o produto A pois ele é o mais barato')
    elif produtoB < produtoC and produtoB < produtoA:
        print('Você deve comprar o produto B pois ele é o mais barato')
    else:
        print('Você deve comprar o produto C pois ele é o mais barato')


main()
