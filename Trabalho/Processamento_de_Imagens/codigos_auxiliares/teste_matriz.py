from copy import deepcopy, copy
from math import pi, exp
import cmath
import scipy.fftpack as fp

def _fourier(matriz_pixels):
    return fp.fft2(matriz_pixels)

def _inv_fourier(matriz_fourier):
	return fp.ifft2(matriz_fourier)

class Matrix():
	def __init__(self, matriz):
		self.matrix = matriz
		self.nlinha = len(matriz)
		self.ncoluna = len(matriz[0])

	def __str__(self):
		saida = ""

		for k in self.matrix:
			saida += f"| {' '.join(str(elemento) for elemento in k)} |" + "\n"
		
		return saida
	
	def _zero_padding(self, k): #cria uma borda de zeros em volta da matriz matriz
		imagem = deepcopy(self.matrix) #imagem q será colocada a borda
		imagem_aux = [] #borda de cima
		aux = int((k - 1) / 2) #tamanho da borda
		
		for i in range(aux):
			linha = (len(self.matrix[0]) + 2 * (aux)) * [0]
			imagem_aux.append(linha)
		
		for i in range(len(self.matrix)): #borda dos lados
			imagem_aux.append((aux) * [0] + imagem[i] + [0] * (aux))
			
		for i in range(aux): #borda de baixo
			linha = (len(self.matrix[0]) + 2 * (aux)) * [0]
			imagem_aux.append(linha)
		
		return Matrix(imagem_aux)
	
	def _mirror_padding(self, k): #cria uma borda de zeros em volta da matriz pixels
		imagem1 = deepcopy(self.matrix) #imagem q será colocada a borda
		imagem = []
		for i in range(len(self.matrix)):
			linha = []
			for j in range(len(self.matrix[0])):
				linha.append("\033[91m" + self.matrix[i][j] + "\033[0m")
			imagem.append(linha)

		imagem_aux = [] 
		aux = int((k - 1) / 2) #tamanho da borda
		
		for i in range(aux): #borda de cima
			linha = copy(imagem1[aux - i - 1]) #parte do meio

			for k in range(aux):
				linha.append(imagem1[aux - i - 1][-k - 1]) #canto da direita
				linha.insert(0, imagem1[aux - i - 1][k]) #canto da esquerda

			imagem_aux.append(linha)
		
		for i in range(len(imagem)): #borda dos lados
			linha = copy(imagem[i]) #parte do meio
			
			for k in range(aux): 
				linha.append(imagem1[i][-k - 1]) #parte da direita
				linha.insert(0, imagem1[i][k]) #parte da esquerda
			
			imagem_aux.append(linha)

		for i in range(aux): #borda de baixo
			linha = copy(imagem1[-i - 1]) #parte do meio

			for k in range(aux):
				linha.append(imagem1[-i - 1][-k - 1]) #canto da direita
				linha.insert(0, imagem1[-i - 1][k]) #canto da esquerda

			imagem_aux.append(linha)
		
		return Matrix(imagem_aux)

	def _rep_padding(self, k): #cria uma borda tipo espelho em volta da matriz pixels
		imagem1 = deepcopy(self.matrix) #imagem q será colocada a borda
		imagem = []
		for i in range(len(self.matrix)):
			linha = []
			for j in range(len(self.matrix[0])):
				linha.append("\033[91m" + self.matrix[i][j] + "\033[0m")
			imagem.append(linha)
		imagem_aux = [] #borda de cima
		aux = int((k - 1) / 2) #tamanho da borda
		
		for i in range(aux): #borda de cima
			linha = copy(imagem1[aux - i]) #parte do meio

			for k in range(aux):
				linha.append(imagem1[aux - i][-k - 2]) #canto da direita
				linha.insert(0, imagem1[aux - i][k + 1]) #canto da esquerda

			imagem_aux.append(linha)
		
		for i in range(len(imagem)): #borda dos lados
			linha = copy(imagem[i]) #parte do meio
			
			for k in range(aux): 
				linha.append(imagem1[i][-k - 2]) #parte da direita
				linha.insert(0, imagem1[i][k + 1]) #parte da esquerda
			
			imagem_aux.append(linha)

		for i in range(aux): #borda de baixo
			linha = copy(imagem1[-i - 2]) #parte do meio

			for k in range(aux):
				linha.append(imagem1[-i - 2][-k - 2]) #canto da direita
				linha.insert(0, imagem1[-i - 2][k + 1]) #canto da esquerda

			imagem_aux.append(linha)
		
		return Matrix(imagem_aux)
	
	def _periodic_padding(self, k): 
		imagem1 = deepcopy(self.matrix) #imagem q será colocada a borda
		imagem = []
		for i in range(len(self.matrix)):
			linha = []
			for j in range(len(self.matrix[0])):
				linha.append("\033[91m" + self.matrix[i][j] + "\033[0m")
			imagem.append(linha)
		imagem_aux = [] #borda de cima
		aux = int((k - 1) / 2) #tamanho da borda
		imagem_aux = []
		aux = int((k - 1) / 2) #tamanho da borda
		
		for i in range(aux): #borda de cima
			linha = copy(imagem1[-aux + i]) #parte do meio

			for k in range(aux):
				linha.append(imagem1[-aux + i][k]) #canto da direita
				linha.insert(0, imagem1[-aux + i][-k - 1]) #canto da esquerda

			imagem_aux.append(linha)
		
		for i in range(len(imagem)): #borda dos lados
			linha = copy(imagem[i]) #parte do meio
			
			for k in range(aux): 
				linha.append(imagem1[i][k]) #parte da direita
				linha.insert(0, imagem1[i][-k - 1]) #parte da esquerda
			
			imagem_aux.append(linha)

		for i in range(aux): #borda de baixo
			linha = copy(imagem1[i]) #parte do meio

			for k in range(aux):
				linha.append(imagem1[i][k]) #canto da direita
				linha.insert(0, imagem1[i][-k - 1]) #canto da esquerda

			imagem_aux.append(linha)
		
		return Matrix(imagem_aux)
	
	def convolucao(self, k = 3, matriz_convolucao = None, _funcao_borda = _zero_padding):
		if matriz_convolucao is None: #caso a matriz não seja dada, cria a matriz mais simples, que é a de média
			matriz_convolucao = [] 
			for i in range(k):
				matriz_convolucao.append(k * [(1 / k ** 2)]) #matriz de média
		
		print("\nMatriz de convolução:\n")
		print(Matrix(matriz_convolucao))

		aux = int((k - 1) / 2) #auxilia na definição de bordas e nos valores de iteradores
		imagem = deepcopy(self.matrix)
			
		imagem_aux = _funcao_borda(self, k)
		print("\nImagem com borda:\n")
		print(imagem_aux)
			
		for i in range(self.nlinha): #percorre as linhas da imagem
			for j in range(self.ncoluna): #percorre as colunas da imagem
				soma = 0
				for a1, a2 in zip(range(-aux, aux + 1), range(k)): #percorre as linhas da matriz de convolução
					for b1, b2 in zip(range(-aux, aux + 1), range(k)): #percorre as colunas da matriz de convolução
						print(f'Caso [{i + aux + a1}][{j + aux + b1}] da imagem com borda:', imagem_aux.matrix[i + aux + a1][j + aux + b1], matriz_convolucao[a2][b2])
						soma += float(imagem_aux.matrix[i + aux + a1][j + aux + b1]) * matriz_convolucao[a2][b2]
				print(f'\nApós convolução, imagem[{i}][{j}] virou {soma}\n')
				imagem[i][j] = int(round(soma))
			
		return Matrix(imagem)

	def mean(self, k = 3, _funcao_borda = _zero_padding):
		aux = int((k - 1) / 2) #auxilia na definição de bordas e nos valores de iteradores
		imagem = deepcopy(self.matrix)
			
		imagem_aux = _funcao_borda(self, k)
		print("\nImagem com borda:\n")
		print(imagem_aux)
			
		for i in range(self.nlinha):
			for j in range(self.ncoluna):
				vizinhos = []
				for a in range(-aux, aux + 1): #vê quem são os vizinhos
					for b in range(-aux, aux + 1):
						vizinhos.append(imagem_aux.matrix[i + aux + a][j + aux + b])
				imagem[i][j] = int(round(self._media_lista(vizinhos)))
			
		return Matrix(imagem)
	
	@staticmethod
	def _media_lista(lista): #recebe uma lista e retorna a média dos valores
		if len(lista) == 0: #para evitar divisão por 0
			return 0
		else:
			return sum(lista) / len(lista)

