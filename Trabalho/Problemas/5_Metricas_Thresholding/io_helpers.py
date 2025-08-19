from pathlib import Path
import numpy as np
import useful_lib as ul
import my_image_lib_0_8 as mil

BASE = Path(__file__).resolve().parents[0]  # Pasta dos códigos
DIR_SINAIS  = BASE / "Sinais"
DIR_IMAGENS = BASE / "Imagens"

def carrega_sinal_txt(nome: str):
	"""Lê 'Sinais/<nome>.txt' e retorna (sinal, tempos, dt)."""
	caminho = DIR_SINAIS / f"{nome}.txt"
	return ul.le_arquivo_sinal(caminho)

def carrega_imagem(nome: str) -> mil.Image:
	"""Lê 'Imagens/<nome>.pgm' e retorna um objeto mil.Image."""
	caminho = DIR_IMAGENS / f"{nome}.pgm"
	return mil.Image(str(caminho))

def salva_sinal_txt(sinal: np.ndarray, tempos: np.ndarray, nome: str):
	caminho = DIR_SINAIS / f"{nome}.txt"
	DIR_SINAIS.mkdir(parents=True, exist_ok=True) # Garante que a pasta exista
	ul.salva_sinal(sinal, tempos, nome)  
	return caminho

def lista_sinais(extensao = ".txt", isImage = False):
	if isImage: 
		diretorio = DIR_IMAGENS
	else:
		diretorio = DIR_SINAIS
	
	diretorio.mkdir(exist_ok=True)
	arquivos = diretorio.glob(f"*{extensao}") # Lista todos os arquivos do diretório que possuem a extensão
	organizado = sorted(nome.stem for nome in arquivos) # Organiza os nomes dos arquivos em ordem alfabética, cortando a extensão
	return organizado

def main():
	lista = lista_sinais()
	print(lista)

if __name__ == "__main__":
	main()