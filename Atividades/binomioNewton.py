# Calculadora do binômio de Newton
# Este programa calcula o coeficiente binomial (n choose k) usando a fórmula n! / (k! * (n - k)!).
# O usuário deve fornecer os valores de n e k.

# Importante: O fatorial de um número negativo não é definido, e o fatorial de 0 e 1 é 1.

# Início do programa
print("Bem vindo á Calculadora do binômio de Newton!")

# Solicita ao usuário os valores de n e k
# n é o número total de elementos, e k é o número de elementos a serem escolhidos.
# O usuário deve inserir números inteiros não negativos, onde k não pode ser maior que n.
n = int(input("Digite o primeiro valor: "))
k = int(input("Digite o segundo valor: "))

# Função para calcular o fatorial de um número
def fatorial(numero):

    """
    Calcula o fatorial de um número.
    Args:
        numero: O número inteiro para calcular o fatorial.  
    Returns:
        O fatorial do número.
        Se o número for negativo, retorna uma mensagem indicando que o fatorial não é definido.
        Se o número for 0 ou 1, retorna 1, pois o fatorial de 0 e 1 é 1.
    """

    # Verifica se o número é um inteiro
    if not isinstance(numero, int):
        raise ValueError ("Por favor, insira um número inteiro.")
    
    # Verifica se o número é negativo, pois fatorial não é definido para negativos
    if numero < 0:
        raise ValueError ("Fatorial não é definido para números negativos")
    
    # Verifica se o número é 0 ou 1, pois o fatorial de 0 e 1 é 1
    if numero == 0 or numero == 1:
        return 1
    
    # Inicializa o fatorial como 1
    resultado = 1

    # Calcula o fatorial multiplicando os números de 1 até o número
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Função para calcular o coeficiente binomial (n choose k)
def binomio(a, b):
    """
    Calcula o coeficiente binomial (n choose k) usando a fórmula n! / (k! * (n - k)!).
    Args:
        a: O número inteiro n.
        b: O número inteiro k.
    Returns:
        O coeficiente binomial, que é o número de maneiras de escolher k elementos de um conjunto de n elementos.
    """
    
    # Verifica se b é maior que a, pois não é possível escolher mais elementos do que existem
    if b > a:
        raise ValueError("O valor de k não pode ser maior que n.")
    
    # Calcula o coeficiente binomial usando a função fatorial
    return fatorial(a) / (fatorial(b) * fatorial((a - b)))

# Chama a função binomio e imprime o resultado
print(f"O coeficiente binomial de {n} e {k} é: {binomio(n, k)}")