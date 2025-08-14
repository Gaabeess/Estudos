temperatura_fahrenheit = input("Digite a temperatura em Fahrenheit: ")  # input do usuário

temperatura_fahrenheit = float(temperatura_fahrenheit)                  # conversão de stg para float
temperatura_Celsius = (temperatura_fahrenheit - 32) * 5 / 9             # fórmula de conversão de Fahrenheit para Celsius
temperatura_Celsius = round(temperatura_Celsius, 2)                     # arredondamento para duas casas decimais

print("Temperatura em Celsius:", temperatura_Celsius)                   # exibição do resultado
# Exemplo de uso: se o usuário digitar 32, a saída será "Temperatura em Celsius: 0.0"
# Se o usuário digitar 212, a saída será "Temperatura em Celsius: 100.0"