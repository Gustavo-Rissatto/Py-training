#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Digite a altura da pessoa (em metros):"))

peso_ideal = (72.7 * altura) - 58

print ("o peso ideal para uma pessoa com a altura", altura, "metros é:",peso_ideal,"quilos.")