import json

# Dados para salvar no arquivo JSON
pessoa = {
    "nome": "Maria Fernanda",
    "idade": 23,
    "cidade": "Minas Gerais"
}

arquivo_json = "atividadePratica07/pessoa.json"

# Escrever os dados no arquivo JSON
with open(arquivo_json, 'w', encoding='utf-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

print(f"Dados escritos em {arquivo_json}")

# Ler os dados do arquivo JSON
with open(arquivo_json, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

print("Dados lidos do arquivo JSON:")
print(dados)
