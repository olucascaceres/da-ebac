import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega os dados do arquivo CSV para um DataFrame
df = pd.read_csv('gasolina.csv')

# Cria o gráfico utilizando o Seaborn
sns.lineplot(x='dia', y='venda', data=df)

# Adiciona rótulos aos eixos x e y
plt.xlabel('Dia')
plt.ylabel('Preço')

# Salva o gráfico em um arquivo PNG
plt.savefig('gasolina.png')

# Exibe o gráfico na tela
plt.show()