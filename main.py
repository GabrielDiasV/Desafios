import numpy as np
from scipy.stats import norm

#criacao da funcao para precificacao de opcoes
def BlackScholes (S, K, T, sigma, r, type):
    "calculo do valor teórico de opções put ou call via modelo de Black-Scholes"
    price = 0
    d1 = (np.log(S/K) + (r + sigma ** 2 / 2) * T)/(sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "CALL":
            price = S * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "PUT":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - S * norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Por favor, confira os parâmetros inseridos")

#leitura de variaveis
type = input("Insira o tipo de opcao (CALL ou PUT): ")
S = float(input("Insira o preco atual da acao objeto da opcao: "))
K = float(input("Insira o preco de exercicio da opcao: "))
T = float(input("Insira o prazo de vencimento (em anos) da opcao: "))
sigma = float(input("Insira a volatilidade do preco da acao objeto: "))
r = float(input("Insira a taxa livre de risco anual em regime de capitalizacao continua: "))

print(f"Valor da opcao: {round(BlackScholes(S, K, T, sigma, r, type = type.upper()), 3)}")

