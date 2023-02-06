#Função faixa de idade
def faixaIdade(idade):
  if idade <= 12:
    return 'crieança'
  elif idade <= 18:
    return 'adolecente'
  elif idade <= 80:
    return 'adulto'
  else:
    return 'idoso'

#Função soma quadrado
def somaQuad(n1, n2):
  return n1**2 + n2**2