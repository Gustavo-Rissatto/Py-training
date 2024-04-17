#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre;
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Por favor, insira um número real: "))

# Calcular o produto do dobro do primeiro com metade do segundo
dobro = (numero1 * 2) * (numero2 / 2)
print("O produto do dobro do primeiro com metade do segundo é:", dobro)

# Calcular a soma do triplo do primeiro com o terceiro
triplo = (numero1 * 3) + numero_real
print("A soma do triplo do primeiro com o terceiro é:", triplo)

# Calcular o terceiro elevado ao cubo
cubo = numero_real ** 3
print("O terceiro elevado ao cubo é:", cubo)