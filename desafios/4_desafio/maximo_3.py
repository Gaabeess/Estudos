
def maximo(a, b, c):
    """
    Retorna o maior valor entre três números.
    Args:
        a: Primeiro número.
        b: Segundo número.
        c: Terceiro número.
    Returns:
        O maior número entre a, b e c.
    """
    # Compara os três números e retorna o maior
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c