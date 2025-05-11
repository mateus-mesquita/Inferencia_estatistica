from scipy.stats import t
from intervalos_de_confianca.ic_norm import erro_medio
import numpy as np

# Função para calcular o intervalo de confiança usando a distribuição t de Student
def IC_T(dados, conf=0.95):
    # Cria o objeto t com graus de liberdade baseados no tamanho da amostra
    t_dist = t(len(dados) - 1)

    # Calcula o valor crítico t para o nível de confiança
    t_alfa = t_dist.ppf(1-(1 - conf)/ 2)

    # Calcula o erro médio (erro padrão da média) usando o desvio padrão amostral
    em = erro_medio(np.std(dados, ddof=1), len(dados))

    # Calcula os limites inferior e superior do IC
    ic = [np.mean(dados) - t_alfa * em, np.mean(dados) + t_alfa * em]

    return ic

# Função para calcular o intervalo de confiança usando a distribuição t quando não há amostra
def IC_T_(media, n, dp, conf=0.95):
    # Cria o objeto t com graus de liberdade baseados no tamanho da amostra
    t_dist = t(n - 1)

    # Calcula o valor crítico t
    t_alfa = t_dist.ppf(1-(1 - conf)/ 2)

    # Calcula o erro médio (erro padrão da média)
    em = erro_medio(dp, n)

    # Calcula os limites do IC
    ic = [media - t_alfa * em, media + t_alfa * em]

    return ic