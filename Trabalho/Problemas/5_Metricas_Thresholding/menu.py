# Módulos nativos do python
from dataclasses import dataclass # Para facilitar o manuseio dos parâmetros
from pathlib import Path 

import numpy as np

import useful_lib as ul
import my_image_lib_0_8 as mil

@dataclass
class AppState:
	nome_sinal: str = "std"
	isImage: bool = False
	sinal: np.ndarray | mil.Image = None
	tempos: np.ndarray | None = None
	dt: float | None = None
	salvou: bool = True

	def __post_init__(self):
		if self.nome_sinal == "std":
			caminho = Path(f'Sinais/{self.nome_sinal}.txt')
			self.sinal, self.tempos, self.dt = ul.le_arquivo_sinal(caminho)

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

	def processar_escolha(self, escolha):
		"""Trata a escolha do usuário. Retorna um sinal se for para sair."""
		pass

	def run(self):
		"""Loop principal do menu: exibe, lê entrada e processa até sinalizar saída."""
		while self.rodando:
			self.exibir()  # Mostra o menu atual
			escolha = input("Selecione uma opção: ")
			resultado = self.processar_escolha(escolha)
			if resultado == "SAIR":  
				# Se o submenu solicitou sair/voltar
				self.rodando = False
		# Fim do loop: se houver pai, retorno ao menu pai; se não, programa termina.

class MainMenu(MenuBase):
	def __init__(self):
		super().__init__(parent=None)  # Menu principal não tem pai
		self.titulo = "Menu Principal"

	def exibir(self):
		print(f"=== {self.titulo} ===")
		print("1. Menu de Processamento Wavelet")
		print("2. Outra funcionalidade")
		print("0. Sair")

	def processar_escolha(self, escolha):
		if escolha == "1":
			submenu = WaveletMenu(parent=self)
			submenu.run()            # Entra no submenu de wavelet
			# Ao retornar, o loop deste MainMenu continua
		elif escolha == "2":
			pass
			# executar_outra_funcionalidade()
		elif escolha == "0":
			print("Encerrando o programa...")
			return "SAIR"            # Sinaliza para sair do loop do menu principal
		else:
			print("Opção inválida! Tente novamente.")

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
	appstate = AppState()
	print(appstate)