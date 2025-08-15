# Calculadora que soma os valores de um numero

# solicita ao usuário que insira os números a serem somados
number = input("Digite o numero a ser somado: ")

# Função para dividir o número em suas ordens
# A função recebe um número inteiro e divide-o em suas ordens
# Exemplo: 1234 será dividido em [1, 2, 3, 4]
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

# Função para somar os valores das ordens
# Verifica se todos os valores são números inteiros
def soma (args):

    """
    Soma os valores de uma lista de números inteiros.

    Args:
        args: Lista de números inteiros a serem somados.

    Raises:
        ValueError: Se a lista de números estiver vazia ou se algum valor não for um número inteiro.

    Returns:
        A soma dos números inteiros na lista.
    """
    # Verifica se a lista de números não está vazia
    if not args:

         # Se a lista estiver vazia, lança um erro
        raise ValueError("A lista de números não pode estar vazia.")
    
    # Verifica se todos os valores na lista são números inteiros
    for i in args:
        
        # Retorna a soma dos valores
        # Converte os valores para inteiros e retorna a soma
        return sum(int(i) for i in args)

# Exibe o resultado da soma dos números
print(f"A soma dos números é: {soma(dividir_em_ordens(int(number)))}")


