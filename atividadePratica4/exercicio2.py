# Exercício 2: Registro de Notas da Turma
# Regras:
# - Continuar solicitando notas até que o professor digite 'fim'.
# - Aceitar apenas notas entre 0 e 10.
# - Ignorar notas inválidas e continuar solicitando.
# - Ao final, mostrar a média da turma.

notas = []

while True:
    entrada = input("Digite uma nota entre 0 e 10 ou 'fim' para encerrar e retornar a media da turma: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Deve estar entre 0 e 10.")
    except ValueError:
        print("Entrada inválida.")

if notas:
    media = sum(notas) / len(notas)
    print("Média da turma:", round(media, 2))
else:
    print("Nenhuma nota válida foi inserida.")
