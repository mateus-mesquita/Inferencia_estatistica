from scipy.stats import norm            # Importa a normal padrão
import numpy as np                      # Biblioteca para cálculo numérico

# Função para intervalo de confiança da proporção a partir dos dados brutos
def IC_proporcao(dados, conf=0.95):
    normal = norm(loc=0, scale=1)       # Define a normal padrão

    p_ = sum(dados)/len(dados)          # Estimação pontual da proporção (média dos dados 0/1)
    z = normal.ppf(1 - (1 - conf)/2)    # Quantil da normal padrão para o nível de confiança

    ic = {
        "Limite inferior": p_ - z*np.sqrt(p_*(1 - p_)/len(dados)),  # Fórmula do IC inferior
        "Limite superior": p_ + z*np.sqrt(p_*(1 - p_)/len(dados))   # Fórmula do IC superior
    }
    return ic

# Função alternativa que recebe p e n diretamente (sem os dados)
def IC_proporcao_(p_, n, conf=0.95):
    normal = norm(loc=0, scale=1)
    z = normal.ppf(1 - (1 - conf)/2)

    ic = {
        "Limite inferior": p_ - z*np.sqrt(p_*(1 - p_)/n),
        "Limite superior": p_ + z*np.sqrt(p_*(1 - p_)/n)
    }
    return ic
