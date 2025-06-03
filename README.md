# 📘 Atividades Práticas – Python

Repositório com os exercícios desenvolvidos em Python conforme os enunciados das Atividades Práticas 03, 04 e 05.

## 📑 Sumário

- [Atividade Prática 03](#atividade-pratica-03)  
  - [Exercício 1 - Classificador de Idade](#exercicio-1-classificador-idade)  
  - [Exercício 2 - Calculadora de IMC](#exercicio-2-calculadora-imc)  
  - [Exercício 3 - Conversor de Temperatura](#exercicio-3-conversor-temperatura)  
  - [Exercício 4 - Verificador de Ano Bissexto](#exercicio-4-verificador-ano-bissexto)  

- [Atividade Prática 04](#atividade-pratica-04)  
  - [Exercício 1 - Calculadora de Operações Básicas](#exercicio-1-calculadora-operacoes-basicas)  
  - [Exercício 2 - Registro de Notas da Turma](#exercicio-2-registro-notas-turma)  
  - [Exercício 3 - Verificador de Senha Forte](#exercicio-3-verificador-senha-forte)  
  - [Exercício 4 - Classificador Par ou Ímpar](#exercicio-4-classificador-par-ou-impar)  

- [Atividade Prática 05](#atividade-pratica-05)  
  - [Exercício 1 - Calculadora de Gorjeta](#exercicio-1-calculadora-gorjeta)  
  - [Exercício 2 - Verificador de Palíndromo](#exercicio-2-verificador-palindromo)  
  - [Exercício 3 - Idade em Dias](#exercicio-3-idade-em-dias)  

- [Atividade Prática 07](#atividade-pratica-07)  
  - [Exercício 1 - Cálculo de Média e Desvio em Log de Treinamento](#exercicio-1)  
  - [Exercício 2 - Escrita de Dados em CSV com Informações de Pessoas](#exercicio-2)  
  - [Exercício 3 - Leitura e Exibição de Dados de Arquivo CSV](#exercicio-3)  
  - [Exercício 4 - Leitura e Escrita de Dados em Arquivo JSON](#exercicio-4)  

---

## 🔷 Atividade Prática 03

<a id="exercicio-1-classificador-idade"></a>
### 🔹 Exercício 1 - Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:

- Criança (0–12 anos)  
- Adolescente (13–17 anos)  
- Adulto (18–59 anos)  
- Idoso (60 anos ou mais)

![Exercício 1](https://github.com/user-attachments/assets/afcf84a7-196b-4411-82b6-1a8440a88e9f)

---

<a id="exercicio-2-calculadora-imc"></a>
### 🔹 Exercício 2 - Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.  
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão:

- IMC < 18.5: "Abaixo do peso"  
- IMC < 25: "Peso normal"  
- IMC < 30: "Sobrepeso"  
- Para os demais: "Obeso"

![Exercício 2](https://github.com/user-attachments/assets/1d6fc408-82b7-4c99-8496-8aabd261ed28)

---

<a id="exercicio-3-conversor-temperatura"></a>
### 🔹 Exercício 3 - Conversor de Temperatura

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.  
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

![Exercício 3](https://github.com/user-attachments/assets/9a6c1dab-7900-4239-b1ce-65a7270c2541)

---

<a id="exercicio-4-verificador-ano-bissexto"></a>
### 🔹 Exercício 4 - Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.  
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

![Exercício 4](https://github.com/user-attachments/assets/704d5726-215b-4734-928c-401d6fd36f58)

---

## 🔷 Atividade Prática 04

<a id="exercicio-1-calculadora-operacoes-basicas"></a>
### ✅ Exercício 1 - Calculadora de Operações Básicas

Solicita dois números e uma operação (+, -, *, /).  
Repete até que uma operação válida seja feita.  
Trata erros como entrada inválida, divisão por zero e operação inválida.  
Mostra o resultado e encerra.

![Exercício 1](https://github.com/user-attachments/assets/963f9496-2374-4117-9921-6b86d751a594)

---

<a id="exercicio-2-registro-notas-turma"></a>
### 📝 Exercício 2 - Registro de Notas da Turma

Continua solicitando notas até o professor digitar 'fim'.  
Aceita apenas notas entre 0 e 10.  
Ignora inválidas.  
Ao final, exibe a média da turma.

![Exercício 2](https://github.com/user-attachments/assets/f87c6d95-442c-4cb5-84a5-2cea4adf9cd7)

---

<a id="exercicio-3-verificador-senha-forte"></a>
### 🔐 Exercício 3 - Verificador de Senha Forte

Senha forte: no mínimo 8 caracteres e pelo menos um número.  
Continua pedindo senha até ser forte ou o usuário digitar 'sair'.

![Exercício 3](https://github.com/user-attachments/assets/fdeebf6c-b059-490f-a0f5-0c157d3e5f2e)

---

<a id="exercicio-4-classificador-par-ou-impar"></a>
### 🔢 Exercício 4 - Classificador Par ou Impar

Solicita números inteiros até digitar 'fim'.  
Informa se é par ou ímpar.  
Se não for número, informa o erro.  
Ao final, exibe a quantidade total de pares e ímpares inseridos.

![Exercício 4](https://github.com/user-attachments/assets/2a5b1e7b-bffe-49bb-8de6-075698453c2a)

---

## 🔷 Atividade Prática 05

<a id="exercicio-1-calculadora-gorjeta"></a>
### 💰 Exercício 1 - Calculadora de Gorjeta

Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.

- Solicita o valor da conta e a porcentagem da gorjeta.  
- Calcula e exibe o valor da gorjeta a ser deixada.

![Exercício 1](https://github.com/user-attachments/assets/8d6b82b2-1326-4a80-8793-eb87b9ec78e4)

---

<a id="exercicio-2-verificador-palindromo"></a>
### 🔄 Exercício 2 - Verificador de Palíndromo

Crie uma função que verifique se uma palavra ou frase é um palíndromo, desconsiderando espaços e pontuações.

- Retorna `"Sim"` se for palíndromo e `"Não"` caso contrário.

![Exercício 2](https://github.com/user-attachments/assets/0acad7b9-9a60-41dd-bb75-d190c6477127)

---

<a id="exercicio-3-idade-em-dias"></a>
### 📅 Exercício 3 - Idade em Dias

Crie uma função que calcule a idade de uma pessoa em dias com base no ano de nascimento.

- Solicita o ano de nascimento.  
- Retorna a idade aproximada em dias (sem considerar anos bissextos).

![Exercício 3](https://github.com/user-attachments/assets/29d17571-1364-402d-a869-08472d31bf70)

---

## 🔷 Atividade Prática 07

<a id="exercicio-1"></a>
### 📊 Exercício 1 - Cálculo de Média e Desvio em Log de Treinamento

Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning.  
Calcule a média e o desvio padrão do tempo de execução constantes.

![Exercício 1](https://github.com/user-attachments/assets/803933df-a853-4b1f-a8e5-263f2f477191)

---

<a id="exercicio-2"></a>
### 📝 Exercício 2 - Escrita de Dados em CSV com Informações de Pessoas

Crie um script em Python que escreva dados em um arquivo CSV.  
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

![Exercício 2](https://github.com/user-attachments/assets/ce63e606-ba42-4b31-862d-120f75bf2e17)  
![Exercício 2](https://github.com/user-attachments/assets/deb6a58f-45e5-417e-8bd6-bc2527cad0f9)

---

<a id="exercicio-3"></a>
### 📂 Exercício 3 - Leitura e Exibição de Dados de Arquivo CSV

Crie um script em Python que leia um arquivo CSV e exiba os dados na tela.  
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

![Exercício 3](https://github.com/user-attachments/assets/63929ae1-14e9-4d13-b556-1ba9cc9b0af2)

---

<a id="exercicio-4"></a>
### 📄 Exercício 4 - Leitura e Escrita de Dados em Arquivo JSON

Crie um script em Python que leia e escreva dados em um arquivo JSON.  
O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

![Exercício 4](https://github.com/user-attachments/assets/33b921bb-48b5-4814-8e44-181dadc99192)  
![Exercício 4](https://github.com/user-attachments/assets/c8b7617c-dbe1-4b41-bb4e-f5532dac73d3)
