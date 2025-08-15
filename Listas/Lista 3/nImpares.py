# Exibição de números ímpares

numbers = int(input("Digite um numero inteiro positivo: "))

# Função para exibir números ímpares
def numeros_impares(numbers):

    """
    Exibe números ímpares de 1 até o número fornecido.
    Args:
        numbers: O número inteiro positivo até onde os ímpares serão exibidos.
    Returns:
        Nenhum retorno, apenas imprime os números ímpares.
        Se o número for negativo ou zero, solicita um número positivo.
    """
    
    # Verifica se o número é positivo
    # Se for positivo, imprime os números ímpares de 1 até o número fornecido
    # Se for negativo ou zero, solicita um número positivo
    if numbers > 0:

        # Inicializa o contador e o primeiro número ímpar
        count = 0  
        num = 1    

        # Enquanto o contador for menor que o número de ímpares a serem impressos
        while count < numbers:
            print(num)
            num += 2  # Próximo ímpar
            count += 1 
    
    # Se o número for negativo ou zero, solicita um número positivo
    else:
        print("Por favor, insira um número inteiro positivo.")
        return
    
# Chama a função e imprime os números ímpares
numeros_impares(int(numbers))
# A função imprime N numeros ímpares começando de 1
# Exemplo: se o usuário inserir 5, a saída será 1, 3, 5, 7, 9