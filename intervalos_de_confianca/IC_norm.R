# Criando função de intervalo de confiança para distribuição normal

erro.medio = function(dp,n) dp/sqrt(n)

IC.Norm <- function(dados, conf = 0.95){
  # alfa/2
  alfa = qnorm(1-(1-conf)/2)
  erro.amostral = alfa*erro.medio(sd(dados),length(dados))
  
  ic = c(
    "Limite inferior" = mean(dados) - erro.amostral,
    "Limite Superior" = mean(dados) + erro.amostral
  )
  return(ic)
}

# Para casos em que não possui amostra
IC.Norm2 <- function(media,dp,n,conf = 0.95){
  alfa = qnorm(1-(1-conf)/2)
  erro.amostral = alfa*erro.medio(dp,n)
  
  ic = c(
    "Limite inferior" = media - erro.amostral,
    "Limite Superior" = media + erro.amostral
  )
  return(ic)
}

