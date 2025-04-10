import useful_lib as ul
import numpy as np
from pathlib import Path
from math import pi

nome_sinal = "std"

def menu_adiciona(sinal, tempos):
	def print_menu():
		print(f"Você escolheu adicionar um sinal ao sinal {nome_sinal}.")
		print("Como você deseja realizar a soma?\n")
		print("\tE: Soma os sinais atualmente salvos.\tN: Soma sinais novos.")
		print("\tM: Mostra esse menu novamente.\tX: Sair.")

	print_menu()
	salvou = True
	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha == "E":
			escolha2 = "Y"
			while escolha2 == "Y":
				print("\nVocê escolheu adicionar sinais existentes.")
				nome_adiciona = input(f"Entre com o nome do sinal que deseja somar a {nome_sinal}: ")
				print("\n")

				caminho = Path(f'Sinais/{nome_adiciona}.txt')
				if caminho.exists():
					sinal_novo, tempos_novo = ul.le_arquivo_sinal(nome_adiciona)
					salvou = False
				else:
					print("Esse sinal não existe. Tente novamente.\n")
					print_menu()
					continue

				sinal += sinal_novo
				assert np.array_equal(tempos, tempos_novo)	

				print("Deseja realizar uma nova soma? (y/n)")
				escolha2 = str(input()).capitalize()
				while escolha2 not in "YN":
					print("Por favor, digite somente \"y\" ou \"n\".")
					escolha2 = str(input()).capitalize()
		
		elif escolha == "N":
			escolha2 = "Y"
			while escolha2 == "Y":
				sinal_novo, tempos_novo = menu_cria_sinal()
				salvou = False

				sinal += sinal_novo
				assert np.array_equal(tempos, tempos_novo)	

				print("Deseja realizar uma nova soma? (y/n)")
				escolha2 = str(input()).capitalize()
				while escolha2 not in "YN":
					print("Por favor, digite somente \"y\" ou \"n\".")
					escolha2 = str(input()).capitalize()

		elif escolha == "M":
			print("\n")
			print_menu()

		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()
			while escolha2 not in "YN":
					print("Por favor, digite somente \"y\" ou \"n\".")
					escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			elif escolha2 == "Y":
				return sinal, tempos, salvou

def menu_cria_sinal(opcao_N = False):
	global nome_sinal

	def reseta_parametros():
		S_0 = ul.S_0
		omega = ul.omega
		T = ul.T
		dt = ul.dt
		n_pontos = ul.n_pontos
		return S_0, omega, T, dt, n_pontos

	S_0, omega, T, dt, n_pontos = reseta_parametros()

	def print_parametros():
		nonlocal S_0, omega, T, dt, n_pontos

		print("Os parâmetros atuais são:")
		print(f"\t(1) S_0 = {S_0}\t(3) omega = {omega}\t(5) n_pontos = {n_pontos}")
		print(f"\t(2) T = {T}\t(4) dt = {dt}\t")

	if opcao_N:
		def print_menu():
			print("Você escolheu criar um sinal novo.")
			
			print_parametros()

			print("\nEscolha sua opção: ")
			print("\t*: Digite um número de 1 a 5 para mudar o parâmetro correspondente.")
			print("\tH: Obter ajuda a respeito do que é cada parâmetro.\tR: Reseta os parâmetros para os originais.")
			print("\tM: Mostra este menu novamente.\t\t\t\tX: Salvar sinal criado.")
	else:
		def print_menu():
			print(f"Crie um sinal para que ele seja somado ao sinal {nome_sinal}.")
			
			print_parametros()

			print("\nEscolha sua opção: ")
			print("\t*: Digite um número de 1 a 5 para mudar o parâmetro correspondente.")
			print("\tH: Obter ajuda a respeito do que é cada parâmetro.\tR: Reseta os parâmetros para os originais.")
			print("\tM: Mostra este menu novamente.\t\t\t\tX: Somar este sinal.")

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha in "12345":
			if escolha == "1":
				print("Você escolheu mudar S_0.")
				S_0 = float(input("Digite o novo valor de S_0: "))
				print("\n")
				print_parametros()

			elif escolha == "2":
				print("\nVocê escolheu mudar T.")
				T = float(input("Digite o novo valor de T: "))
				print("\n")
				print_parametros()
				
			elif escolha == "3":
				print("Você escolheu mudar omega.")
				print("Entre com a frequência em Hz, que esta será automaticamente convertida em rad/s.")
				omega = float(input("Digite o novo valor de omega: ")) * (2 * pi)
				print("\n")
				print_parametros()
				
			elif escolha == "4":
				print("Você escolheu mudar dt.")
				dt = float(input("Digite o novo valor de dt: "))
				print("\n")
				print_parametros()
				
			elif escolha == "5":
				print("Você escolheu mudar n_pontos.")
				n_pontos = int(input("Digite o novo valor de n_pontos: "))
				print("\n")
				print_parametros()
				
		elif escolha == "H":
			print("Estes parâmetros controlam o comportamento do sinal simulado.")
			print("\tS_0: Indica a amplitude máxima do sinal.")
			print("\tT: Indica o tempo de relaxação.")
			print("\tomega: Indica a frequência de oscilação do sinal em rad/s.")
			print("\tdt: Indica o espaçamento em tempo entre os pontos usados pra gerar o sinal.")
			print("\tn_pontos: Indica quantos pontos serão usados para simular o sinal.")
			print("O sinal é gerado pela função: S(t) = S_o * exp(-t/T) * exp(i * omega * t)")
		
		elif escolha == "R":
			print("Você escolheu resetar os parâmetros.")
			S_0, omega, T, dt, n_pontos = reseta_parametros()
			print("Os parâmetros foram resetados.")
			print("\n")
			print_parametros()
		
		elif escolha == "M":
			print("\n")
			print_menu()

		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			elif escolha2 == "Y":
				if opcao_N:
					nome_sinal = input("\nEntre com o nome que deseja dar a esse sinal: ")

					caminho = Path(f'Sinais/{nome_sinal}.txt')
					if caminho.exists():
						print("Você está prestes a sobrescrever um sinal, tem certeza? (y/n)")
						escolha3 = str(input()).capitalize()

						if escolha3 == "N":
							print_menu()
							continue

					tempos = ul.cria_array_tempos(dt, n_pontos) 
					sinal = ul.simula_sinal(tempos, omega, T, S_0)
					ul.salva_sinal(sinal, tempos, nome_sinal)
					return sinal, tempos
				else:
					tempos = ul.cria_array_tempos(dt, n_pontos) 
					sinal = ul.simula_sinal(tempos, omega, T, S_0)
					return sinal, tempos

