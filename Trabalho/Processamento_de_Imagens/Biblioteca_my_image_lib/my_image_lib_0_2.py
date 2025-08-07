import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import floor
from copy import deepcopy
import numpy as np

#classe que representa uma imagem digital
class Image:
	def __init__(self, MeuArquivo):
		self._local = MeuArquivo
		with open(MeuArquivo, "r") as arquivo:
			self.magic_number = arquivo.readline().rstrip("\n") #lê o número mágico
			if self.magic_number == "P2": #Caso seja um arquivo .pgm
				dim = [int(i) for i in arquivo.readline().split()] #lê as dimensões
				dim2 = (dim[0], dim[1])
				self.dimensions = dim2
				self.colunas = self.dimensions[0]
				self.linhas = self.dimensions[1]
				self.maxval = int(arquivo.readline()) #lê o valor máximo
			
			self.pixels = self._get_matrix(arquivo, self.magic_number)
			
			self.hist = [] #inicializa o histograma
			conta_pixel = 0 #conta quantos pixels tem
			
			for j in range(256): #j representa a intensidade do pixel que está sendo contado
				for k in self.pixels:
					conta_pixel += k.count(j)
				self.hist.append(conta_pixel)
				conta_pixel = 0
	
	#propriedades do objeto
	@property
	def magic(self):
		return self.magic_number
	
	@property
	def dimension(self):
		return self.dimensions
	
	@property
	def ncoluna(self):
		return self.colunas
	
	@property
	def nlinha(self):
		return self.linhas
	
	@property
	def max(self):
		return self.maxval
	
	@property
	def min(self):
		minimo = min(self.pixels[0])

		for linha in self.pixels:
			if min(linha) < minimo:
				minimo = min(linha)
		
		return minimo
		
	def pixel(self):
		return self.pixels
		
	def histogram(self):
		return self.hist
	
	#métodos
	def thresholding(self, outputpath, t = 127):
		with open(outputpath, "w") as arquivo:
			arquivo.write(self.magic + "\n") #escreve o número mágico
			arquivo.write(str(self.ncoluna) + " " + str(self.nlinha) + "\n") #escreve as dimensões
			imagem = self.pixels[:] #inicializa os pixels da nova imagem
			
			for i in range(self.nlinha): #joga a intensidade pra 255 ou pra 0 dependendo do valor do pixel
				for j in range(self.ncoluna):
					if imagem[i][j] > t:
						imagem[i][j] = 255
					else:
						imagem[i][j] = 0
			
			maximo_imagem = self._max_matriz(imagem)
			arquivo.write(str(maximo_imagem) + "\n")
			
			self._escreve_pixels(arquivo, imagem)
		
		return Image(outputpath)
	
	def sgt(self, outputpath, dt = 1):
		with open(outputpath, "w") as arquivo:
			arquivo.write(self.magic + "\n") #escreve o número mágico
			arquivo.write(str(self.ncoluna) + " " + str(self.nlinha) + "\n") #escreve as dimensões
			imagem = self.pixels[:] #inicializa os pixels da nova imagem
			
			self.old_t = 0
			
			grupo_menor = [] #inicializa duas listas, que serão usadas para calcular as médias dos grupos 1 e 2
			grupo_maior = []
			
			for i in imagem:
				for k in i:
					if k > self.old_t:
						grupo_maior.append(k)
					else:
						grupo_menor.append(k)
			
			self.new_t = 0.5 * (self._media_lista(grupo_maior) + self._media_lista(grupo_menor)) #conseguido o novo valor pra T, começa um loop
			
			while abs(self.new_t - self.old_t) >= dt: #checa se a diferença é maior que dt
				self.old_t = self.new_t
				
				grupo_menor = []
				grupo_maior = []
				
				for i in imagem:
					for k in i:
						if k > self.old_t:
							grupo_maior.append(k)
						else:
							grupo_menor.append(k)
				self.new_t = 0.5 * (self._media_lista(grupo_maior) + self._media_lista(grupo_menor))
			
			self.new_t = floor(self.new_t) #joga T para o maior inteiro possível
				
			for i in range(self.nlinha): #joga a intensidade pra 255 ou pra 0 dependendo do valor do pixel
				for j in range(self.ncoluna):
					if imagem[i][j] > self.new_t:
						imagem[i][j] = 255
					else:
						imagem[i][j] = 0
			
			maximo_imagem = self._max_matriz(imagem) #aqui eu uso a mesma aplicação do método thresholding, para evitar que sejam criados 2 arquivos
			arquivo.write(str(maximo_imagem) + "\n")
			self._escreve_pixels(arquivo, imagem)

		return Image(outputpath)
	
	#parto do pressuposto que k sempre será ímpar	
	def mean(self, outputpath, k = 3):
		aux = int((k - 1) / 2) #auxilia na definição de bordas e nos valores de iteradores
		with open(outputpath, "w") as arquivo:
			arquivo.write(self.magic + "\n") #escreve o número mágico
			arquivo.write(str(self.ncoluna) + " " + str(self.nlinha) + "\n") #escreve as dimensões
			imagem = self.pixels[:] #inicializa os pixels da nova imagem
			
			#zero padding
			
			imagem_aux = [] #borda de cima
			for i in range(aux):
				linha = (self.ncoluna + 2 * (aux)) * [0]
				imagem_aux.append(linha)
			
			for i in range(len(imagem)): #borda dos lados
				imagem_aux.append((aux) * [0] + imagem[i] + [0] * (aux))
				
			for i in range(aux): #borda de baixo
				linha = (self.ncoluna + 2 * (aux)) * [0]
				imagem_aux.append(linha)
			
			#média
			
			for i in range(self.nlinha):
				for j in range(self.ncoluna):
					vizinhos = []
					for a in range(-aux, aux + 1): #vê quem são os vizinhos
						for b in range(-aux, aux + 1):
							vizinhos.append(imagem_aux[i + aux + a][j + aux + b])
					imagem[i][j] = int(self._media_lista(vizinhos))
			
			maximo_imagem = self._max_matriz(imagem)
			arquivo.write(str(maximo_imagem) + "\n")
			
			self._escreve_pixels(arquivo, imagem)
			
		return Image(outputpath)
	
	#parto do pressuposto que k sempre será ímpar
	def median(self, outputpath, k):
		aux = int((k - 1) / 2) #auxilia na definição de bordas e nos valores de iteradores
		with open(outputpath, "w") as arquivo:
			arquivo.write(self.magic + "\n") #escreve o número mágico
			arquivo.write(str(self.ncoluna) + " " + str(self.nlinha) + "\n") #escreve as dimensões
			imagem = self.pixels[:] #inicializa os pixels da nova imagem
			
			#zero padding
			
			imagem_aux = [] #borda de cima
			for i in range(aux):
				linha = (self.ncoluna + 2 * (aux)) * [0]
				imagem_aux.append(linha)
			
			for i in range(len(imagem)): #borda dos lados
				imagem_aux.append((aux) * [0] + imagem[i] + [0] * (aux))
				
			for i in range(aux): #borda de baixo
				linha = (self.ncoluna + 2 * (aux)) * [0]
				imagem_aux.append(linha)
			
			#mediana
			
			for i in range(self.nlinha):
				for j in range(self.ncoluna):
					vizinhos = []
					for a in range(-aux, aux + 1): #vê quem são os vizinhos
						for b in range(-aux, aux + 1):
							vizinhos.append(imagem_aux[i + aux + a][j + aux + b])
					imagem[i][j] = int(self._mediana_lista(vizinhos))
			
			maximo_imagem = self._max_matriz(imagem)
			arquivo.write(str(maximo_imagem) + "\n")
			self._escreve_pixels(arquivo, imagem)
						
		return Image(outputpath)

	def transformacao_linear(self, outputpath, contraste, brilho): #realiza uma transformação linear na imagem
		with open(outputpath, "w") as arquivo:
			arquivo.write(self.magic + "\n") #escreve o número mágico
			arquivo.write(str(self.ncoluna) + " " + str(self.nlinha) + "\n") #escreve as dimensões
			imagem = deepcopy(self.pixels) #inicializa os pixels da nova imagem

			for i in range(self.nlinha):
				for j in range(self.ncoluna):
					transforma = contraste  * imagem[i][j] + brilho #aplica a transformação linear
					imagem[i][j] = int(transforma) #troca o valor do pixel

					if imagem[i][j] < 0: #caso a transformação tenha feito a imagem ultrapassar os limites
						imagem[i][j] = 0
					elif imagem[i][j] > 255:
						imagem[i][j] = 255
			
			maximo_imagem = self._max_matriz(imagem)
			arquivo.write(str(maximo_imagem) + "\n")
			
			self._escreve_pixels(arquivo, imagem)
			
		return Image(outputpath)
	
	def aplica_mascara(self, outputpath, mascara):
		with open(outputpath, "w") as arquivo:
			arquivo.write(self.magic + "\n") #escreve o número mágico
			arquivo.write(str(self.ncoluna) + " " + str(self.nlinha) + "\n") #escreve as dimensões
			imagem = deepcopy(self.pixels) #inicializa os pixels da nova imagem

			for i in range(self.nlinha):
				for j in range(self.ncoluna):
					imagem[i][j] *= mascara[i][j] #coloca a mascara por cima da imagem

			maximo_imagem = self._max_matriz(imagem)
			arquivo.write(str(maximo_imagem) + "\n")
			
			self._escreve_pixels(arquivo, imagem)
			
		return Image(outputpath)

	def mascara_bin(self, limite, maior = True): #cria uma máscara binária
		mascara = [] #inicializa a mascara

		if maior: #caso se queira mascarar valores maiores que limite
			for i in self.pixels:
				linha = []
				for j in i:
					if j > limite: #caso seja um pixel que será mascarado
						linha.append(0) 
					else:
						linha.append(1)
				mascara.append(linha)

		else: #caso se queira mascarar valores menores que limite
			for i in self.pixels:
				linha = []
				for j in i:
					if j < limite: #caso seja um pixel que será mascarado
						linha.append(0) 
					else:
						linha.append(1)
				mascara.append(linha)
		
		return mascara

	#métodos usados na classe
	@staticmethod
	def _max_matriz(matriz): #recebe uma matriz e retorna o valor máximo dela
		maximo = 0
		for k in matriz:
			if max(k) > maximo:
				maximo = max(k)
		return maximo	
	
	@staticmethod
	def _media_lista(lista): #recebe uma lista e retorna a média dos valores
		if len(lista) == 0: #para evitar divisão por 0
			return 0
		else:
			return sum(lista) / len(lista)
			
	@staticmethod
	def _mediana_lista(lista): #recebe uma lista e retorna a mediana dos valores
		lista.sort()
		aux = int((len(lista) - 1) / 2)
		return lista[aux]
	
	@staticmethod
	def _get_matrix(arq, numero_magico): #recebe os pixels da imagem
		matriz = []
		if numero_magico == "P2": #Lê .pgm
			for k in arq.readlines():
				matriz.append([int(i) for i in list(k.split())])
		return matriz
	
	@staticmethod
	def _escreve_pixels(arquivo, imagem):
		for k in imagem:
				arquivo.write(" ".join([str(i) for i in k]) + "\n")

