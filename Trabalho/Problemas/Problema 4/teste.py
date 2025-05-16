import numpy as np
import matplotlib.pyplot as plt
import pywt
import useful_lib as ul

w = pywt.Wavelet("db4")

sinal, tempos = ul.le_arquivo_sinal("Sinais/Exemplo.txt")

coeficientes = pywt.wavedec(sinal, wavelet='db4', level=4)

max_len = max(len(c) for c in coeficientes)
coef_matrix = np.array([np.pad(c, (0, max_len - len(c))) for c in coeficientes])
coef_matrix = np.abs(coef_matrix)

plt.imshow(coef_matrix, aspect='auto', cmap='viridis', origin='lower')
plt.colorbar(label='Amplitude')
plt.xlabel('Posição no sinal')
plt.ylabel('Níveis da DTWT')
plt.title('Coeficientes da Transformada Wavelet (DTWT)')
plt.savefig("Del/wavelet.png")

#ul.mostra_sinal(sinal, tempos, "r")