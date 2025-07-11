import numpy as np
import matplotlib.pyplot as plt
import my_image_lib_0_7 as mil
import pywt
from copy import deepcopy

#inicialização dos dados
with open("first_parameters.txt", "r") as valores_iniciais: #recebe os primeiros dados
	S_0 = float(valores_iniciais.readline().split()[2])
	omega = float(valores_iniciais.readline().split()[2])
	T = float(valores_iniciais.readline().split()[2])
	dt = float(valores_iniciais.readline().split()[2])
	n_pontos = int(valores_iniciais.readline().split()[2])

def le_arquivo_sinal(caminho_arq, isImage = False):
	if isImage:
		sinal = mil.Image(f"{caminho_arq}")
		return sinal

	else:
		with open(f"{caminho_arq}", "r") as arquivo_sinal:
			n_pontos, dt = arquivo_sinal.readline().split()
			n_pontos = int(n_pontos)
			dt = float(dt)
			sinal = np.array([complex(i) for i in arquivo_sinal.readline().split()])
			tempos = np.array([float(i) for i in arquivo_sinal.readline().split()])
		return sinal, tempos, dt

def salva_sinal(sinal, tempos, nome_sinal):
	with open(f"Sinais/{nome_sinal}.txt", "w") as arquivo_sinal:
		n_pontos = str(len(sinal))
		dt = tempos[1] - tempos[0]
		arquivo_sinal.write(str(n_pontos) + " " + str(dt) + "\n")
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
		ft = np.fft.fft(sinal)
		ft = np.fft.fftshift(ft)
		return ft

def cria_array_frequencias(tempos):
	n_pontos = len(tempos)
	dt = tempos[1] - tempos[0]
	frequencia = np.fft.fftfreq(n_pontos, dt)
	frequencia = np.fft.fftshift(frequencia)
	return frequencia

def mostra_FT(ft, frequencia = None, componente = None, ppm = False, isImage = False):
	if isImage:
		imagem = ft.representacao()
		mil.print_grayscale_image(imagem)
	else:
		if ppm:
			freq_ref = 127.74 #Para um campo de 3T (em MHz)
			frequencia = (frequencia - freq_ref) / freq_ref 

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

		if ppm:
			plt.xlabel('Deslocamento Químico (ppm)')
		else:
			plt.xlabel('Frequência (Hz)')
			
		plt.ylabel('FT do Sinal')
		plt.title('Espectro de Frequência do Sinal')
		plt.legend()
		plt.grid()
		plt.show()

def mostra_residuo(ft_original, frequencia_original, ft_filtrado, componente = "m", ppm = False):
	ft_plota = ft_original - ft_filtrado

	if ppm:
		freq_ref = 127.74 #Para um campo de 3T (em MHz)
		frequencia_original = (frequencia_original - freq_ref) / freq_ref 

	assert componente in "rim", "Uso errado do parâmetro \'componente\'.\n Use \'r\' para mostrar a parte real do sinal.\n Use \'i\' para mostrar a parte imaginária do sinal.\n Use \'ri\' para mostrar a parte real e a parte imaginária do sinal.\n Use \'m\' para mostrar o módulo do sinal." 
	if componente == "r": 
		plt.plot(frequencia_original, ft_plota.real, label="Parte real do resíduo")
	elif componente == "i":
		plt.plot(frequencia_original, ft_plota.imag, label="Parte imaginária do resíduo")
	elif componente == "ri":
		plt.plot(frequencia_original, ft_plota.real, label="Parte real do resíduo")
		plt.plot(frequencia_original, ft_plota.imag, label="Parte imaginária do resíduo")
	elif componente == "m":
		plt.plot(frequencia_original, np.abs(ft_plota), label="Módulo do resíduo")
	
	if ppm:
		plt.xlabel('Deslocamento Químico (ppm)')
	else:
		plt.xlabel('Frequência (Hz)')

	plt.ylabel('ΔFT')
	plt.title('Resíduo Espectral')
	plt.legend()
	plt.grid()
	plt.show()
	
def aplica_DTWT_em_sinal(sinal, familia, nivel, isImage = False):
	if isImage:
		pass
	else:
		coeficientes = pywt.wavedec(sinal, wavelet=familia, level=nivel)
		return coeficientes

def mostra_WT(coeficientes, dt, isImage = False):
	freq_max = (1 / dt) / 2
	level = len(coeficientes) - 1

	if isImage:
		pass
	else:
		for i, c in enumerate(coeficientes):
			plt.subplot(len(coeficientes), 1, len(coeficientes) - i)
			plt.plot(c, label=f'Nível {len(coeficientes) - i}' if i > 0 else 'Aproximação')

			if i == 0:
				f_low = 0
			else:	
				f_low = freq_max / 2**(level - i + 1)

			f_high = freq_max / 2**(level - i)
			faixa = f"{f_low:.1f}–{f_high:.1f} Hz"
			
			plt.title(faixa)
			plt.legend()
			plt.grid(True)

		plt.tight_layout()
		plt.show()

def aplica_IDTWT_em_sinal(coeficientes, familia, isImage):
	if isImage:
		pass
	else:
		sinal_rec = pywt.waverec(coeficientes, wavelet=familia)
		return sinal_rec

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
	sinal, tempos, dt = le_arquivo_sinal("Sinais/SinalMNR_gauss005.txt")
	mostra_sinal(sinal, tempos, "r")

	sinal2, tempos2, dt2 = le_arquivo_sinal("Sinais/SinalMNR_gauss005_sym2_filter1111.txt")
	mostra_sinal(sinal2, tempos2, "r")

	ft = aplica_FFT_em_sinal(sinal)
	ft2 = aplica_FFT_em_sinal(sinal2)
	frequencia = cria_array_frequencias(tempos)
	frequencia2 = cria_array_frequencias(tempos2)

	mostra_FT(ft, frequencia, "m")
	mostra_FT(ft2, frequencia2, "m")
	mostra_residuo(ft, frequencia, ft2)

	return 0

if __name__ == "__main__":
	main()