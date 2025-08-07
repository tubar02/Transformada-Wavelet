import my_image_lib_0_4 as img
from copy import deepcopy

def zera_centro(_matriz, a = 1, b = 1):
	matriz = deepcopy(_matriz)
	m, n = len(matriz) // 2, len(matriz[0]) // 2
	for i in range(m - a, a + m):
		for j in range(n - b, b + n):
			matriz[i][j] = 0
	return matriz

def zera_impares(_matriz):
	matriz = deepcopy(_matriz)
	linhas, colunas = len(matriz), len(matriz[0])
	for i in range(1, linhas, 2):
		for j in range(colunas):
			matriz[i][j] = 0
	return matriz

def zera_pares(_matriz):
	matriz = deepcopy(_matriz)
	linhas, colunas = len(matriz), len(matriz[0])
	for i in range(0, linhas, 2):
		for j in range(colunas):
			matriz[i][j] = 0
	return matriz

def zera5(_matriz):
	matriz = deepcopy(_matriz)
	linhas, colunas = len(matriz), len(matriz[0])
	for i in range(0, linhas, 10):
		for aux in range(5):
			if aux + i >= linhas: 
				break
			for j in range(colunas):
				matriz[i + aux][j] = 0
	return matriz

def tira_impar(_matriz):
	matriz = deepcopy(_matriz)
	resultado = matriz[::2]
	return resultado

def main():
	output = "Trabalho 4\\Output\\"
	
	imagem = img.Image("Trabalho 4\\Input\\bird.pgm") #imagem
	img.print_grayscale_image(imagem)

	imagem_fourier = img.Fourier_Image(imagem) #transformada de fourier
	imagem_fourier.shift()

	representa1 = imagem_fourier.representacao() #visualização da transformada
	img.print_grayscale_image(representa1)
	'''
	imagem_volta = imagem_fourier.inverte(output + "birdInvFourier.pgm") #transformada inversa
	img.print_grayscale_image(imagem_volta)

	try:
		subtrai = imagem_volta - imagem #subtração
		img.print_grayscale_image(subtrai)
	except:
		print("A subtração resulta numa matriz de zeros")
	
	print(imagem_fourier._shift)
	imagem_volta = imagem_fourier.inverte(output + "birdShiftInv.pgm") #inversa sem shift
	img.print_grayscale_image(imagem_volta)
	'''
	zerado = imagem_fourier.filtro_espaco_de_freq(output + "bird_0center.pgm", zera_centro)
	img.print_grayscale_image(zerado) #zera o centro da transformada
	 
	representa2 = zerado.representacao()
	img.print_grayscale_image(representa2)

	impar = imagem_fourier.filtro_espaco_de_freq(output + "bird_0impar.pgm", zera_impares)
	img.print_grayscale_image(impar) #zera as linhas ímpares da transformada
	 
	representa2 = impar.representacao()
	img.print_grayscale_image(representa2)
	'''
	par = imagem_fourier.filtro_espaco_de_freq(output + "bird_0par.pgm", zera_pares)
	img.print_grayscale_image(par) #zera as linhas ímpares da transformada
	 
	representa3 = par.representacao()
	img.print_grayscale_image(representa3)
	'''
	cinco5 = imagem_fourier.filtro_espaco_de_freq(output + "bird_0cinco.pgm", zera5)
	img.print_grayscale_image(cinco5) #zera as linhas ímpares da transformada
	 
	representa4 = cinco5.representacao()
	img.print_grayscale_image(representa4)

	tira = imagem_fourier.filtro_espaco_de_freq(output + "bird_tiraimpar.pgm", tira_impar) #tira as linhas ímpares
	
	print(f"Dimensões da matriz após tira_impar: {len(tira.pixels)} x {len(tira.pixels[0])}")
	print(f"Primeiras linhas da matriz após tira_impar: {tira.pixels[:2]}")

	img.print_grayscale_image(tira)

	representa5 = tira.representacao()
	img.print_grayscale_image(representa5)

main()