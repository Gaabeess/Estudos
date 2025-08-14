## Calculadora de Raízes de Função Quadrada

# Solicita ao usuário que insira a função quadrada
funcao_quadrada = input("Digite a função quadrada no formato ax^2 + bx + c: ")

# Função para extrair os coeficientes a, b e c da função quadrada
def extrair_coeficientes(funcao):

    # Remove espaços e substitui '-' por '+-' para facilitar a separação dos termos
    funcao = funcao.replace(" ", "").replace("-", "+-")

    # Separa os termos da função
    termos = funcao.split("+")

    # Inicializa os coeficientes a, b e c
    a = b = c = 0

    # Percorre os termos para identificar e extrair os coeficientes
    for termo in termos:

        # Extrai o coeficiente de x^2
        if "x^2" in termo:
        
            # Trata o caso onde o coeficiente é 1 ou -1
            a = int(termo.replace("x^2", "")) if termo.replace("x^2", "") not in ["", "+", "-"] else int(termo.replace("x^2", "1")) if termo.replace("x^2", "") in ["+", ""] else -1

        # Extrai o coeficiente de x
        elif "x" in termo:
        
            # Trata o caso onde o coeficiente é 1 ou -1
            b = int(termo.replace("x", "")) if termo.replace("x", "") not in ["", "+", "-"] else int(termo.replace("x", "1")) if termo.replace("x", "") in ["+", ""] else -1
            
        # Extrai o termo constante
        elif termo:

            # Trata o caso onde o termo é apenas um número
            c = int(termo)

            # Retorna os coeficientes a, b e c como inteiros
            return a, b, c
    

# Calcula as raízes da função quadrada usando a fórmula de Bhaskara
def calcular_raizes(a, b, c): 

    # Extrai os coeficientes da função quadrada
    a, b, c = extrair_coeficientes(funcao_quadrada) 
    
    # Verifica se o coeficiente 'a' é zero
    if a == 0:

        # Lança um erro se 'a' for zero, pois não é uma função quadrada
        raise ValueError("O coeficiente 'a' não pode ser zero em uma função quadrada.")
    
    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c

    # Calcula as raízes com base no valor de delta
    if delta < 0:

        # Se delta for negativo, não há raízes reais
        return None, None
    
    # Se delta for zero, há uma raiz real (raiz dupla)
    elif delta == 0:

        # Calcula a raiz única
        raiz = -b / (2*a)

        # Retorna a raiz dupla
        return raiz, raiz
    
    # Se delta for positivo, há duas raízes reais distintas
    else:

        # Calcula as duas raízes usando a fórmula de Bhaskara
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)

        # Retorna as duas raízes distintas
        return raiz1, raiz2
    
# Chama a função para calcular as raízes e armazena os resultados
raiz1, raiz2 = calcular_raizes(*extrair_coeficientes(funcao_quadrada))

# Exibe as raízes encontradas
if raiz1 is None and raiz2 is None:
    print("A função não possui raízes reais.")
elif raiz1 == raiz2:
    print(f"A função possui uma raiz real: {raiz1}")
else:
    print(f"A função possui duas raízes reais: {raiz1} e {raiz2}")

# Exemplo de uso:
# Entrada: 2x^2 - 4x + 2
# Saída: A função possui uma raiz real: 1.0