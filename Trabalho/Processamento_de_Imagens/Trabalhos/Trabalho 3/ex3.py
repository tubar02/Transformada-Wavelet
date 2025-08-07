import my_image_lib_0_3 as img

def detector_borda(imagem, outputpath, funcao_borda):
	kernel_passa_alta = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]] #filtro passa alta
	for i in range(len(kernel_passa_alta)):
		for j in range(len(kernel_passa_alta[0])):
			kernel_passa_alta[i][j] *= 1 / 9 #normaliza o filtro

	borda = imagem.convolution(outputpath, 3, funcao_borda, kernel_passa_alta)
	return borda
      
def realce_borda(imagem, outputpath, funcao_borda):
	kernel_passa_alta = [[-1, -1, -1], [-1, 17, -1], [-1, -1, -1]] #filtro passa alta
	for i in range(len(kernel_passa_alta)):
		for j in range(len(kernel_passa_alta[0])):
			kernel_passa_alta[i][j] *= 1 / 9 #normaliza o filtro

	borda = imagem.convolution(outputpath, 3, funcao_borda, kernel_passa_alta)
	return borda

def main():
    matriz = [] #faz a imagem com os 4 quadrados
    linha = [] #cria a linha padrão
    for pixel in [0, 255]: #itera duas vezes
        for j in range(256):
            linha.append(pixel)
    for iterador in [1, -1]: #itera duas vezes
        for j in range(256):
            matriz.append(linha[::iterador]) #iterador inverte a ordem depois da primeira iteração
    
    quadrados = img.pgm_from_matrix("Trabalho 3\\Output\\quadrados.pgm", matriz)
    img.print_grayscale_image(quadrados)

    quadrados_zero_pad = quadrados.convolution("Trabalho 3\\Output\\quadrados_zero.pgm", 15)
    img.print_grayscale_image(quadrados_zero_pad)

    quadrados_mirror_pad = quadrados.convolution("Trabalho 3\\Output\\quadrados_mirror.pgm", 15, img.Image._mirror_padding)
    img.print_grayscale_image(quadrados_mirror_pad)

    quadrados_rep_pad = quadrados.convolution("Trabalho 3\\Output\\quadrados_rep.pgm", 15, img.Image._rep_padding)
    img.print_grayscale_image(quadrados_rep_pad)

    quadrados_periodic_pad = quadrados.convolution("Trabalho 3\\Output\\quadrados_periodic.pgm", 15, img.Image._periodic_padding)
    img.print_grayscale_image(quadrados_periodic_pad)
	
    imagem = img.Image("Trabalho 3\\Input\\lena.pgm")
    img.print_grayscale_image(imagem)
    
    for k in [3, 7, 15]: #valores de k
        media = imagem.convolution(f'Trabalho 3\\Output\\lena_meank{k}.pgm', k, img.Image._mirror_padding)
        img.print_grayscale_image(media)
                               
    for k in [3, 7, 15]: #valores de k
        for desvio in [1, 5, 10]: #valores do desvio padrão
            desvio = imagem.convolution(f'Trabalho 3\\Output\\lena_desvio{desvio}k{k}.pgm', k, img.Image._mirror_padding, img.kernel_gaussiano(desvio, k))
            img.print_grayscale_image(desvio)
	
    bordas = detector_borda(imagem, "Trabalho 3\\Output\\lena_borda.pgm", img.Image._mirror_padding)
    img.print_grayscale_image(bordas)
	
    realce = realce_borda(imagem, "Trabalho 3\\Output\\lena_realce.pgm", img.Image._mirror_padding)
    img.print_grayscale_image(realce)

main()