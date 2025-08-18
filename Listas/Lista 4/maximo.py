# Programa para encontrar o maior valor entre dois números

# Solicita ao usuário dois valores inteiros
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

# Função para retornar o maior valor entre dois números
def maximo(a, b):
    """
    Retorna o maior valor entre dois números.
    Args:
        a: Primeiro número.
        b: Segundo número.
    Returns:
        O maior número entre a e b.
    """
    # Compara os dois números e retorna o maior
    if a > b:
        return a
    else:
        return b

# Chama a função maximo e imprime o resultado    
print(maximo(valor1, valor2))  # Exemplo de uso da função