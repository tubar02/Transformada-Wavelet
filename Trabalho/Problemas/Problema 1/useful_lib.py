import numpy as np
import matplotlib.pyplot as plt

#inicialização dos dados
n_pontos = 2 ** 11 
dt = 5 * 10 ** (-4)
with open("first_parameters.txt", "r") as valores_iniciais: #recebe os primeiros dados
	S_0 = float(valores_iniciais.readline().split()[2])
	omega = float(valores_iniciais.readline().split()[2])
	T = float(valores_iniciais.readline().split()[2])

def cria_array_tempos(Dt = dt, n_Pontos = n_pontos):
	array_tempos = np.linspace(0, (n_Pontos - 1) * Dt, n_Pontos) #cria o vetor com os tempos igualmente espaçados
	return array_tempos

def simula_sinal(array_tempos, omega_0 = omega, T_0 = T):
	sinal = np.exp(-array_tempos/T_0) * np.exp(1j * omega_0 * array_tempos)
	return sinal

def mostra_sinal(tempo, sinal, separa_componentes = True):
	if separa_componentes:
		plt.plot(tempo, sinal.real, label="Parte real")
		plt.plot(tempo, sinal.imag, label="Parte imaginária")
	else:
		plt.plot(tempo, np.abs(sinal), label="Módulo")
		
	plt.xlabel("Tempo (s)")
	plt.ylabel("Sinal(t)")
	plt.title("Sinal Simulado")
	plt.legend()
	plt.grid()
	plt.show()

def aplica_FFT_em_sinal(sinal):
	return 0

def main():
	tempo = cria_array_tempos(0.0005, 2048)
	sinal = simula_sinal(tempo, 50)

	mostra_sinal(tempo, sinal)
	mostra_sinal(tempo, sinal, False)

	return 0

if __name__ == "__main__":
	main()