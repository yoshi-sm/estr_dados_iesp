"""Crie um programa que o usuário digite uma sequência de valores (de tamanho dinâmico)
numa única variável, chamada registro. Em seguida, mostre os valores armazenados."""


def coletor(lista):
    valor = input("Digite um valor e pressione ENTER ou pressione ENTER para encerrar: ")
    if valor == "":
        return False
    else:
        lista.append(valor)
        return True


def main():
    registro = []
    continuar = True
    while continuar:
        continuar = coletor(registro)

    for i in registro:
        print(i)


main()
