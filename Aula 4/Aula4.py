import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selenium import train_test_split

tabela = pd.read_csv(r"C:\Users\Thigas\OneDrive\Documentos\Aula 4\advertising.csv")


# --------------- jupyter
# #criar tabela 
# sns.heatmap(tabela.corr())

# # exibe 
# plt.show
# -------------- jupyter


#machine learn
y = tabela['Vendas']
x = tablea[['TV', 'Radio', 'Jornal']]