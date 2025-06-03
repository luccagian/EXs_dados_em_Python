"""

2. Aplicar a técnica de regressão linear em uma base de dados real de tamanho maior que 100 (base quantitativa, pode ser a mesma base de dados da avaliação continuada 01).

Usar um pacote pronto do python para aplicar a regressão linear na base de dados. Fazer os gráficos para a base de dados e para a regressão linear.

"""

# importar os dados

import pandas as pd
from google.colab import drive
drive.mount('/content/gdrive')

url = 'gdrive/My Drive/Colab Notebooks/laptop_prices.csv'

df = pd.read_csv(url)

prices = df['Price_euros'].values.reshape(-1, 1)
peso = df['Weight'].values

# criar modelo

model = LinearRegression()
model.fit(prices, peso)

a = model.intercept_
b = model.coef_[0]

print(f"\nEquação de regressão: Y = a * x + b\na={a}\nb={b}\n")

plt.scatter(prices, peso, color='blue', label='Dados')
plt.plot(prices, model.predict(prices), color='red', label='Linha de Regressão')
plt.xlabel('Preços Notebook(EUR)')
plt.ylabel('Peso')
plt.title('Preços vs Peso')
plt.legend()
plt.show()
