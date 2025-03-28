import useful_lib as ul

#recebe os dados da biblioteca
def reseta_parametros():
	S_0 = ul.S_0
	omega = ul.omega
	T = ul.T
	dt = ul.dt
	n_pontos = ul.n_pontos
	return S_0, omega, T, dt, n_pontos

S_0, omega, T, dt, n_pontos = reseta_parametros()

def print_parametros():
	global S_0, omega, T, dt, n_pontos

	print("Os parâmetros atuais são:")
	print(f"\t(1) S_0 = {S_0}\t(3) omega = {omega}\t(5) n_pontos = {n_pontos}")
	print(f"\t(2) T = {T}\t(4) dt = {dt}\t")

def menu_muda_parametro():
	global S_0, omega, T, dt, n_pontos

	def print_menu():
		print("Você escolheu mudar os parâmetros do sinal.")
		
		print_parametros()

		print("\nEscolha sua opção: ")
		print("\t*: Digite um número de 1 a 5 para mudar o parâmetro correspondente.")
		print("\tH: Obter ajuda a respeito do que é cada parâmetro.\tR: Reseta os parâmetros para os originais.")
		print("\tM: Mostra este menu novamente.\t\t\t\tX: Sair deste menu.")

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

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

def menu():
	global S_0, omega, T, dt, n_pontos

	def print_menu():
		print("Bem-vindo à resolução do Problema 1!") 
		print("Escolha sua opção: ")
		print("\tS: Mostra o sinal gerado.\tP: Modifica os parâmetros do sinal.")
		print("\tF: Mostra a FT do sinal.")
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
		
		elif escolha == "F":
			tempos = ul.cria_array_tempos(dt, n_pontos)
			sinal = ul.simula_sinal(tempos, omega, T, S_0)
			ft = ul.aplica_FFT_em_sinal(sinal)
			frequencias = ul.cria_array_frequencias(n_pontos, dt)
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