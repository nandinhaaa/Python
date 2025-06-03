import pandas as pd

# Caminho relativo ao arquivo CSV (está na mesma pasta do script)
caminho = "atividadePratica07/log_treinamento.csv"

# Leitura do CSV
df = pd.read_csv(caminho)

# Cálculos
media = df["tempo_execucao"].mean()
desvio_padrao = df["tempo_execucao"].std()

# Exibição
print(f"Média do tempo de execução: {media:.2f} segundos")
print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
