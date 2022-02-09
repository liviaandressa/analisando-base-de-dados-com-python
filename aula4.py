#Tratando e compilando as bases de dados 

import os

lista_arquivos = os.listdir("C:\\Users\\Lívia\Desktop\\curso-python-hashtag\\Vendas")

for arquivo in lista_arquivos:

    if "Vendas" in arquivo:
        print(f"C:\\Users\\Lívia\Desktop\\curso-python-hashtag\\Vendas\\{arquivo}")