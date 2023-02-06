import pandas as pd

df = pd.DataFrame({'nome':['Deivid', 'Vitor', 'Luz'],
                  'idade': [10,20,15]})

print(df)
print(df.nome[1])
print(df['idade'][1])
print(df.loc[1,'idade'])
print(df.idade.min())
print(df.idade.max())

#O pandas tem muitas funções 'Sempre pesquise no Google'