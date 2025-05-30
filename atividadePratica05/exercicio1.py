def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.

    Parâmetros:
    - valor_conta (float): O valor total da conta.
    - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
    - float: O valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso:
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
resultado = calcular_gorjeta(valor, porcentagem)
print(f"Gorjeta: R${resultado:.2f}")
