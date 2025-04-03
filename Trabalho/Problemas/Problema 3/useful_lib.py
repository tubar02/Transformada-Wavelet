import numpy as np
import matplotlib.pyplot as plt

#inicialização dos dados
with open("first_parameters.txt", "r") as valores_iniciais: #recebe os primeiros dados
	S_0 = float(valores_iniciais.readline().split()[2])
	omega = float(valores_iniciais.readline().split()[2])
	T = float(valores_iniciais.readline().split()[2])
	dt = float(valores_iniciais.readline().split()[2])
	n_pontos = int(valores_iniciais.readline().split()[2])

def le_arquivo_sinal(nome_arq):
	with open(f"Sinais/{nome_arq}.txt", "r") as arquivo_sinal:
		n_pontos = arquivo_sinal.readline()
		sinal = np.array([complex(i) for i in arquivo_sinal.readline().split()])
		tempos = np.array([float(i) for i in arquivo_sinal.readline().split()])
	return sinal, tempos

def salva_sinal(sinal, tempos, nome_sinal):
	with open(f"Sinais\{nome_sinal}.txt", "w") as arquivo_sinal:
		arquivo_sinal.write(str(len(sinal)) + "\n")
		arquivo_sinal.write(" ".join([str(i) for i in sinal]) + "\n")
		arquivo_sinal.write(" ".join([str(i) for i in tempos]) + "\n")

def cria_array_tempos(Dt = dt, n_Pontos = n_pontos):
	array_tempos = np.linspace(0, (n_Pontos - 1) * Dt, n_Pontos) #cria o vetor com os tempos igualmente espaçados
	return array_tempos

def simula_sinal(array_tempos, omega_0 = omega, T_0 = T, S_0 = S_0):
	sinal = S_0 * np.exp(-array_tempos/T_0) * np.exp(1j * omega_0 * array_tempos) #cria o vetor com o sinal simulado
	return sinal

def mostra_sinal(tempo, sinal, componente):
	assert componente in "rim", "Uso errado do parâmetro \'componente\'.\n Use \'r\' para mostrar a parte real do sinal.\n Use \'i\' para mostrar a parte imaginária do sinal.\n Use \'ri\' para mostrar a parte real e a parte imaginária do sinal.\n Use \'m\' para mostrar o módulo do sinal." 
	if componente == "r": 
		plt.plot(tempo, sinal.real, label="Parte real")
	elif componente == "i":
		plt.plot(tempo, sinal.imag, label="Parte imaginária")
	elif componente == "ri":
		plt.plot(tempo, sinal.real, label="Parte real")
		plt.plot(tempo, sinal.imag, label="Parte imaginária")
	elif componente == "m":
		plt.plot(tempo, np.abs(sinal), label="Módulo")
		
	plt.xlabel("Tempo (s)")
	plt.ylabel("Sinal(t)")
	plt.title("Sinal Simulado")
	plt.legend()
	plt.grid()
	plt.show()

def aplica_FFT_em_sinal(sinal):
	return np.fft.fft(sinal)

def cria_array_frequencias(tempos):
	n_pontos = len(tempos)
	dt = tempos[1] - tempos[0]
	return np.fft.fftfreq(n_pontos, dt)

def mostra_FT(frequencia, ft, componente):
	assert componente in "rim", "Uso errado do parâmetro \'componente\'.\n Use \'r\' para mostrar a parte real do sinal.\n Use \'i\' para mostrar a parte imaginária do sinal.\n Use \'ri\' para mostrar a parte real e a parte imaginária do sinal.\n Use \'m\' para mostrar o módulo do sinal." 
	if componente == "r": 
		plt.plot(frequencia, ft.real, label="Parte real")
	elif componente == "i":
		plt.plot(frequencia, ft.imag, label="Parte imaginária")
	elif componente == "ri":
		plt.plot(frequencia, ft.real, label="Parte real")
		plt.plot(frequencia, ft.imag, label="Parte imaginária")
	elif componente == "m":
		plt.plot(frequencia, np.abs(ft), label="Módulo")

	plt.xlabel('Frequência (Hz)')
	plt.ylabel('FT do Sinal')
	plt.title('Espectro de Frequência do Sinal')
	plt.legend()
	plt.grid()
	plt.show()

def main():
	tempo = cria_array_tempos(0.0005, 2048)
	sinal = simula_sinal(tempo, 628)

	mostra_sinal(tempo, sinal)

	fft_sinal = np.fft.fft(sinal)
	frequencias = np.fft.fftfreq(n_pontos, dt)

	plt.plot(frequencias, np.abs(fft_sinal))
	plt.xlabel('Frequência (Hz)')
	plt.ylabel('Magnitude')
	plt.title('Espectro de Frequência do Sinal')
	plt.grid()
	plt.show()

	return 0

if __name__ == "__main__":
	main()