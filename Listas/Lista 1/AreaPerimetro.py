ladoQuadrado = float(input("Informe o lado do quadrado: "))  # input do usuário
# conversão de string para float

area = int(ladoQuadrado ** 2)  # cálculo da área
perimetro = int(4 * ladoQuadrado)  # cálculo do perímetro

print(f"perímetro: {perimetro} - área: {area}")  # exibição do resultado
