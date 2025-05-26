# Exercício 3: Verificação de Senha Forte
# Regras:
# - Senha forte: pelo menos 8 caracteres e pelo menos um número.
# - Continuar pedindo senha até que uma válida seja inserida ou o usuário digite 'sair'.

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrado.")
        break

    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte registrada com sucesso.")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e conter um número.")