#funções úteis
def perfil_linha(imagem, linha): #Histograma de uma linha da imagem
		hist = [] #inicializa o histograma
		conta_pixel = 0 #conta quantos pixels tem
		print("to na funcao perfil_linha")
			
		for j in range(256): #j representa a intensidade do pixel que está sendo contado
			conta_pixel = imagem.pixels[linha].count(j)
			hist.append(conta_pixel)
			conta_pixel = 0
		
		return hist

def normaliza_hist(hist): #Normaliza o histograma
	histograma = hist[:] #Para não alterar a lista passada

	total = sum(histograma)

	for k in range(len(histograma)):
		histograma[k] = histograma[k] / total
	
	return histograma

#funções de plot
def print_image(imagem): #Plota a imagem em cor
    img = mpimg.imread(imagem._local)
    plt.imshow(img)
    plt.axis('off')  # Para desativar os eixos
    plt.show()

def print_grayscale_image(imagem): #Plota a imagem em escala de cinza
	img = mpimg.imread(imagem._local)
    
    # Exibir a imagem em tons de cinza
	plt.imshow(img, cmap='gray', vmin=0, vmax=255)
	plt.axis('off')  # Para desativar os eixos
	plt.show()

def plota_histograma(imagem, titulo = "Histograma da Imagem", histograma = None,  cor = "cornflowerblue"): #Plota um histograma
	if histograma is None: #Forma de padronizar a variável histograma
		histograma = imagem.hist

	intensidades = range(len(histograma)) 

	plt.bar(intensidades, histograma, color = cor)
	plt.xlabel("Intensidade")
	plt.ylabel("Número de pixels")
	plt.title(titulo)

	# Define os limites dos eixos x e y
	plt.xlim(0, len(histograma))  # Limites do eixo x de 0 a 255 (intervalo de intensidades)
	plt.ylim(0, max(histograma))  # Limites do eixo y de 0 ao máximo valor do histograma

	plt.show()