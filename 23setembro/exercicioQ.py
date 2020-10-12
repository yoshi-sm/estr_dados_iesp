"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada. """


def tabuadafor(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")


def main():
    numero = int(input("Para qual número você deseja ver a tabuada? (entre 1 e 10)\n"))
    if 10 >= numero >= 1:
        tabuadafor(numero)
    else:
        print("Número inválido")


main()
