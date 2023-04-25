import pandas as pd
import numpy as np

# iremos supor que, na pasta na qual se encontra o código também se encontra um arquivo csv contendo valores
# de diversos ativos da bolsa, incluindo o ^BVSP (no caso do mercado brasileiro). A formatacao suposta sera
# um df com colunas nomeadas de acordo com o nome do ativo. Importando esse arquivo:
data = pd.read_csv("data_stocks.csv")

# logaritmando os valores no dado
log_data = np.log(data/data.shift())

# Encontrando o índice da coluna do Ibovespa
market_col = log_data.columns.get_loc("^BVSP")

#Funcao para o calculo do beta
def beta_calc(data_frame):
    betas = []
    market_var = data_frame['^BVSP'].var()
    cov_data = data_frame.cov()
    for col_index in range(0,len(data_frame.columns)):
        betas = betas + [cov_data.iloc[col_index, market_col]/market_var]
    return betas

#calculando o beta sobre os dados logaritimados
print(*beta_calc(log_data), sep = ", ")
