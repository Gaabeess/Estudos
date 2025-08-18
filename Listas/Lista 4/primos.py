
# Encontra o maior número primo menor ou igual a n
def maior_primo(n):

    """
    Encontra o maior número primo menor ou igual a n.
    Args:
        n: Um número inteiro positivo.
    Returns:
        O maior número primo menor ou igual a n. Se não houver primos, retorna None.
    """

    # Verifica se n é menor que 2, pois não há primos menores que 2
    if n < 2:
        return None  # Não há primos menores que 2

    # Função auxiliar para verificar se um número é primo
    def is_primo(num):

        """Verifica se um número é primo."""
        
        # Números menores que 2 não são primos
        if num < 2:
            return False
        
        # Verifica divisibilidade de 2 até a raiz quadrada de num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
            
        return True

    # Itera de n até 2 para encontrar o maior primo
    for i in range(n, 1, -1):
        if is_primo(i):
            return i

    return None  # Caso não haja primos encontrados

print(maior_primo(int(input("Digite um número inteiro positivo: "))))