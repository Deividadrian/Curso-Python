#A soma dos numeros pares de 0 a 100
soma = 0
for i in range(0,101):
  if i%2==0:
    soma += i

print(soma)

# Esse mesmo código em uma unica linha
print(sum([i if i%2==0 else 0 for i in range(0,101)]))