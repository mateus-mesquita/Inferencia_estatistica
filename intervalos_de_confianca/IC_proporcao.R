# Intervalo de confiança para proporção com base nos dados
IC.proporcao <- function(dados, conf = 0.95){
  # Estimação de p (assume dados 0/1)
  p_ = sum(dados) / length(dados)
  
  q = qnorm(1 - (1 - conf)/2)  # Quantil da normal padrão para o nível de confiança
  
  ic = c(
    "Limite inferior" = p_ - q * sqrt(p_ * (1 - p_) / length(dados)),  # IC inferior
    "Limite superior" = p_ + q * sqrt(p_ * (1 - p_) / length(dados))   # IC superior
  )
  return(ic)
}

# Versão que usa p e n diretamente
IC.proporcao_ <- function(p_, n, conf = 0.95){
  q = qnorm(1 - (1 - conf)/2)
  
  ic = c(
    "Limite inferior" = p_ - q * sqrt(p_ * (1 - p_) / n),
    "Limite superior" = p_ + q * sqrt(p_ * (1 - p_) / n)
  )
  return(ic)
}