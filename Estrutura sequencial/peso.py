#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Digite sua altura em metros:"))
genero = input("Qual o seu genero, Masculino ou Feminino?:")

if (genero=="masculino"):
    peso = (72.7*altura) - 58
    print("o seu peso ideal é de:",peso)

elif (genero=="feminino"):
    peso = (62.1*altura) -44.7
    print("o seu peso ideal é de:",peso)

else:
    print("entrada invalida:")
    
    
