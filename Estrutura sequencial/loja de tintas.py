'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro 
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

# Definição dos dados dos produtos
litros_por_metro_quadrado = 1 / 6
litro_18 = 18
lata_preco1 = 80
litro_36 = 3.6
lata_preco2 = 25
folga = 1.1  # 10% de folga

# Entrada do usuário para o tamanho da área a ser pintada
tamanho_area = float(input("Digite o tamanho da área em metros quadrados: "))

# Cálculo da quantidade de tinta necessária, considerando a folga
quantidade_litros_total = tamanho_area * litros_por_metro_quadrado * folga

# Calculando a quantidade de latas e galões necessários para cada opção
latas_18_necessarias = math.ceil(quantidade_litros_total / litro_18)
galoes_36_necessarios = math.ceil(quantidade_litros_total / litro_36)

# Calculando o preço total para cada opção
preco_total_latas18 = latas_18_necessarias * lata_preco1
preco_total_galoes36 = galoes_36_necessarios * lata_preco2

# Calculando a melhor combinação para minimizar o desperdício de tinta
melhor_combinacao = None
menor_desperdicio = float('inf')

for latas_18_utilizadas in range(latas_18_necessarias + 1):
    galoes_36_utilizados = math.ceil((quantidade_litros_total - latas_18_utilizadas * litro_18) / litro_36)
    quantidade_litros_utilizados = latas_18_utilizadas * litro_18 + galoes_36_utilizados * litro_36
    desperdicio = quantidade_litros_utilizados - quantidade_litros_total
    if desperdicio < menor_desperdicio:
        melhor_combinacao = (latas_18_utilizadas, galoes_36_utilizados)
        menor_desperdicio = desperdicio

# Calculando o preço total para a melhor combinação
preco_total_melhor_combinacao = melhor_combinacao[0] * lata_preco1 + melhor_combinacao[1] * lata_preco2

# Imprimindo os resultados
print("Quantidade de tinta necessária:")
print("Comprar apenas latas de 18 litros:", latas_18_necessarias, "latas")
print("Comprar apenas galões de 3,6 litros:", galoes_36_necessarios, "galões")
print("Melhor combinação para minimizar o desperdício de tinta:")
print("Latas de 18 litros:", melhor_combinacao[0])
print("Galões de 3,6 litros:", melhor_combinacao[1])
print("Preço total para comprar apenas latas de 18 litros: R$", preco_total_latas18)
print("Preço total para comprar apenas galões de 3,6 litros: R$", preco_total_galoes36)
print("Preço total para a melhor combinação: R$", preco_total_melhor_combinacao)











