# Módulos nativos do python
from dataclasses import dataclass # Para facilitar o manuseio dos parâmetros
from pathlib import Path 

import numpy as np

import useful_lib as ul
import my_image_lib_0_8 as mil
import cli_helpers as cli
import io_helpers as io

@dataclass
class AppState:
	nome_sinal: str = "std"
	isImage: bool = False
	sinal: np.ndarray | mil.Image = None
	tempos: np.ndarray | None = None
	dt: float | None = None
	salvou: bool = True

class MenuBase:
	def __init__(self, parent=None, state=None):
		self.parent = parent
		self.state = state
		self.rodando = True
		self.opcoes = {}  # "tecla": ("Descrição", função)

	def exibir(self):
		# cada filho pode sobrescrever o cabeçalho, mas aqui listamos as opções
		for k, (desc, _) in self.opcoes.items():
			print(f"[{k}] {desc}")
			print("\n")

	def processar_escolha(self, escolha):
		"""Trata a escolha do usuário. Retorna "SAIR" se for para sair."""
		_, handler = self.opcoes[escolha]
		return handler()

	def run(self):
		"""Loop principal do menu: exibe, lê entrada e processa até sinalizar saída."""

		opcoes_validas = [i[0] for i in self.opcoes.items()]

		while self.rodando:
			self.exibir()  # Mostra o menu atual
			escolha = cli.faz_escolha("Digite sua escolha: ", opcoes_validas)
			resultado = self.processar_escolha(escolha)
			if resultado == "SAIR":  
				# Se o submenu solicitou sair/voltar
				self.rodando = False
		# Fim do loop: se houver pai, retorno ao menu pai; se não, programa termina.

class MainMenu(MenuBase):
	def __init__(self, state):
		super().__init__(None, state)  # Menu principal não tem pai
		self.titulo = "Problema 5 - Menu Principal"
		self.opcoes = {"X": ("Encerra o programa.", self.sair)}

	def exibir(self):
		print(12 * "==" + " " + self.titulo + " " + 12 * "==" + "\n\n")
		super().exibir()

	def sair(self):
		return "SAIR"
		
class WaveletMenu(MenuBase):
	def __init__(self, parent):
		super().__init__(parent)
		self.titulo = "Menu de Processamento Wavelet"

	def exibir(self):
		print(f"=== {self.titulo} ===")
		print("1. Aplicar transformada Wavelet na imagem X")
		print("2. Aplicar transformada Wavelet na imagem Y")
		print("0. Voltar")

	def processar_escolha(self, escolha):
		if escolha == "1":
			pass
			# aplicar_wavelet_imagem_x()   # Chamada da função de processamento correspondente
		elif escolha == "2":
			pass
			# aplicar_wavelet_imagem_y()
		elif escolha == "0":
			print("Retornando ao menu anterior...")
			return "SAIR"                # Sinaliza para encerrar este menu (voltar)
		else:
			print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
	state = AppState()
	menu = MainMenu(state)
	menu.run()