# operacoes.py
def dividir(numerador, denominador):
    """
    Realiza a divisão de dois números.
    Levanta ZeroDivisionError se o denominador for zero.
    """
    if denominador == 0:
        raise ZeroDivisionError("O denominador não pode ser zero.")
    return numerador / denominador
