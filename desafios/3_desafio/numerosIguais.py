# Calculadoras/numerosIguais.py

# Solicita ao usuário que insira o número a ser verificado
number = input("Digite o numero a ser verificado: ")

# Função para dividir o número em suas ordens
def dividir_em_ordens(numero):

    """
    Divide um número inteiro em suas ordens (unidades, dezenas, centenas, etc.).

    Args:
        numero: O número inteiro a ser dividido.

    Returns:
        Uma lista contendo as ordens do número, da unidade para a maior ordem.
    """

    # Inicializa uma lista para armazenar as ordens do número
    # A lista será usada para armazenar as unidades, dezenas, centenas, etc.
    ordens = []
   
    # Inicializa a variável 'i' para multiplicar as ordens
    # A variável 'i' será usada para multiplicar a ordem atual
    # Isso garante que as ordens sejam armazenadas corretamente
    i = 1

    # Enquanto o número for maior que zero, divide-o em ordens
    # A cada iteração, extrai a ordem atual e adiciona à lista de ordens
    # O número é dividido por 10 para remover a ordem já processada
    # A variável 'i' é usada para multiplicar a ordem atual
    # Isso garante que as ordens sejam armazenadas corretamente
    while numero > 0:
        ordem = numero % 10
        ordens.append(ordem)
        numero //= 10
        i *= 10

    # Inverte a lista de ordens para que as unidades fiquem no início
    # Isso é necessário para que a soma seja feita da unidade para a maior ordem
    ordens.reverse()
    return ordens[::-1]

# Função para verificar se os números são iguais
def numerosIguais(array):

    """
    Verifica se há números iguais em uma lista.
    Args:
        array: Lista de números inteiros a serem verificados.

    Returns:
        Uma string indicando se há números iguais ou não.
    """
    # Inicializa o índice para percorrer a lista
    i = 0

    # Percorre a lista de números para verificar se há números iguais
    while i < len(array) - 1:
        if array[i] == array[i + 1]:
            return "sim"
        i += 1
    return "não"

# Exibe o resultado da verificação de números iguais
print(numerosIguais(dividir_em_ordens(int(number))))
    