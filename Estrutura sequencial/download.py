'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

# Solicitar ao usuário o tamanho do arquivo em MB e a velocidade do link de Internet em Mbps
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Converter a velocidade da Internet para MB por segundo (1 byte = 8 bits)
velocidade_internet_mbps_para_mbps = velocidade_internet_mbps / 8
# Calcular o tempo aproximado de download em segundos
tempo_download_segundos = tamanho_arquivo_mb / velocidade_internet_mbps_para_mbps
# Converter o tempo para minutos
tempo_download_minutos = tempo_download_segundos / 60

# Imprimir o tempo aproximado de download
print("O tempo aproximado de download do arquivo é de cerca de", tempo_download_minutos, "minutos.")

