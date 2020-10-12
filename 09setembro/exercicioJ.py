"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Gênero Inválido. """


def main():

    letra = input('Digite "F" ou "M": ')
    if letra == "F":
        print("Feminino!")
    elif letra == "M":
        print("Masculino!")
    else:
        print("Gênero Inválido!")


main()
