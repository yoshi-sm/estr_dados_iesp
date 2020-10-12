"""Digite um número e descubra se ele é um palíndromo.
Palíndromo:
1º algarismo de n é igual ao seu último algarismo,
2º algarismo de n é igual ao penúltimo algarismo, e assim sucessivamente."""


def main():
    numero = input("Digite um número inteiro: ")
    verificador = True
    for i in range(int(len(numero)/2)):
        if numero[i] != numero[-(i+1)]:
            verificador = False

    if verificador:
        print(f'"{numero}" é um palíndromo.')
    else:
        print(f'"{numero}" não é um palíndromo.')


main()
