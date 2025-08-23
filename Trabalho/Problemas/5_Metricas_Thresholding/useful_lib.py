import numpy as np
import matplotlib.pyplot as plt
import my_image_lib_0_8 as mil
import pywt
from math import sqrt
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
		return sinal, None, None

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
	
def aplica_DTWT_em_sinal(sinal, familia, nivel = None, isImage = False):
	if isImage:
		imagem = mil.Wavelet_Image(sinal, familia, nivel)
		return imagem

	else:
		coeficientes = pywt.wavedec(sinal, wavelet=familia, level=nivel)
		return coeficientes

def mostra_WT(coeficientes, dt = None, componente = "m", isImage = False, level = None):
	if isImage:
		coeficientes.representar_nivel(level)

	else:
		freq_max = (1 / dt) / 2
		level = len(coeficientes) - 1
		for i, c in enumerate(coeficientes):
			assert componente in "rim", "Uso errado do parâmetro \'componente\'.\n Use \'r\' para mostrar a parte real do sinal.\n Use \'i\' para mostrar a parte imaginária do sinal.\n Use \'ri\' para mostrar a parte real e a parte imaginária do sinal.\n Use \'m\' para mostrar o módulo do sinal." 

			plt.subplot(len(coeficientes), 1, len(coeficientes) - i)

			if componente == "r": 
				plt.plot(c.real, label=f'Nível {len(coeficientes) - i} - Real' if i > 0 else 'Aproximação')
			elif componente == "i":
				plt.plot(c.imag, label=f'Nível {len(coeficientes) - i} - Imag' if i > 0 else 'Aproximação')
			elif componente == "ri":
				plt.plot(c.real, label=f'Nível {len(coeficientes) - i} - Real' if i > 0 else 'Aproximação')
				plt.plot(c.imag, label=f'Nível {len(coeficientes) - i} - Imag' if i > 0 else 'Aproximação')
			elif componente == "m":
				plt.plot(np.abs(c), label=f'Nível {len(coeficientes) - i} - Mód' if i > 0 else 'Aproximação')

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

def aplica_IDTWT_em_sinal(coeficientes, familia = None, isImage = False):
	if isImage:
		imagem_rec = coeficientes.reconstruir()
		return imagem_rec

	else:
		sinal_rec = pywt.waverec(coeficientes, wavelet=familia)
		return sinal_rec

def potencia_media(sinal, isImage = False):
	"""
    Potência média do sinal (1D ou 2D, real ou complexo).
    Usa |x|^2 para sinais complexos, como em RM.
    """
	if not isImage:
		potencia = np.abs(sinal) ** 2
	else:
		potencia = np.abs(np.asarray(sinal.pixel())) ** 2
	return potencia.mean()

def converte_snr(snr, saida = "db"):
	if saida == "db":
		snr_db = 10 * np.log10(snr)
		return snr_db
	elif saida == "lin":
		snr_lin = 10 ** (snr / 10)
		return snr_lin

def sigma_gauss(componente_ruido_gauss = None, sinal = None, snr_db = None, isImage = False):
	if snr_db != None:
		sigma = sqrt(potencia_media(sinal, isImage) / converte_snr(snr_db, "lin"))
	else:
		sigma = sqrt(potencia_media(componente_ruido_gauss))
	return sigma

def sigma_rayleigh(mod_ruido_gauss_complex = None, sinal = None, snr_db = None, isImage = False):
	if snr_db != None:
		if not isImage:
			sigma = sqrt(potencia_media(sinal, isImage) / (2 *converte_snr(snr_db, "lin")))
		else:
			sigma = sigma_gauss(mod_ruido_gauss_complex, sinal, snr_db, isImage)
	else:
		sigma = sqrt(potencia_media(mod_ruido_gauss_complex) / 2)
	return sigma

def sigma_rician(mod_degradado_gauss, original):
	potencia_sinal = potencia_media(original)
	potencia_degrado = potencia_media(mod_degradado_gauss)
	sigma = sqrt((potencia_degrado - potencia_sinal) / 2)
	return sigma

def adiciona_ruido(sinal, noise_type = "gaussian", mode = "sigma", param = 0.1, isImage = False, outputpath = None):
	"""
	noise_type: "gaussian", "salt_pepper", "poisson", etc.
	mode: "sigma" ou "snr"
	param: sigma (se mode="sigma") ou snr_db (se mode="snr")
	"""
		
	if mode == "snr":
		sigma = sigma_rayleigh(snr_db = param, sinal = sinal, isImage = isImage)
	else:
		sigma = param

	if noise_type == "gaussian":
		return adiciona_ruido_gauss(sinal, 0, sigma, isImage, outputpath)

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

