import my_image_lib_0_5 as img

def imag_e_hist(imagem, titulo = ''):
    img.print_grayscale_image(imagem)
    img.plota_histograma(imagem, titulo)

def matriz_grad(n):
	matriz = []
	for i in range(n + 1):
		linha = []
		for j in range(n + 1):
			if i < j:
				linha.append(i)
			else:
				linha.append(j)
		matriz.append(linha)
	return matriz

def inv_matriz_grad(n):
	matriz = []
	for i in range(n, -1, -1):
		linha = []
		for j in range(n, -1, -1):
			if i > j:
				linha.append(i)
			else:
				linha.append(j)
		matriz.append(linha)
	return matriz

def main():
	grad = matriz_grad(255)
	inv_grad = inv_matriz_grad(255)

	matriz = [] #faz a imagem com os 4 quadrados

	for j in range(2):
		for i in range(256):
			linha = []
			for k in range(2):
				linha += grad[i] + inv_grad[i]
			matriz.append(linha)

		for i in range(256):
			linha = []
			for k in range(2):
				linha += inv_grad[i] + grad[i]
			matriz.append(linha)

	imagem = img.pgm_from_matrix("Trabalho 5\\Input\\matrix_grad.pgm", matriz)
	imag_e_hist(imagem, "Histograma da Imagem Gerada")

	imagem_fourier = img.Fourier_Image(imagem)
	representa1 = imagem_fourier.representacao()
	img.print_grayscale_image(representa1)

	sal_pimenta = img.Ruido(imagem)
	sal_pimenta.impulsivo(25)
	ruidosa = imagem.corrompe("Trabalho 5\\Output\\matrix_salt.pgm", sal_pimenta)
	imag_e_hist(ruidosa, "Histograma da Imagem com Ruído")

	ruidosa_fourier = img.Fourier_Image(ruidosa)
	representa2 = ruidosa_fourier.representacao()
	img.print_grayscale_image(representa2)

	filtrado = ruidosa.median("Trabalho 5\\Output\\matrix_median.pgm", 3)
	imag_e_hist(filtrado)

main()