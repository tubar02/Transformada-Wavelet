import useful_lib as ul

#recebe os dados da biblioteca
S_0 = ul.S_0
omega = ul.omega
T = ul.T
dt = ul.dt
n_pontos = ul.n_pontos

def menu_muda_parametro():
	global S_0, omega, T, dt, n_pontos

	def print_menu():
		print("Você escolheu mudar os parâmetros do sinal.")
		print("Os parâmetros atuais são:")
		print(f"\t(1) S_0 = {S_0}\t(3) omega = {omega}\t(5) n_pontos = {n_pontos}")
		print(f"\t(2) T = {T}\t(4) dt = {dt}\t")

		print("\nEscolha sua opção: ")
		print("\t*: Digite um número de 1 a 5 para mudar o parâmetro correspondente.")
		print("\tH: Obter ajuda a respeito do que é cada parâmetro.\tX: Sair deste menu.")
		print("\tM: Mostra este menu novamente.")

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha == "1":
			print("Você escolheu mudar S_0.")
			S_0 = float(input("Digite o novo valor de S_0: "))

		elif escolha == "2":
			print("\nVocê escolheu mudar T.")
			T = float(input("Digite o novo valor de T: "))
			
		elif escolha == "3":
			print("Você escolheu mudar omega.")
			omega = float(input("Digite o novo valor de omega: "))
			
		elif escolha == "4":
			print("Você escolheu mudar dt.")
			dt = float(input("Digite o novo valor de dt: "))
			
		elif escolha == "5":
			print("Você escolheu mudar n_pontos.")
			n_pontos = int(input("Digite o novo valor de n_pontos: "))
		
		elif escolha == "M":
			print("\n")
			print_menu()
		
		elif escolha == "H":
			print("Estes parâmetros controlam o comportamento do sinal simulado.")
			print("\tS_0: Indica a amplitude máxima do sinal.")
			print("\tT: Indica o tempo de relaxação.")
			print("\tomega: Indica a frequência de oscilação do sinal.")
			print("\tdt: Indica o espaçamento em tempo entre os pontos usados pra gerar o sinal.")
			print("\tn_pontos: Indica quantos pontos serão usados para simular o sinal.")
			print("O sinal é gerado por uma função S(t) = S_o * exp(-t/T) * exp(i * omega * t)")

		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			elif escolha2 == "Y":
				break

def menu():
	global S_0, omega, T, dt, n_pontos

	def print_menu():
		print("Bem-vindo à resolução do Problema 1!") 
		print("Escolha sua opção: ")
		print("\tS: Mostra o sinal gerado.\tP: Modifica os parâmetros do sinal.")
		print("\tM: Mostra este menu novamente.\tX: Termina o programa.")

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha == "S":
			tempos = ul.cria_array_tempos(dt, n_pontos)
			sinal = ul.simula_sinal(tempos, omega, T, S_0)
			ul.mostra_sinal(tempos, sinal)

		elif escolha == "P":
			print("\n")
			menu_muda_parametro()
			print("\n")
			print_menu()

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