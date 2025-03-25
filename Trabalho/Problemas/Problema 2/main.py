import useful_lib as ul
from pathlib import Path

#recebe os dados da biblioteca
def reseta_parametros():
	S_0 = ul.S_0
	omega = ul.omega
	T = ul.T
	dt = ul.dt
	n_pontos = ul.n_pontos
	return S_0, omega, T, dt, n_pontos

S_0, omega, T, dt, n_pontos = reseta_parametros() #cria as variáveis globais que serão usadas no programa
tempos = ul.cria_array_tempos(dt, n_pontos) 
sinal = ul.simula_sinal(tempos, omega, T, S_0)
nome_sinal = "std"

def print_parametros():
	global S_0, omega, T, dt, n_pontos

	print("Os parâmetros atuais são:")
	print(f"\t(1) S_0 = {S_0}\t(3) omega = {omega}\t(5) n_pontos = {n_pontos}")
	print(f"\t(2) T = {T}\t(4) dt = {dt}\t")

def menu_muda_sinal():
	global nome_sinal

	def print_menu():
		print("Você escolheu mudar o formato do sinal.")

		print("\nEscolha  sua opção: ")
		print("\tL: Lista todos os sinais acessíveis ao programa.\tA: Altera o sinal atual.")
		print("\tS: Salva o sinal atual em um arquivo.\t\t\tM: Mostra este menu novamente.")
		print("\tD: Deleta um sinal salvo.\t\t\t\tF: Muda o foco para outro sinal.")
		print("\tN: Cria um novo sinal.\t\t\t\t\tX: Sair deste menu.")

	print_menu()
	'''
	salvou = False
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

		elif escolha == "S":
			print("Você escolheu salvar o sinal em um arquivo.")
			nome_sinal = input("Digite o nome que deseja dar a este sinal: ")

			if nome_sinal == "std":
				print("Esse é o sinal padrão, e não pode ser alterado.")
				continue

			salva_sinal(sinal, tempos, nome_sinal)
			
			print("\nO sinal foi salvo com sucesso.")
			salvou = True
		
		elif escolha == "D":
			print("Você escolheu apagar um sinal.\n")
			nome_apaga = input("Digite o nome do sinal que deseja excluir: ")

			if nome_apaga == "std":
				print("Esse é o sinal padrão, e não pode ser excluído.")
				continue

			caminho = Path(f'Sinais/{nome_apaga}.txt')
			if caminho.exists():
				caminho.unlink()
				print("O sinal foi apagado.")
			else:
				print("Não existe nenhum sinal com esse nome.")
			
		elif escolha == "F":
			print("Você escolheu focar em outro sinal.\n")
			nome_foca = input("Digite o nome do sinal que deseja analisar: ")

			caminho = Path(f'Sinais/{nome_foca}.txt')
			if caminho.exists() and salvou:
				nome_sinal = nome_foca
				print("O foco foi alterado.")
			elif not salvou:
				print("Você tem alterações não salvas, tem certeza que deseja continuar? (y/n)")
				escolha2 = str(input()).capitalize()

				if escolha2 == "N":
					continue
				elif escolha2 == "Y":
					nome_sinal = nome_foca
					print("O foco foi alterado.")
			else:
				print("Não existe nenhum sinal com esse nome.")

		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			elif escolha2 == "Y" and salvou:
				break
			elif not salvou:
				print("Você tem alterações não salvas, tem certeza que deseja continuar? (y/n)")
				escolha3 = str(input()).capitalize()

				if escolha3 == "N":
					continue
				elif escolha3 == "Y":
					break
	'''
	print("\n")
	def print_menu():
		print("Você escolheu modificar os sinais.")
		
		print_parametros()

		print("\nEscolha sua opção: ")
		print("\t*: Digite um número de 1 a 5 para mudar o parâmetro correspondente.")
		print("\tH: Obter ajuda a respeito do que é cada parâmetro.\tR: Reseta os parâmetros para os originais.")
		print("\tM: Mostra este menu novamente.\t\t\t\tX: Sair deste menu.")

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
				omega = float(input("Digite o novo valor de omega: "))
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

			tempos = ul.cria_array_tempos(dt, n_pontos) 
			sinal = ul.simula_sinal(tempos, omega, T, S_0)
				
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
				break
		
		elif escolha == "F":
			print("Você escolheu focar em outro sinal.\n")
			nome_foca = input("Digite o nome do sinal que deseja analisar: ")

			caminho = Path(f'Sinais/{nome_foca}.txt')
			if caminho.exists():
				print(caminho)
				nome_sinal = nome_foca
				print("O foco foi alterado.")
			else:
				print("Não existe nenhum sinal com esse nome.")

def menu():
	global nome_sinal

	tempos, sinal = ul.le_arquivo_sinal(nome_sinal)

	def print_menu():
		print("Bem-vindo à resolução do Problema 1!") 
		print("Escolha sua opção: ")
		print("\tS: Mostra o sinal gerado.\tP: Modifica os sinais.")
		print("\tF: Mostra a FT do sinal.")
		print("\tM: Mostra este menu novamente.\tX: Termina o programa.")

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha == "S":
			ul.mostra_sinal(tempos, sinal)

		elif escolha == "P":
			print("\n")
			menu_muda_sinal()
			print("\n")
			print_menu()
		
		elif escolha == "F":
			ft = ul.aplica_FFT_em_sinal(sinal)
			frequencias = ul.cria_array_frequencias(tempos)
			ul.mostra_FT(frequencias, ft)

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