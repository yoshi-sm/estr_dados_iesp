def diaDoProgramador(ano):
    #caso o ano seja 1918
    if ano == 1918:
        return "26.09.1918"

    #caso seja antes de 1918
    elif ano < 1918:
        #ano bissexto
        if ano % 4 == 0:
            return f"12.09.{ano}"
        #ano comum
        else:
            return f"13.09.{ano}"

    #caso seja depois de 1918
    else:
        #ano bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            return f"12.09.{ano}"
        #ano comum
        else:
            return f"13.09.{ano}"


def main():
    #garantindo que o ano esteja no intervalo valido
    ano = int(input("Digite o ano desejado (valor inteiro entre 1700 e 2700 por favor): "))
    while not(1700 <= ano <= 2700):
        print("Ano inválido!\n")
        ano = int(input("Digite o ano desejado (valor inteiro entre 1700 e 2700 por favor): "))
    #print
    print(diaDoProgramador(ano))


main()
