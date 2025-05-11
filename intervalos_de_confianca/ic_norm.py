from scipy.stats import norm
import numpy as np

# Função lambda para calcular o erro médio (erro padrão da média)
erro_medio = lambda dp, n: dp / np.sqrt(n)

# Função para calcular o intervalo de confiança da média com dados amostrais
def IC_Normal(dados, conf=0.95):
    # Define distribuição normal padrão (média 0, desvio padrão 1)
    Normal = norm(loc=0, scale=1)

    # Calcula o valor crítico z para o nível de confiança
    z = Normal.ppf(1- (1 - conf)/ 2)

    # Calcula o erro padrão da média usando desvio padrão amostral
    em = erro_medio(np.std(dados, ddof=1), len(dados))

    # Calcula os limites inferior e superior do IC
    ic = [np.mean(dados) - z * em, np.mean(dados) + z * em]

    # Retorna string formatada com o resultado
    saida = f"""
    ======= Intervalo de confiança para média ======
    
    - Nível de confiança: {conf*100}%
    
    - IC = {ic}
    """
    return saida

# Função para calcular IC da média quando só se tem os parâmetros (n, média e dp)
def IC_normal_(n, media, dp, conf=0.95):
    # Define distribuição normal padrão
    Normal = norm(loc=0, scale=1)

    # Calcula o valor crítico z
    z = Normal.ppf(1 - (1 - conf)/ 2)

    # Calcula o erro padrão da média
    em = erro_medio(dp, n)

    # Calcula os limites do IC
    ic = [media - z * em, media + z * em]

    # Retorna string formatada com o resultado
    saida = f"""
    ======= Intervalo de confiança para média ======
    
    - Nível de confiança: {conf*100}%
    
    - IC = {ic}
    """
    return saida