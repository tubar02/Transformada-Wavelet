# Módulos nativos do python
from dataclasses import dataclass # Para facilitar o manuseio dos parâmetros

import numpy as np

import numpy.typing as npt
from typing import Callable

import useful_lib as ul
import my_image_lib_0_8 as mil
import cli_helpers as cli
import io_helpers as io

@dataclass
class Sinal:
	nome_sinal: str = "std"
	isImage: bool = False
	sinal: np.ndarray | mil.Image = None
	tempos: np.ndarray | None = None
	dt: float | None = None
	n_pontos: int = None
	salvou: bool = True

class MenuBase:
	pass
class MenuBase:
	def __init__(self, parent: MenuBase = None, estado: Sinal = None):
		self.parent = parent
		self.state = estado
		self.rodando: bool = True
		self.opcoes = {}  # "tecla": ("Descrição", função)

	def exibir(self):
		# cada filho pode sobrescrever o cabeçalho, mas aqui listamos as opções
		for k, (desc, _) in self.opcoes.items():
			print(f"[{k}] {desc}")
		print("\n")

	def processar_escolha(self, escolha: str) -> Callable:
		"""Trata a escolha do usuário. Retorna "SAIR" se for para sair."""
		_, handler = self.opcoes[escolha]
		return handler()

	def run(self):
		"""Loop principal do menu: exibe, lê entrada e processa até sinalizar saída."""

		opcoes_validas = [i[0] for i in self.opcoes.items()]

		while self.rodando:
			self.exibir()  # Mostra o menu atual
			escolha = cli.faz_escolha("Digite sua escolha: ", opcoes_validas)
			print("\n")
			resultado = self.processar_escolha(escolha)
			print("\n")
			if resultado == "SAIR":  
				# Se o submenu solicitou sair/voltar
				self.rodando = False
		# Fim do loop: se houver pai, retorno ao menu pai; se não, programa termina.

	#---- handlers ----
	def sair(self):
		sai = cli.sim_ou_nao("Deseja mesmo sair?")
		if sai:
			return "SAIR"

class MainMenu(MenuBase):
	def __init__(self, estado: Sinal):
		super().__init__(None, estado)  # Menu principal não tem pai
		self.titulo = "Problema 5 - Menu Principal"
		self.opcoes = {"P": ("Gerenciar sinais.", self.gerenciar),
			"X": ("Encerrar o programa.", self.sair)}

	def exibir(self):
		print(12 * "==" + " " + self.titulo + " " + 12 * "==" + "\n\n")
		super().exibir()

	#---- handlers ----
	def gerenciar(self):
		gerenciador = ManagerMenu(self, self.state)
		gerenciador.run()

class ManagerMenu(MenuBase):
	def __init__(self, parent: MainMenu, estado: Sinal):
		super().__init__(parent, estado)
		self.titulo = "Menu de Gerenciamento de Sinais"
		self.opcoes = {"L": ("Listar sinais.", self.listar),
			"F": ("Selecionar sinal.", self.focar),
			"D": ("Deletar sinal.", self.deletar),
			"X": ("Sair do menu.", self.sair)}

	def exibir(self):
		print(12 * "==" + " " + self.titulo + " " + 12 * "==" + "\n\n")
		super().exibir()

	#---- handlers ----
	def listar(self):
		print("Sinais\n")
		sinais_sort = io.lista_sinais()
		for nome in sinais_sort:
			if nome == self.state.nome_sinal and not self.state.isImage:
				print(f"\t--> {nome} <--")
			else:
				print(f"\t{nome}")

		print("Imagens\n")
		sinais_sort = io.lista_sinais(".pgm", True)
		for nome in sinais_sort:
			if nome == self.state.nome_sinal and self.state.isImage:
				print(f"\t--> {nome} <--")
			else:
				print(f"\t{nome}")
	
	def focar(self):
		self.state.isImage = cli.sim_ou_nao("Seu sinal é uma imagem?")
		nome_foca = input("\nDigite o nome do sinal que deseja analisar: ")

		extensao = ".txt"
		if self.state.isImage:
			extensao = ".pgm"

		existe, caminho = io.checa_arquivo(nome_foca, extensao, self.state.isImage)

		if existe:
			self.state.sinal, self.state.tempos, self.state.dt, self.state.n_pontos = ul.le_arquivo_sinal(caminho, self.state.isImage)
			self.state.nome_sinal = nome_foca
		else:
			print("\nNão existe nenhum sinal com esse nome.")

	def deletar(self):
		deleta_img = cli.sim_ou_nao("O sinal que você deseja deletar é uma imagem?")
		nome_apaga = input("Digite o nome do sinal que deseja excluir: ")

		extensao = ".pgm"
		if deleta_img:
			extensao = ".pgm"

		existe, caminho = io.checa_arquivo(nome_apaga, extensao, deleta_img)

		if not existe:
			print("\nNão existe nenhum sinal com esse nome.")
		else:
			io.deleta_arquivo(nome_apaga, extensao, deleta_img)

if __name__ == "__main__":
	sinal_selecionado = Sinal()
	menu = MainMenu(sinal_selecionado)
	menu.run()