def snr(original, degradado = None, ruido = None, retorno = "db", isImage = False):
	"""
	SNR entre um original e um degradado (ou original e ruído).
	- original: np.ndarray 1D/2D (real ou complexo)
	- degradado: original + ruido (se não fornecer 'ruido')
	- ruido: opcional; se dado, ignora 'degradado'
	- retorno: "db" (default), "linear" ou "sigma"
	"""
	if not isImage:
		if ruido is None:
			assert degradado is not None, "Passe 'degradado' ou 'ruido'."
			ruido_gauss = degradado - original
		else:
			ruido_gauss = ruido

		p_sig = potencia_media(original)
		p_rui = potencia_media(ruido_gauss)
	else:
		if ruido is None:
			assert degradado is not None, "Passe 'degradado' ou 'ruido'."
			ruido_gauss = np.asarray(degradado.pixel()) - np.asarray(original.pixel())
		else:
			ruido_gauss = ruido

		p_sig = potencia_media(original, isImage)
		p_rui = potencia_media(ruido_gauss)

	snr_lin = p_sig / p_rui
	if retorno == "db":
		return converte_snr(snr_lin)
	elif retorno == "sigma":
		sigma = sigma_gauss(ruido_gauss.real)
		return sigma
	return snr_lin

def estima_snr_wavelet(sinal_ruidoso_coeficientes, original, ponto):
	sigma = np.median(np.abs(sinal_ruidoso_coeficientes[-1][ponto::])) / (1.17741)
	snr_lin = potencia_media(original) / (2 * sigma ** 2)
	snr_db = converte_snr(snr_lin)
	return snr_db

def visu_shrink(coeficiente, sigma): 
	limiar = sigma * sqrt(2 * np.log(coeficiente.size)) 
	return limiar

def hard_thresholding(coeficientes, sigma, isImage = False, outputpath = None, familia = "db2"): 
	if not isImage:
		novos_coefs = [coeficientes[0]]
		for lista in coeficientes[1::]: 
			limiar = visu_shrink(lista, sigma)
			lista = np.asarray([i if np.abs(i) >= limiar else 0 for i in lista]) 
			novos_coefs.append(lista) 
	else:
		coeficientes_wt = coeficientes.coef
		novos_coefs = [coeficientes_wt[0]]
		for detalhes in coeficientes_wt[1::]:
			novos_detalhes = []
			for detalhe in detalhes:
				limiar = visu_shrink(detalhe, sigma)
				detalhe = np.asarray([[i if np.abs(i) >= limiar else 0 for i in linha] for linha in detalhe])
				novos_detalhes.append(detalhe)
			novos_coefs.append(novos_detalhes)
		novos_coefs = tuple(novos_coefs)
		imagem_reconstruida = pywt.waverec2(novos_coefs, familia)
		imagem = mil.pgm_from_matrix(outputpath, imagem_reconstruida)
		novos_coefs = aplica_DTWT_em_sinal(imagem, coeficientes.wavelet, coeficientes.level, True)
	return novos_coefs

def main():
	sinal, _, _ = le_arquivo_sinal("Imagens//MRI.pgm", True)
	mostra_sinal(sinal, isImage = True)
	ruidoso = adiciona_ruido(sinal, mode = "snr", param = 30, isImage = True, outputpath = "Imagens//gourds_gauss.pgm")
	mostra_sinal(ruidoso, isImage = True)

	snr_db = snr(sinal, ruidoso, isImage = True)
	print(f"snr original = {snr_db}")

	transformado = aplica_DTWT_em_sinal(ruidoso, "coif2", 2, True)
	mostra_WT(transformado, isImage = True, level = 1)

	sigma = snr(sinal, ruidoso, retorno = "sigma", isImage = True)
	transf_n_linear = hard_thresholding(transformado, sigma, True, "Imagens//MRI_hard_visu.pgm", "coif2") 
	mostra_WT(transf_n_linear, isImage = True, level = 1) 
	reconstroi = aplica_IDTWT_em_sinal(transf_n_linear, "coif2", True)
	mostra_sinal(reconstroi, isImage = True)

	db = snr(sinal, reconstroi, isImage = True)
	print(f"snr dps de filtrar = {db}")
	'''
	snr_db = estima_snr_wavelet(transformado, sinal, 700)
	print(f"snr por wavelet = {snr_db}")
	'''
	return 0

if __name__ == "__main__":
	main()