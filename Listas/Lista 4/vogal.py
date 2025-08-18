

def vogal(letra):
    """Verifica se uma letra é uma vogal.

    Args:
        letra (str): Uma única letra a ser verificada.

    Returns:
        bool: True se a letra for uma vogal, False caso contrário.
    """
    vogais = 'aeiouAEIOU'
    return letra in vogais
print(vogal(input("Digite uma letra: ")))  # Exemplo de uso da função
