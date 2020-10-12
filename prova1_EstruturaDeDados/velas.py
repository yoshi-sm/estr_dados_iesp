def numVelasAniversario(velasAltura): #pycharm ta mandando botar a funcao e parametro em minúsculo!
    #funcao da questao
    temp = 0
    for i in velasAltura:
        if temp < i:
            temp = i

    return velasAltura.count(temp)


def main():
    #recebendo o tamanho da lista velasAltura e obrigando o tamanho a ficar entre 1 e 100000
    tamanho = 0
    while not 1 <= tamanho <= 100000:
        tamanho = int(input("Digite a quantidade de velas: "))
        if not(1 <= tamanho <= 100000):
            print("Valor de tamanho inválido, tente novamente (1 <= quantidade de velas <= 100000).")

    alturas = input("Digite os valores das alturas das velas em inteiros separados por espaço"
                    " (Exemplo: 5 3 4 1 6 7): ")

    verificador = True

    while verificador:
        verificador = False
        #verificacao se o tamanho bate com a quantidade de alturas dadas
        if len(alturas.split(" ")) != tamanho or alturas == "":
            print("Quantidade de valores de alturas de velas não corresponde à quantidade de velas!\n"
                  f"Quantidade = {tamanho}\n")
            verificador = True

        for i in alturas.split(" "):
            #verificando se o usuario colocou letras por algum motivo
            try:
                int(i)
            except ValueError:
                print("Os valores das alturas devem ser números!\n")
                verificador = True
                break
            #verificando se o numero esta no intervalo correto
            if int(i) < 1 or int(i) > 10000000:
                print("As alturas devem ser limitadas em 1 <= altura <= 10000000\n")
                verificador = True
                break

        #caso o dado "alturas" nao passe em algum teste, alturas sera pedido denovo
        if verificador:
            alturas = input("Digite os valores das alturas das velas serparados por espaço"
                            " (Exemplo: 5 3 4 1 6 7): ")

    #gerando velasAltura a partir de altura
    velasAltura = []
    for i in alturas.split(" "):
        velasAltura.append(int(i))

    #saida do codigo
    print(f"Número de velas com altura máxima: {numVelasAniversario(velasAltura)}")


main()
