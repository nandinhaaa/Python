import pandas as pd

# Dados das pessoas
pessoas = [
    {"Nome": "Nanda", "Idade": 23, "Cidade": "Minas Gerais"},
    {"Nome": "Brian", "Idade": 25, "Cidade": "São Paulo"},
    {"Nome": "Carla", "Idade": 22, "Cidade": "Belo Horizonte"},
]

# Criar um DataFrame a partir da lista de dicionários
df = pd.DataFrame(pessoas)

# Salvar em arquivo CSV
df.to_csv("pessoas.csv", index=False, encoding='utf-8')

print("Arquivo pessoas.csv criado com sucesso!")
