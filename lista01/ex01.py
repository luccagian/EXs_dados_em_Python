"""
1. Construa uma base de dados numérica simulada de dimensão + ou – 15. Calcular as medidas elencadas acima, assim como fazer os gráficos citados. 

• Media. 
• Mediana. 
• Variância (Populacional e amostral). 
• Desvio Padrão (Populacional e amostral). 
• Coeficiente de variação (Populacional e amostral). 
• Quartis. 
• Histograma. 
• Box plot. 

"""

dados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

import numpy as np
import matplotlib.pyplot as plt

#média

media = np.mean(dados)
print("media:", media)

#mediana

mediana = np.median(dados)
print("mediana:", mediana)

#variâcia populacional

variancia_pop = np.var(dados)
print("variancia populacional: ", variancia_pop)

#variância amostral

variancia_am = np.var(dados, ddof = 1)
print("variancia amostral:", variancia_am)

#desvio padrão populacional

desvio_padrao_pop = np.std(dados)
print("desvio padrao populacional:", desvio_padrao_pop)

#desvio padrão amostral

desvio_padrao_am = np.std(dados,ddof = 1)
print("desvio padrao amostral:", desvio_padrao_am)

#coeficinete de variação pop.

cv_pop = desvio_padrao_pop / media
print("coeficinete de variação popuacional:", cv_pop)

#coeficinete de variação amostral

cv_am = desvio_padrao_am / media
print("coeficinete de variação amostral:", cv_am)

#quartis
#minimo

minimo = np.min(dados)
print("minimo:", minimo)

#Q1

q1 = np.quantile(dados,0.25)
print("primeiro quartil:", q1)

#mediana
print("mediana:", mediana)

#Q3

q3 = np.quantile(dados,0.75)
print("terceiro quartil:", q3)

#maximo

maximo = np.max(dados)
print("maximo:", maximo)

print("\nGráficos:\n")

#histograma

plt.hist(dados, bins = 5,color = 'lightblue', edgecolor='black', rwidth = 0.8)
plt.title("Histograma")
plt.xlabel("Dados")
plt.ylabel("Frequência")
plt.show()

#boxplot

plt.boxplot(x=dados, patch_artist=True, boxprops=dict(facecolor='lightblue') )
plt.title('Boxplot')
plt.xlabel('Dados')
plt.show()
