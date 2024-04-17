#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

cobert_litros = 3
litros_lata = 18
valor_lata = 80.00


metros_quadrados = float(input("Digite o tamanho em metros quadrados da area:"))

litros_necessarios = metros_quadrados / cobert_litros
latas_necessarias = math.ceil(litros_necessarios / litros_lata)
preco_total = latas_necessarias * valor_lata

print("sera usada",latas_necessarias,"latas para pintar.")
print("o preço total, fica em R$",preco_total,".")