def menu_muda_sinal():
	global nome_sinal

	salvou = True
	def print_menu():
		nonlocal salvou

		print("Você escolheu mudar o formato do sinal.")

		print("\nEscolha  sua opção: ")
		print("\tL: Lista todos os sinais acessíveis ao programa.\tA: Soma um sinal ao sinal com foco atual.")
		print("\tS: Salva o sinal atual em um arquivo.\t\t\tN: Cria um novo sinal.")
		print("\tD: Deleta um sinal salvo.\t\t\t\tF: Muda o foco para outro sinal.")
		print("\tR: Adiciona ruído gaussiano a um sinal.")
		print("\tM: Mostra este menu novamente.\t\t\t\tX: Sair deste menu.")
		print("Foco: ", nome_sinal)
		if not salvou:
			print("Você possui alterações não salvas!")

	print_menu()
	
	sinal, tempos = ul.le_arquivo_sinal(nome_sinal)
	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")
		
		if escolha == "L":
			print("Você escolheu listar os sinais salvos.\n")

			pasta = Path('Sinais')

			for arquivo in pasta.iterdir():
				nome_arq = arquivo.name[:-4:]
				if nome_sinal == nome_arq:
					print(f"--> {nome_arq} <--")
				else:
					print(f"{nome_arq}")
		
		elif escolha == "A":
			sinal, tempos, salvou = menu_adiciona(sinal, tempos)
			print_menu()

		elif escolha == "S":
			print("Você escolheu salvar o sinal em um arquivo.\n")
			nome_sinal = input("Digite o nome que deseja dar a este sinal: ")

			if nome_sinal == "std":
				print("Esse é o sinal padrão, e não pode ser alterado.")
				continue

			caminho = Path(f'Sinais/{nome_sinal}.txt')
			if caminho.exists():
				print("Você está prestes a sobrescrever um sinal, tem certeza? (y/n)")
				escolha3 = str(input()).capitalize()

				if escolha3 == "N":
					continue

			ul.salva_sinal(sinal, tempos, nome_sinal)
			
			print("\nO sinal foi salvo com sucesso.")
			salvou = True
		
		elif escolha == "N":
			print("\n")
			sinal, tempos = menu_cria_sinal(True)
			print("\n")
			print_menu()

		elif escolha == "D":
			print("Você escolheu apagar um sinal.\n")
			nome_apaga = input("Digite o nome do sinal que deseja excluir: ")

			if nome_apaga == "std":
				print("Esse é o sinal padrão, e não pode ser excluído.")
				continue

			caminho = Path(f'Sinais/{nome_apaga}.txt')
			if caminho.exists():
				caminho.unlink()
				print("\nO sinal foi apagado.")

				if nome_apaga == nome_sinal:
					nome_sinal = "std"

			else:
				print("\nNão existe nenhum sinal com esse nome.")
			
		elif escolha == "F":
			print("Você escolheu focar em outro sinal.\n")
			nome_foca = input("Digite o nome do sinal que deseja analisar: ")

			caminho = Path(f'Sinais/{nome_foca}.txt')
			if caminho.exists() and salvou:
				nome_sinal = nome_foca
				sinal, tempos = ul.le_arquivo_sinal(nome_sinal)
				print("\nO foco foi alterado.")
			elif not salvou:
				print("Você tem alterações não salvas, tem certeza que deseja continuar? (y/n)")
				escolha2 = str(input()).capitalize()

				if escolha2 == "N":
					continue
				elif escolha2 == "Y":
					nome_sinal = nome_foca
					salvou = True
					print("O foco foi alterado.")
			else:
				print("\nNão existe nenhum sinal com esse nome.")

		elif escolha == "R":
			print("Você escolheu adicionar ruído gaussiano a um sinal.")
			print("O ruído gaussiano é gerado a partir de uma função de densidade de probabilidade, definida como: ")
			print("\n\tP(x) = 1/(sigma * sqrt(2 * pi)) * exp(-((x - mu)^2)/(2 * sigma^2))")
			print("\nOnde mu indica a média, e sigma o desvio padrão.")

			mu = float(input("\nEntre com o valor de mu: "))
			sigma = float(input("Entre com o valor de sigma: "))

			sinal_ruidoso = ul.adiciona_ruido_gauss(sinal, mu, sigma)
			
			print("\nSinal ruidoso criado.")
			nome_salva = input("Entre com um nome para dar ao sinal ruidoso: ")

			ul.salva_sinal(sinal_ruidoso, tempos, nome_salva)
			print("O sinal foi salvo.")

		elif escolha == "M":
			print("\n")
			print_menu()
		
		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			elif escolha2 == "Y" and salvou:
				return sinal, tempos
			elif not salvou:
				print("Você tem alterações não salvas, tem certeza que deseja continuar? (y/n)")
				escolha3 = str(input()).capitalize()

				if escolha3 == "N":
					continue
				elif escolha3 == "Y":
					return sinal, tempos

