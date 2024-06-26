valorHora = int(input("Digite o valor da sua hora: "))
quantidadeHora = int(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = (valorHora * quantidadeHora)


if salarioBruto <= 900:
    IR = 0
elif salarioBruto > 900 and salarioBruto <= 1500:
    IR = (salarioBruto * 0.05)
elif salarioBruto > 1500 and salarioBruto <= 2500:
    IR = (salarioBruto * 0.10)
else:
    IR = (salarioBruto * 0.20)


INSS = (salarioBruto * 0.10)
FGTS = (salarioBruto * 0.11)
totalDesconto = (IR + INSS)
salarioLiquido = (salarioBruto - totalDesconto)


print('Salário Bruto: ', salarioBruto)
print('Desconto do Imposto de Renda: ', IR)
print('Desconto do INSS: ', INSS)
print('Desconto do FGTS: ',FGTS)
print('Total de descontos: ',totalDesconto)
print('Salário Liquido: ', salarioLiquido)