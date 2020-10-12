"""Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a. salário bruto.
b. quanto pagou ao IPRF
c. quanto pagou ao INSS.
d. quanto pagou ao sindicato.
e. o salário líquido.
f. o valor descontado"""


def salario_bruto(salario_hora, horas_mes):
    return round(salario_hora * horas_mes, 2)


def iprf(salario_hora, horas_mes):
    return round((salario_bruto(salario_hora, horas_mes)/100) * 11, 2)


def inss(salario_hora, horas_mes):
    return round((salario_bruto(salario_hora, horas_mes)/100) * 8, 2)


def sindicato(salario_hora, horas_mes):
    return round((salario_bruto(salario_hora, horas_mes)/100) * 5, 2)


def salario_liquido(salario_hora, horas_mes):
    return salario_bruto(salario_hora, horas_mes) - iprf(salario_hora, horas_mes) \
           - inss(salario_hora, horas_mes) - sindicato(salario_hora, horas_mes)


def main():
    salario_hora = float(input("Digite quanto você ganha por hora: "))
    horas_mes = float(input("Digite quantas horas você trabalhou no mês: "))

    print(f"O valor do seu salário bruto é de R${salario_bruto(salario_hora, horas_mes)}.\n"
          f"Foram descontados R${iprf(salario_hora, horas_mes)} pelo imposto de renda.\n"
          f"Foram descontados R${inss(salario_hora, horas_mes)} pelo INSS.\n"
          f"Foram descontados R${sindicato(salario_hora, horas_mes)} pelo sindicato.\n"
          f"Seu salário líquido é de R${salario_liquido(salario_hora, horas_mes)}.\n"
          f"O valor total descontado é "
          f"de R${round(salario_bruto(salario_hora, horas_mes) - salario_liquido(salario_hora, horas_mes), 2)}")


main()
