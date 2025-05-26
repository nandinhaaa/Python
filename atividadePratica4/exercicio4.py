# Exercício 4: Verificação de Par ou Ímpar
# Regras:
# - Continuar pedindo números até que o usuário digite 'fim'.
# - Informar se o número é par ou ímpar.
# - Se não for um número inteiro, informar o erro e continuar.
# - Ao final, mostrar a quantidade total de números pares e ímpares inseridos.

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: Entrada não é um número inteiro.")

print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
