# Programa completo do Jogo NIM - Exercício 5 da Lista 5 de Python


# Função que define a jogada do computador
def computador_escolhe_jogada(n, m):

    """
    Função que determina a jogada do computador.
    O computador tenta deixar um múltiplo de (m+1) para o usuário.
    Se não for possível, ele remove o máximo permitido (m).
    Args:
        n (int): Número de peças restantes no tabuleiro.
        m (int): Número máximo de peças que podem ser removidas em uma jogada.
    Returns:
        int: Número de peças que o computador decide remover.
    """

    # Computador tenta deixar um múltiplo de (m+1) para o usuário
    for jogada in range(1, m + 1):

        # Verifica se a jogada deixa um múltiplo de (m+1)
        if (n - jogada) % (m + 1) == 0:
            return jogada
        
    # Se não for possível, remove o máximo permitido
    return min(n, m)

# Função que define a jogada do usuário
def usuario_escolhe_jogada(n, m):

    """
    Função que solicita a jogada do usuário.
    O usuário deve escolher um número válido de peças para remover.
    Args:
        n (int): Número de peças restantes no tabuleiro.
        m (int): Número máximo de peças que podem ser removidas em uma jogada.
    Returns:
        int: Número de peças que o usuário decide remover.
    """

    # Solicita a jogada do usuário até que seja válida
    while True:
        jogada = int(input(f"Quantas peças você vai tirar (1 a {m})? "))

        # Verifica se a jogada é válida
        if 1 <= jogada <= m and jogada <= n:
            return jogada
        
        # Jogada inválida, solicita novamente
        print("Jogada inválida! Tente novamente.")

# Função que gerencia uma partida do jogo
def partida():

    """
    Função que gerencia uma partida do jogo NIM.
    Define quem começa, alterna as jogadas entre o usuário e o computador,
    e determina o vencedor.
    Args:
        None
    Returns:
        None
    """

    # Solicita o número de peças e o limite por jogada  
    n = int(input("\nQuantas peças? "))
    m = int(input("\nLimite de peças por jogada? "))
    
    # Define quem começa
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        jogador = "usuario"
    else:
        print("\nComputador começa!\n")
        jogador = "computador"
    
    # Loop principal do jogo
    while n > 0:
        if jogador == "usuario":
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"\nVocê tirou {jogada} peça(s).\n")
            jogador = "computador"
        else:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"\nO computador tirou {jogada} peça(s).\n")
            jogador = "usuario"
        
        # Verifica se o jogo acabou
        if n == 0:
            if jogador == "usuario":
                print("\nO computador ganhou!\n")
            else:
                print("\nVocê ganhou!\n")
        else:
            print(f"\nRestam {n} peça(s) no tabuleiro.\n")


# Função que gerencia um campeonato de 3 partidas
def campeonato():

    """
    Função que gerencia um campeonato de 3 partidas do jogo NIM.
    Mantém o placar e anuncia o vencedor do campeonato.
    Args:
        None
    Returns:
        None
    """

    # Inicializa o placar
    vitorias_usuario = 0
    vitorias_computador = 0
    
    # Loop para 3 partidas
    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****\n")
        vencedor = partida()
        if vencedor == "usuario":
            vitorias_usuario += 1
        else:
            vitorias_computador += 1
    
    # Anuncia o vencedor do campeonato
    print("\n**** Fim do campeonato! ****")
    print(f"Placar final: Você {vitorias_usuario} x {vitorias_computador} Computador") 

    # Declara o campeão
    if vitorias_usuario > vitorias_computador:
        print("\n****Você é o campeão!****\n")
    else:
        print("\n****O computador é o campeão!****\n")

# Função principal que inicia o jogo
def main():

    """
    Função principal que inicia o jogo NIM.
    Permite ao usuário escolher entre uma partida única ou um campeonato.
    Args:
        None
    Returns:
        None
    """

    # Menu inicial
    print("Bem-vindo ao jogo do NIM!")
    print("Escolha:")
    print("\n1 - para jogar uma partida isolada")
    print("\n2 - para jogar um campeonato")

    # Solicita a escolha do usuário
    escolha = int(input("\nSua escolha: "))
    
    # Inicia o jogo conforme a escolha do usuário
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    elif escolha == 2:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()
    else:
        print("\nOpção inválida! Tente novamente.\n")

# Executa o jogo
if __name__ == "__main__":
    main()