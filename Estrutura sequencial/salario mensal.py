#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = int(input("digite o valor ganho por hora:"))
mes = int(input("quantas horas são trabalhadas mensalmente?:"))

salario = hora*mes

print("o valor ganho neste mês, foi de:",salario)
