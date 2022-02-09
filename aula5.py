#Tratar / compilar as bases de dados

import os
import pandas as pd

tabela_total = pd.DataFrame()
lista_arquivos = os.listdir("C:\\Users\\Lívia\Desktop\\curso-python-hashtag\\Vendas")

for arquivo in lista_arquivos:

    tabela = pd.read_csv(f"C:\\Users\\Lívia\Desktop\\curso-python-hashtag\\Vendas\\{arquivo}")
    tabela = tabela_total.append(tabela)
    
print(tabela_total)
#display(tabela_total) usa o diisplay caso esteja codando no google colab, é melhor para vizualizar lá