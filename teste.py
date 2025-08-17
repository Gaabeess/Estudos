# nota = 6
# resultado = (nota >= 3.0 and nota < 5.0)
# print("Recuperação", resultado)


# ano = 2023
# bissexto = (ano % 4 == 0)
# print("Ano bissexto", bissexto)

def value_of_card(card):
    
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    if card == 'J' or 'Q' or 'K':
        return 10
        
    if card == 'A':
        return 1

    else:
        return int(card)
        
print(value_of_card('A'))  # Example usage, should return 1