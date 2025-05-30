import re

def eh_palindromo(texto: str) -> str:
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Parâmetros:
    - texto (str): A palavra ou frase a ser verificada.

    Retorna:
    - str: "Sim" se for palíndromo, "Não" caso contrário.
    """
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto.lower())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


# Exemplo:
entrada = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(entrada)
print(f"É palíndromo? {resultado}")
