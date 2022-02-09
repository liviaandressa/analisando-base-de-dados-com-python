#calculando produto mais vendido 

import os
import pandas as pd

tabela_total = pd.DataFrame()
lista_arquivos = os.listdir("C:\\Users\\Lívia\Desktop\\curso-python-hashtag\\Vendas")

for arquivo in lista_arquivos:

    tabela = pd.read_csv(f"C:\\Users\\Lívia\Desktop\\curso-python-hashtag\\Vendas\\{arquivo}")
    tabela = tabela_total.append(tabela)
    
print(tabela_total)

#seleciona somente as colunas desejadas - tabela_produtos = tabela_produtos[['Quantidade Vendida', 'Preco Unitario']]
#Coloca a coluna ordenada - .sort_values(by="Quantidade Vendida", ascending=False) 
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida', 'Preco Unitario']].sort_values(by="Quantidade Vendida", ascending=False) 

print(tabela_produtos)
#display(tabela_produtos)

'''---------------------------------------------------------------'''

#calculando produto que mais faturou

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_faturamento = tabela_total.groupby('Produto').sum()
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by="Faturamento", ascending=False) 
print(tabela_faturamento)


'''---------------------------------------------------------------'''

#calculando loja que mais faturou

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']].sort_values(by="Faturamento", ascending=False)
print(tabela_lojas)


'''---------------------------------------------------------------'''

#criando gráfico de faturamento de cada loja

import plotly.express as px

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()