def kernel_gaussiano(desvio_padrao, k):
	aux = int((k - 1) / 2) #tamanho do kernel
	K = 1 / (2 * pi * desvio_padrao ** 2) #constante K
	
	matriz_gauss = [] #kernel gaussiano
	for s in range(-aux, aux + 1): #linha
		linha = []
		for t in range(-aux, aux + 1): #coluna
			valor = K * 	exp(-1 * (s ** 2 + t ** 2) / (2 * desvio_padrao ** 2)) #valor a ser colocado no kernel
			linha.append(valor)
		matriz_gauss.append(linha)
	
	return Matrix(matriz_gauss)

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
	return Matrix(matriz)

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
	return Matrix(matriz)

def _subtrai_matriz(matriz1, matriz2): #subtrai duas matrizes
		linhas, colunas = len(matriz1.matrix), len(matriz1.matrix[0]) #recebe as dimensões da matriz

		assert linhas == len(matriz2.matrix) and colunas == len(matriz2.matrix[0]), "As dimensões das matrizes devem ser iguais"

		nova_mat = [] #matriz que será retornada
		for i in range(linhas):
			linha = []
			for j in range(colunas):
				subtrai = matriz1.matrix[i][j] - matriz2.matrix[i][j]
				linha.append(subtrai)
			nova_mat.append(linha)
		
		return Matrix(nova_mat)

def zera_impares(_matriz):
	matriz = deepcopy(_matriz)
	linhas, colunas = len(matriz), len(matriz[0])
	for i in range(1, linhas, 2):
		for j in range(colunas):
			matriz[i][j] = 0
	return Matrix(matriz)

def zera5(_matriz):
	matriz = deepcopy(_matriz)
	linhas, colunas = len(matriz), len(matriz[0])
	for i in range(0, linhas, 10):
		for aux in range(5):
			if aux + i >= linhas: 
				break
			for j in range(colunas):
				matriz[i + aux][j] = 0
	return Matrix(matriz)

def tira_impar(_matriz):
	matriz = deepcopy(_matriz)
	resultado = matriz[::2]
	return Matrix(resultado)

def main():
	ordem = int(input("Entre com a ordem das matrizes: "))
	matriz = []
	for j in range(ordem):
		matriz.append([int(i) for i in input(f'Entre com a linha {j + 1} da matriz: ').split()])
	
	matriz1 = Matrix(matriz)

	print(matriz1)

	subtrai = tira_impar(matriz1.matrix)

	print("\n")
	print(subtrai)

main()