def menu():
	global nome_sinal

	sinal, tempos = ul.le_arquivo_sinal(nome_sinal)

	def print_menu():
		print("Bem-vindo à resolução do Problema 2!") 
		print("Escolha sua opção: ")
		print("\tS: Mostra o sinal gerado.\tP: Modifica os sinais.")
		print("\tF: Mostra a FT do sinal.")
		print("\tM: Mostra este menu novamente.\tX: Termina o programa.")
		print("Foco: ", nome_sinal)

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha == "S":
			print("Você escolheu ver o gráfico do sinal no domínio do tempo.")
			print("Como você deseja visualizar seu sinal?\n")
			print("\tr: Componente real.\ti: Componente imaginária.")
			print("\tri: Componentes real e imaginária.\tm: Módulo.\n")

			escolha = input("Entre com sua escolha: ").lower()

			ul.mostra_sinal(sinal, tempos, escolha)

		elif escolha == "P":
			print("\n")
			sinal, tempos = menu_muda_sinal()
			print("\n")
			print_menu()
		
		elif escolha == "F":
			print("Você escolheu ver o gráfico do sinal no domínio da frequência.")
			print("Como você deseja visualizar seu sinal transformado?\n")
			print("\tr: Componente real.\ti: Componente imaginária.")
			print("\tri: Componentes real e imaginária.\tm: Módulo.\n")

			escolha = input("Entre com sua escolha: ").lower()

			ft = ul.aplica_FFT_em_sinal(sinal)
			frequencias = ul.cria_array_frequencias(tempos)
			ul.mostra_FT(ft, frequencias, escolha)

		elif escolha == "M":
			print("\n")
			print_menu()

		elif escolha == "X":
			print("Você escolheu sair do programa.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			elif escolha2 == "Y":
				break

def main():
	print("\n")

	menu()

	print("\n")
	return 0

if __name__ == "__main__":
	main()