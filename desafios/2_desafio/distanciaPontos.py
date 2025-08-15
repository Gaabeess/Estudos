## Calculadora de distância entre dois pontos

import math

# Solicita ao usuário que insira as coordenadas dos dois pontos
ponto1 = input("Digite as coordenadas do primeiro ponto (x1, y1): ")
ponto2 = input("Digite as coordenadas do segundo ponto (x2, y2): ")

# Função para calcular a distância entre dois pontos no plano cartesiano
def calcular_distancia(ponto1, ponto2):

    # Extrai as coordenadas dos pontos
    x1, y1 = map(float, ponto1.split(","))
    x2, y2 = map(float, ponto2.split(",")) 

    # Calcula a distância entre os dois pontos usando a fórmula da distância euclidiana
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Retorna a distância calculada
    return distancia

# Exibe o resultado da distância entre os pontos
print(f"A distância entre os pontos ({ponto1}) e ({ponto2}) é: {calcular_distancia(ponto1, ponto2)}")