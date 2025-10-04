# ==========================================
# Imports (só vão funcionar se instalados)
# ==========================================
import matplotlib.pyplot as plt    # Gráficos e visualização de dados
import numpy as np                 # Manipulação de arrays e matrizes
import pandas as pd                # Manipulação e análise de dados em tabelas (DataFrames)
import seaborn as sns              # Visualização estatística com gráficos mais bonitos e fáceis
import scipy                       # Funções científicas avançadas (ex: integração, otimização)
import sklearn                     # Aprendizado de máquina (scikit-learn)
import tensorflow as tf            # Framework para deep learning
import torch                       # PyTorch, outra biblioteca para deep learning
import requests                    # Requisições HTTP para APIs e web scraping
import flask                       # Framework web leve para desenvolvimento de APIs e aplicações web
import tkinter as tk               # Interfaces gráficas desktop simples

# ==========================================
# Exemplo 1 - Cálculo de IMC
# ==========================================
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc:.2f}")

# ==========================================
# Exemplo 2 - Maioridade
# ==========================================
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("É maior de idade e pode dirigir")
else:
    print("É menor de idade e NÃO pode dirigir")
print("FIM")

# ==========================================
# Exemplo 3 - Comparação entre dois números
# ==========================================
a = int(input("Digite o 1º número: "))
b = int(input("Digite o 2º número: "))

if a > b:
    print("a,b")
elif a < b:
    print("b,a")
else:
    print("empate")

# ==========================================
# Exemplo 4 - Condições com cores
# ==========================================
cor_copo = input("Diga a cor do copo: ").lower()
if cor_copo == "amarelo":
    print("O copo é amarelo")
elif cor_copo == "verde":
    print("O copo é verde")
elif cor_copo == "azul":
    print("O copo é azul")
elif cor_copo == "vermelho":
    print("O copo é vermelho")
elif cor_copo == "rosa":
    print("O copo é rosa")
else:
    print("Não existe copo ou ele não é dessas cores")

# ==========================================
# Exemplo 5 - Lista de cores
# ==========================================
cores_prato = ["roxo", "cinza", "preto", "rosa"]
escolha_cor = input("Escolha uma cor: ").lower()
if escolha_cor in cores_prato:
    print(f"O prato da cor {escolha_cor} existe")
else:
    print(f"O prato da cor {escolha_cor} não existe ou foi digitado incorretamente")

# ==========================================
# Exemplo 6 - Orientação sexual e gênero
# ==========================================
orisex = ["homossexual", "hetero", "lesbica", "bissexual", "pansexual"]
genero = ["homem", "mulher", "não binário"]

atalhos_orisex = {
    "gay": "homossexual",
    "pan": "pansexual",
    "bi": "bissexual"
}

atalhos_genero = {
    "nb": "não binário",
    "m": "mulher",
    "h": "homem"
}

diga_orisex = input("Qual é a sua orientação sexual? ").lower().strip()
diga_genero = input("Qual é o seu gênero? ").lower().strip()

if diga_orisex in atalhos_orisex:
    diga_orisex = atalhos_orisex[diga_orisex]

if diga_genero in atalhos_genero:
    diga_genero = atalhos_genero[diga_genero]

if diga_orisex in orisex and diga_genero in genero:
    print(f"Você é {diga_orisex} e {diga_genero}")
elif diga_orisex in orisex and diga_genero not in genero:
    print(f"Você é {diga_orisex} mas não existe gênero {diga_genero}")
elif diga_orisex not in orisex and diga_genero in genero:
    print(f"Não existe {diga_orisex} mas você é {diga_genero}")
else:
    print(f"Não existe orientação sexual {diga_orisex} nem gênero {diga_genero} - TENTE NOVAMENTE")

# ==========================================
# Exemplo 7 - Lista de nomes
# ==========================================
Nome = ["Duda", "Kristen"]

while True:
    nome_digitado = input("Qual é o seu nome? ").strip()
    if nome_digitado in Nome:
        print(f"Olá {nome_digitado}, Seja bem-vindo(a) à nossa empresa!")
        break
    else:
        print("Nome não reconhecido, tente de novo.")

# ==========================================
# Exemplo 8 - Nome + Empresa
# ==========================================
nome = ["Ana", "Maria", "Pedro", "João", "Duda", "Kristen"]
empresa = ["McDonalds", "Outback", "TOTVS", "FMU"]

while True:
    diga_nome = input("Fala seu nome: ").strip()
    diga_empresa = input("Digite o nome da empresa: ").strip()

    if diga_nome in nome and diga_empresa in empresa:
        print(f"Oi {diga_nome}. Seja bem-vindo(a) a {diga_empresa} \n")
        break
    else:
        print("Nome ou empresa não reconhecido, tente novamente")

# ==========================================
# Exemplo 9 - Triângulo Retângulo
# ==========================================
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Triângulo retângulo POSITIVO")
else:
    print("Triângulo retângulo NEGATIVO")

# ==========================================
# Exemplo 10 - Quadrados até digitar 0
# ==========================================
n = int(input("Digite um número (0 para parar): "))
while n != 0:
    print(n*n)
    try:
        n = int(input("Digite outro número (0 para parar): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# ==========================================
# Exemplo 11 - Divisão manual
# =====================
