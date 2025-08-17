from pathlib import Path
import numpy as np
import useful_lib as ul
import my_image_lib_0_8 as mil

BASE = Path(__file__).resolve().parents[0]  # pasta do Problema 5
DIR_SINAIS  = BASE / "Sinais"
DIR_IMAGENS = BASE / "Imagens"

def carrega_sinal_txt(nome: str):
	"""Lê 'Sinais/<nome>.txt' e retorna (sinal, tempos, dt)."""
	caminho = DIR_SINAIS / f"{nome}.txt"
	return ul.le_arquivo_sinal(caminho)

def carrega_imagem(path: str | Path) -> mil.Image:
	return mil.Image(str(path))

def salva_sinal_txt(sinal: np.ndarray, tempos: np.ndarray, nome: str):
	caminho = DIR_SINAIS / f"{nome}.txt"
	DIR_SINAIS.mkdir(parents=True, exist_ok=True)
	ul.salva_sinal(sinal, tempos, nome)  # se sua função já escreve na pasta Sinais/, ok
	return caminho

def lista_sinais(ext=".txt"):
	DIR_SINAIS.mkdir(exist_ok=True)
	return sorted(p.stem for p in DIR_SINAIS.glob(f"*{ext}"))