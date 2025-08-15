# Verifica se um número é primo

# Solicita ao usuário um número inteiro para verificar se é primo
# O número deve ser um inteiro positivo maior que 1
# Se o usuário inserir um número inválido, o programa deve solicitar novamente
number = int(input("Digite um número para verificar se é primo: "))


# Função para verificar se um número é primo
# A função recebe um número inteiro e verifica se ele é primo
# Um número é considerado primo se for maior que 1 e não for divisível por nenhum número além de 1 e ele mesmo
# Exemplo: 2, 3, 5, 7 são primos; 4, 6, 8, 9 não são primos
def numero_primo(numero):
    """
    Verifica se um número é primo.
    Args:
        numero: O número inteiro a ser verificado.

    Returns:
        Uma string indicando se o número é primo ou não.
    """
    # Verifica se o número é menor que 2, pois números menores que 2 não são primos
    if numero < 2:
        return "Não é primo"
    # Percorre os números de 2 até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        # Verifica se o número é divisível por algum desses números
        if numero % i == 0:
            return "Não é primo"
    # Se não for divisível por nenhum, é primo
    return "É primo"

# Chama a função e imprime o resultado
print(numero_primo(number))