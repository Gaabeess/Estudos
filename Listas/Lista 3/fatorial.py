# calculadora de n!

# Solicita ao usuário um número inteiro para calcular o fatorial
# O número deve ser um inteiro não negativo
# Se o usuário inserir um número inválido, o programa deve solicitar novamente
number = int(input("Digite um número para calcular o fatorial: "))

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
        return "Por favor, insira um número inteiro."
    
    # Verifica se o número é negativo, pois fatorial não é definido para negativos
    if numero < 0:
        return "Fatorial não é definido para números negativos"
    
    # Verifica se o número é 0 ou 1, pois o fatorial de 0 e 1 é 1
    if numero == 0 or numero == 1:
        return 1
    
    # Inicializa o fatorial como 1
    resultado = 1

    # Calcula o fatorial multiplicando os números de 1 até o número
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

# Chama a função e imprime o resultado
print(f"{fatorial(number)}")