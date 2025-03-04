import numpy as np
import matplotlib.pyplot as plt

def mostra_sinal(sinal):

	return 0

def aplica_FFT_em_sinal(sinal):
	return 0

def main():
	t = np.array([0, 1, 2, 3])  
	T = 2

	resultado = np.exp(-t/T)  # Aplica e^(-t/T) a cada elemento
	print(resultado)

	for k in resultado:
		print(k)

	return 0

if __name__ == "__main__":
	main()