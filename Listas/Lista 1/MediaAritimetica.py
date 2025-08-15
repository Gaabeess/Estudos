nota1 = float(input("Digite a primeira nota: "))    # input do usuário
nota2 = float(input("Digite a segunda nota: "))     # input do usuário
nota3 = float(input("Digite a terceira nota: "))    # input do usuário
nota4 = float(input("Digite a quarta nota: "))      # input do usuário

media = (nota1 + nota2 + nota3 + nota4) / 4  # cálculo da média
media = round(media, 2)  # arredondamento para duas casas decimais

print(f"A média aritmética é {media}")  # exibição do resultado