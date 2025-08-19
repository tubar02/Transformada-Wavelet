from pathlib import Path
import numpy as np
import numpy.typing as npt
from typing import Any, Literal, overload
import useful_lib as ul
import my_image_lib_0_8 as mil

ComplexArray = npt.NDArray[np.complexfloating[Any, Any]]
FloatArray   = npt.NDArray[np.floating[Any]]

BASE = Path(__file__).resolve().parents[0]  # Pasta dos códigos
DIR_SINAIS  = BASE / "Sinais"
DIR_IMAGENS = BASE / "Imagens"

@overload
def carrega_sinal(nome: str = "std", is_image: Literal[False] = False) -> tuple[ComplexArray, FloatArray, float, int]: ...
@overload
def carrega_sinal(nome: str = "std", is_image: Literal[True]  = True)  -> mil.Image: ...

def carrega_sinal(nome: str = "std", isImage: bool = False):
	"""
    Se is_image=False: lê 'Sinais/<nome>.txt' e retorna (sinal, tempos, dt, n) 
    Se is_image=True:  carrega 'Imagens/<nome>.pgm' e retorna mil.Image
    """
	if isImage:
		caminho = DIR_IMAGENS / f"{nome}.pgm"
	else:
		caminho = DIR_SINAIS / f"{nome}.txt"
	return ul.le_arquivo_sinal(caminho, isImage)

def salva_sinal_txt(sinal: np.ndarray, tempos: np.ndarray, nome: str):
	"""Salva um sinal em 'Sinais/<nome>.txt."""
	caminho = DIR_SINAIS / f"{nome}.txt"
	DIR_SINAIS.mkdir(parents=True, exist_ok=True) # Garante que a pasta exista
	ul.salva_sinal(sinal, tempos, nome)  
	return caminho

def lista_sinais(extensao = ".txt", isImage = False) -> list[str]:
	"""Lista todos os sinais de um diretório."""
	if isImage: 
		diretorio = DIR_IMAGENS
	else:
		diretorio = DIR_SINAIS
	
	diretorio.mkdir(exist_ok=True)
	arquivos = diretorio.glob(f"*{extensao}") # Lista todos os arquivos do diretório que possuem a extensão
	organizado = [str(i) for i in sorted(nome.stem for nome in arquivos)] # Organiza os nomes dos arquivos em ordem alfabética, cortando a extensão
	return organizado

def main():
	print(carrega_sinal)

if __name__ == "__main__":
	main()