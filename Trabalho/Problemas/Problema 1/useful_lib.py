import numpy as np
import matplotlib.pyplot as plt

#inicialização dos dados
n_pontos = 2 ** 11 
dt = 5 * 10 ** (-4)
with open("first_parameters.txt", "r") as valores_iniciais: #recebe os primeiros dados
	S_0 = valores_iniciais.readline().split()[2]
	omega = valores_iniciais.readline().split()[2]
	T = valores_iniciais.readline().split()[2]

def calcula_sinal(Dt = dt, omega_0 = omega, T_0 = T, n_Pontos = n_pontos):
	array_tempos = np.linspace(0, (n_Pontos - 1) * Dt, n_Pontos) #cria o vetor com os tempos igualmente espaçados
	array_sinal = np.exp(-array_tempos/T) * np.exp(1j * omega * array_tempos)

def mostra_sinal(sinal):

	return 0

def aplica_FFT_em_sinal(sinal):
	return 0

def main():
	array, step = np.linspace(0, 2047 * 0.5, 2048, retstep=True)
	print(array)
	print("Espaçamento entre os valores:", step)

	return 0

if __name__ == "__main__":
	main()