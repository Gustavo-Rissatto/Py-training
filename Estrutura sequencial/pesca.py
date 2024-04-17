#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o 
#estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um 
#programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável
#excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("digite a quantidade em quilos, de peixe:"))
limite = 50
if peso_peixe > limite:
    excesso = peso_peixe - limite
    multa = excesso*4.00
    print("joão excedeu o peso limite:")
    print("joão excedeu o peso em:",excesso)
    print("joão deve pagar R$",multa,"em multa:")
else:
    print("joão não excedeu o limite")