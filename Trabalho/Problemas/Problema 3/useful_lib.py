import numpy as np
import matplotlib.pyplot as plt
import my_image_lib_0_6 as mil
from copy import deepcopy

#inicialização dos dados
with open("first_parameters.txt", "r") as valores_iniciais: #recebe os primeiros dados
	S_0 = float(valores_iniciais.readline().split()[2])
	omega = float(valores_iniciais.readline().split()[2])
	T = float(valores_iniciais.readline().split()[2])
	dt = float(valores_iniciais.readline().split()[2])
	n_pontos = int(valores_iniciais.readline().split()[2])

def le_arquivo_sinal(nome_arq, isImage = False):
	if isImage:
		sinal = mil.Image(f"Imagens/{nome_arq}")
		return sinal

	else:
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

def mostra_sinal(sinal, tempo = None, componente = None, isImage = False):
	if isImage:
		mil.print_grayscale_image(sinal)
	else:
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

def aplica_FFT_em_sinal(sinal, isImage = False):
	if isImage:
		imagem = mil.Fourier_Image(sinal)
		imagem.shift()
		return imagem
	else:
		return np.fft.fft(sinal)

def cria_array_frequencias(tempos):
	n_pontos = len(tempos)
	dt = tempos[1] - tempos[0]
	return np.fft.fftfreq(n_pontos, dt)

def mostra_FT(ft, frequencia = None, componente = None, isImage = False):
	if isImage:
		imagem = ft.representacao()
		mil.print_grayscale_image(imagem)
	else:
		ft, frequencia = np.fft.fftshift(ft), np.fft.fftshift(frequencia) #realiza o shift
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

def adiciona_ruido_gauss(_sinal, mu, sigma, isImage = False, outputpath = None):
	if isImage:
		ruido = mil.Ruido(_sinal)
		ruido.gauss(mu, sigma)
		corrompido = _sinal.corrompe(outputpath, ruido)
		return corrompido
	else:
		sinal = deepcopy(_sinal)

		ruido1 = np.random.normal(mu, sigma, len(sinal))
		ruido2 = np.random.normal(mu, sigma, len(sinal)) * 1j
		return sinal + ruido1 + ruido2

def main():
	sinal = le_arquivo_sinal("gourds.pgm", True)

	mostra_sinal(sinal, isImage=True)

	sinal_FT = aplica_FFT_em_sinal(sinal, True)
	
	mostra_FT(sinal_FT, isImage=True)
	
	mu, sigma = 0, 25
	sinal_ruidoso = adiciona_ruido_gauss(sinal, mu, sigma, True, f"Imagens\\gourdsGauss.pgm")

	mostra_sinal(sinal_ruidoso, isImage=True)

	fft_sinal_ruidoso = aplica_FFT_em_sinal(sinal_ruidoso, True)

	mostra_FT(fft_sinal_ruidoso, isImage=True)

	return 0

if __name__ == "__main__":
	main()