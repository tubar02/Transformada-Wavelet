import numpy as np
import matplotlib.pyplot as plt
import pywt
import useful_lib as ul

sinal, tempos = ul.le_arquivo_sinal("Sinais/omega100.txt")

ul.mostra_sinal(sinal, tempos, "r")

coeficientes = pywt.wavedec(sinal, wavelet='haar', level=4)

for i, c in enumerate(coeficientes):
    plt.subplot(len(coeficientes), 1, len(coeficientes) - i)
    plt.plot(c, label=f'Nível {len(coeficientes) - i}' if i > 0 else 'Aproximação')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()