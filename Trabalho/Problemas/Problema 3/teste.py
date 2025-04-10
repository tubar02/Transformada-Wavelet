import numpy as np
import matplotlib.pyplot as plt

# Gerando valores aleatórios de ruído seguindo uma distribuição normal
mu = 0       # Média do ruído
sigma = 1    # Desvio padrão do ruído
n_pontos = 10000  # Número de amostras

ruido = np.random.normal(mu, sigma, n_pontos)  # Gerando os valores

plt.plot(ruido, linestyle='-', marker='.', markersize=3, color='b')
plt.xlabel("Índice")
plt.ylabel("Amplitude do Ruído")
plt.title("Ruído Gaussiano")
plt.grid()
plt.show()