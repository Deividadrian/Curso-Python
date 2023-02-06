#Listas
nomes = ['Deivid', 'Vitor', 'Luz']
idades = [10,20,15]

#Tupas = As tuplas não poden ser mudadas seus valores apos serem decleradas 
sexo = ('M','F','O')

#Dicionários
cadastro = {'nomes': nomes,'idades': idades, 'cidades': ['A',"B",'C']}

for nome in nomes:
  print(nome)

for idade in idades:
  if idade%2==0: print(idade)

for i in range(0,5):
  print(i)

#==============================

i = 0
idade = idades[i]
while idade <= 10:
  print(idade)
  i += 1
  idade = idades[1]