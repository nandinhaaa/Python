from datetime import date

def idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade de uma pessoa em dias com base no ano de nascimento.

    Parâmetros:
    - ano_nascimento (int): O ano em que a pessoa nasceu.

    Retorna:
    - int: Idade aproximada em dias.
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365  # Aproximação sem considerar anos bissextos

# Exemplo:
try:
    ano = int(input("Digite o ano de nascimento: "))
    dias = idade_em_dias(ano)
    print(f"Idade aproximada em dias: {dias}")
except ValueError:
    print("Entrada inválida. Por favor, digite um ano válido.")
