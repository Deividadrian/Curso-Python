import pandas as pd

df = pd.DataFrame({'nome':['Deivid', 'Vitor', 'Luz'],
                  'idade': [10,20,15]})

df.loc[0,'nome'] = 'Adrian'
df['sexo'] = ['M','F','O']
df = df.append({'nome':'Diney','idade': 12, 'sexo': 'M'}, ignore_index=True)
print(df)
