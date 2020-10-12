"""Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""


def main():
    soma = 0
    quant_notas = 2
    for tmp in range(quant_notas):
        nota = float(input(f"Digite a nota {tmp+1}: "))
        soma += nota

    media = soma/quant_notas

    if media >= 7:
        print("Aprovado!")
    elif media < 7:
        print("Reprovado!")
    elif media == 10:
        print("Aprovado com Distinção!")


main()
