import pandas as pd # type: ignore

caminho_arquivo = '/home/digo/Downloads/nomes_pesos.csv'

df = pd.read_csv(caminho_arquivo)

list_costumers= []

for index, row in df.iterrows():
    #print(f'(NULL,"{row['Nome']}", {row['Peso (kg)']})')
    list_costumers.append(f'(NULL,"{row['Nome']}", {row['Peso (kg)']})')


insert_DB= ','.join(list_costumers)