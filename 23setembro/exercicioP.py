"""Dado um inteiro não-negativo n, determinar n!
Por exemplo: 3! = 3 x 2 x 1"""


def mainfor(num):
    for i in range(num-1, 0, -1):
        num *= i
    return num


def mainwhile(num):
    count = num-1
    while count > 0:
        num *= count
        count -= 1

    return num


def main():
    numero = int(input("Digite um número inteiro não negativo: "))

    if numero < 0:
        print("Número negativo!")
    elif numero == 0:
        print(f"{numero}! = 1")
    else:
        # for
        print(f"{numero}! = {mainfor(numero)}")

        # while
        print(f"{numero}! = {mainwhile(numero)}")


main()
