

def fizzbuzz(n):
    """
    Função que implementa o FizzBuzz.
    Args:
        n: Um número inteiro positivo.
    Returns:
        Uma lista de strings representando os números de 1 a n, substituindo múltiplos de 3 por "Fizz",
        múltiplos de 5 por "Buzz" e múltiplos de ambos por "FizzBuzz".
    """
    if n % 3 == 0 and not n % 5 == 0:
        return "Fizz"
    elif n % 5 == 0 and not n % 3 == 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return n