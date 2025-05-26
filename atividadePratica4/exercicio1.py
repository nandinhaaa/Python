# Exercício 1: Calculadora
# Regras:
# - Solicitar ao usuário dois números e a operação.
# - Repetir até que uma operação válida seja concluída.
# - Tratar os seguintes erros:
#   - Entrada não numérica.
#   - Divisão por zero.
#   - Operação inválida.
# - Mostrar o resultado e encerrar.

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: Divisão por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            continue

        print("Resultado:", resultado)
        break
    except ValueError:
        print("Erro: Entrada não numérica.")
