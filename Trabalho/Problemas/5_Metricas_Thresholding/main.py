import useful_lib as ul
import numpy as np
from pathlib import Path
from math import pi

nome_sinal = "std"
isImage = False

def mostrar_sinal(sinal, tempos, isImage):
	if isImage:
		ul.mostra_sinal(sinal, isImage=isImage)
	else:
		print("Como você deseja visualizar seu sinal?\n")
		print("\tr: Componente real.\ti: Componente imaginária.")
		print("\tri: Componentes real e imaginária.\tm: Módulo.\n")
		escolha = input("Entre com sua escolha: ").lower()
		ul.mostra_sinal(sinal, tempos, escolha)

def salvar_sinal(sinal, tempos):
	nome_sinal = input("Digite o nome que deseja dar a este sinal: ")

	if nome_sinal == "std":
		print("Esse é o sinal padrão, e não pode ser alterado.")
		return

	caminho = Path(f'Sinais/{nome_sinal}.txt')
	if caminho.exists():
		print("Você está prestes a sobrescrever um sinal, tem certeza? (y/n)")
		escolha3 = str(input()).capitalize()

		if escolha3 == "N":
			return

	ul.salva_sinal(sinal, tempos, nome_sinal)
			
	print("\nO sinal foi salvo com sucesso.")
	salvou = True
	return salvou

def menu_fourier(sinal, tempos, isImage):
	def print_menu():
		print("Você escolheu ver o sinal no domínio da frequência.\n")
		print("Escolha sua opção: ")
		print("\tF: Mostra a FT do sinal.\tR: Calcula e mostra o resíduo deste sinal com outro.")
		print("\tM: Mostra este menu novamente.\tX: Sai deste menu.")

	print_menu()

	while True:
		escolha = input("\nDigite sua escolha: ").capitalize()
		print("\n")

		if escolha == "F":
			print("Você escolheu visualizar o espectro deste sinal.\n")

			if isImage:
				ft = ul.aplica_FFT_em_sinal(sinal, True)
				ul.mostra_FT(ft, isImage=True)
					
			else:
				print("Como você deseja visualizar seu sinal transformado?\n")
				print("\tr: Componente real.\ti: Componente imaginária.")
				print("\tri: Componentes real e imaginária.\tm: Módulo.\n")

				escolha = input("Entre com sua escolha: ").lower()

				print("\nDeseja visualizar o espectro em ppm? (y/n)")

				escolha2 = input().lower()

				if escolha2 == "y":
					escolha2 = True
				else:
					escolha2 = False

				ft = ul.aplica_FFT_em_sinal(sinal)
				frequencias = ul.cria_array_frequencias(tempos)
				ul.mostra_FT(ft, frequencias, escolha, escolha2)

		elif escolha == "R":
			print("Você escolheu calcular o resíduo deste sinal.\n")

			print("Para isso, você deve entrar com o nome do sinal original.")
			nome_sinal = input("Entre com o nome do sinal original: ")
			caminho = Path(f'Sinais/{nome_sinal}.txt')

			if not caminho.exists():
				print("\nNão existe nenhum sinal com esse nome.")
				continue
			
			sinal_original, tempos_original, dt = ul.le_arquivo_sinal(caminho)
			ft_original = ul.aplica_FFT_em_sinal(sinal_original)
			frequencias_original = ul.cria_array_frequencias(tempos_original)
			ft = ul.aplica_FFT_em_sinal(sinal)

			print("\nComo você deseja visualizar seu resíduo?\n")
			print("\tr: Componente real.\ti: Componente imaginária.")
			print("\tri: Componentes real e imaginária.\tm: Módulo.\n")

			escolha = input("Entre com sua escolha: ").lower()

			print("\nDeseja visualizar o espectro em ppm? (y/n)")

			escolha2 = input().lower()

			if escolha2 == "y":
				escolha2 = True
			else:
				escolha2 = False

			ul.mostra_residuo(ft_original, frequencias_original, ft, escolha, escolha2)

		elif escolha == "M":
			print("\n")
			print_menu()
		
		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			else:
				break

def menu_wavelet(sinal, tempos, dt, isImage):
	print("Você escolheu visualizar a Transformada Wavelet do sinal.")

	def reseta_parametros():
		familia = "haar"
		level = 2
		return familia, level
	
	familia, level = reseta_parametros()
	coeficientes = ul.aplica_DTWT_em_sinal(sinal, familia, level, isImage)

	def print_parametros():
		nonlocal familia, level

		print("\nOs parâmetros atuais da WT são:")
		print(f"\tFamília: {familia}\t\tNível: {level}")
	
	def print_menu():
		print("\nDefina os parâmetros da sua Transformada Wavelet.")

		print_parametros()

		print("\nEscolha sua opção: ")
		print("\tF: Muda a família wavelet.\t\t\tL: Muda até que nível a transformada é calculada.")
		print("\tR: Reseta os parâmetros para os originais.\tS: Exibe o sinal transformado.")
		print("\tP: Filtra o sinal transformado.\t\t\tI: IDTWT do sinal filtrado.")
		print("\tM: Mostra este menu novamente.\t\t\tX: Sai deste menu.")

	print_menu()

	while True:
		escolha = input("\nDigite sua escolha: ").capitalize()
		print("\n")
		
		if escolha == "F":
			print("Você escolheu mudar a família wavelet.")

			print("\nEscolha sua família:")
			print("\tHaar: haar")
			print("\tDaubechies: dbN")
			print("\tSymlet: symN")
			print("\tCoiflet: coifN")
			print("N indica a ordem dos filtros.")

			familia = input("\nDigite sua escolha: ").lower()
			print_parametros()
			coeficientes = ul.aplica_DTWT_em_sinal(sinal, familia, level, isImage)

		elif escolha == "L":
			print("Você escolheu mudar até que nível sua transformada vai.")
			
			while(True):
				try:
					level = int(input("Entre com o nível: "))
					break
				except:
					print("\nO nível deve ser um valor inteiro.\n")
			print_parametros()
			coeficientes = ul.aplica_DTWT_em_sinal(sinal, familia, level, isImage)

		elif escolha == "R":
			print("Você escolheu resetar os parâmetros.")
			familia, level = reseta_parametros()
			print("Os parâmetros foram resetados.")
			print("\n")
			print_parametros()
			coeficientes = ul.aplica_DTWT_em_sinal(sinal, familia, level, isImage)

		elif escolha == "S":
			if isImage:
				print(f"Qual nível da transformada você quer visualizar? (1 a {level})")
				nivel = int(input())
				ul.mostra_WT(coeficientes, isImage = True, level=nivel)

			else:
				print("Como você deseja visualizar seu sinal transformado?\n")
				print("\tr: Componente real.\ti: Componente imaginária.")
				print("\tri: Componentes real e imaginária.\tm: Módulo.\n")

				escolha = input("Entre com sua escolha: ").lower()
				ul.mostra_WT(coeficientes, dt, escolha, isImage)

		elif escolha == "P":
			print("Você escolheu filtrar o sinal transformado.")
			escolha2 = input("\nVocê deseja usar o filtro original (O) (1D), hard thresholding (H) ou soft thresholding (S)?").upper()

			if escolha2 == "O":
				if isImage:
					print("Filtro não disponível para sinais 2D.")
					continue

				print("\nEste filtro funciona zerando todos os coeficientes de um nível a partir de um dado índice.")

				tamanho = len(sinal)

				print(f"Seu sinal original possui {tamanho} pontos.\n")

				if level == 1:
					entrada = f"Entre com o nível que deseja filtrar (1 para detalhe, ou 0 para aproximação): "
				else:
					entrada = f"Entre com o nível que deseja filtrar (1 a {level} para detalhe, ou 0 para aproximação): "

				nivel = int(input(entrada))

				if nivel != 0:
					nivel = nivel * (-1)

				indice = int(input(f"Entre com um índice de 0 a {len(coeficientes[nivel])} a partir do qual os coeficientes serão zerados: "))			
				
				coeficientes[nivel][indice::] = 0

				print("\nSeu sinal foi filtrado.")

			elif escolha2 == "H":
				original, _, _ = ul.le_arquivo_sinal(input("Entre com o caminho do sinal original: "), isImage)
				sigma = ul.snr(original, sinal, retorno = "sigma", isImage = isImage)
				limiar = ul.visu_shrink(sinal, sigma)
				coeficientes = ul.hard_thresholding(coeficientes, limiar, isImage)
				print("\nO sinal foi filtrado.")

			elif escolha2 == "F":
				pass

		elif escolha == "I":
			print("Você escolheu salvar a IDTWT em um arquivo.")
			
			if not isImage:
				sinal_rec = ul.aplica_IDTWT_em_sinal(coeficientes, familia, isImage)
				salvou = salvar_sinal(sinal_rec, tempos)
			else:
				caminho = "Imagens\\" + input("Entre com o que deseja dar ao sinal filtrado: ") + ".pgm"
				sinal_rec = ul.aplica_IDTWT_em_sinal(coeficientes, isImage = True, outputpath = caminho)

			print("Deseja visualizar o sinal reconstruído? (y/n)")

			escolha2 = input().capitalize()

			if escolha2 == "Y":
				print("\n")
				mostrar_sinal(sinal_rec, tempos, isImage)

		elif escolha == "M":
			print("\n")
			print_menu()

		elif escolha == "X":
			print("Você escolheu sair deste menu.")
			print("Tem certeza? (y/n)")

			escolha2 = str(input()).capitalize()

			if escolha2 == "N":
				continue
			else:
				break

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
					sinal_novo, tempos_novo, dt = ul.le_arquivo_sinal(caminho)
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
				dt = tempos[1] - tempos[0]
				return sinal, tempos, dt, salvou

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
					return sinal, tempos, dt
				else:
					tempos = ul.cria_array_tempos(dt, n_pontos) 
					sinal = ul.simula_sinal(tempos, omega, T, S_0)
					return sinal, tempos, dt

def menu_muda_sinal(sinal, tempos, dt):
	global nome_sinal, isImage

	salvou = True
	def print_menu():
		nonlocal salvou

		print("Você escolheu mudar o formato do sinal.")

		print("\nEscolha  sua opção: ")
		print("\tL: Lista todos os sinais acessíveis ao programa.\tA: Soma um sinal ao sinal com foco atual.")
		print("\tS: Salva o sinal atual em um arquivo.\t\t\tN: Cria um novo sinal unidimensional.")
		print("\tD: Deleta um sinal salvo.\t\t\t\tF: Muda o foco para outro sinal.")
		print("\tR: Adiciona ruído gaussiano a um sinal.\t\t\tC: Calcula a SNR entre um sinal ruidoso e o original.")
		print("\tM: Mostra este menu novamente.\t\t\t\tX: Sair deste menu.")
		print("Foco: ", nome_sinal)
		if not salvou:
			print("Você possui alterações não salvas!")

	print_menu()
	
	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")
		
		if escolha == "L":
			print("Você escolheu listar os sinais salvos.\n")

			pasta = Path('Sinais')
			print(pasta)
			for arquivo in pasta.iterdir():
				nome_arq = arquivo.name[:-4:]
				if nome_sinal == nome_arq and not isImage:
					print(f"\t--> {nome_arq} <--")
				else:
					print(f"\t{nome_arq}")

			pasta = Path('Imagens')
			print(pasta)
			for arquivo in pasta.iterdir():
				nome_arq = arquivo.name[:-4:]
				if nome_sinal == nome_arq and isImage:
					print(f"\t--> {nome_arq} <--")
				else:
					print(f"\t{nome_arq}")
		
		elif escolha == "A" and not isImage:
			sinal, tempos, dt, salvou = menu_adiciona(sinal, tempos)
			print_menu()
		elif escolha == "A" and isImage:
			print("Opção não válida para imagens.")

		elif escolha == "S" and not isImage:
			print("Você escolheu salvar o sinal em um arquivo.\n")
			salvou = salvar_sinal(sinal, tempos)
		elif escolha == "S" and isImage:
			print("Opção não válida para imagens.")
		
		elif escolha == "N":
			print("\n")
			sinal, tempos, dt = menu_cria_sinal(True)
			print("\n")
			print_menu()

		elif escolha == "D":
			print("Você escolheu apagar um sinal.\n")
			nome_apaga = input("Digite o nome do sinal que deseja excluir: ")

			caminho1 = Path(f'Sinais/{nome_apaga}.txt')
			caminho2 = Path(f'Imagens/{nome_apaga}.pgm')

			if caminho1.exists() and caminho2.exists():
				print("O seu sinal é uma imagem? (y/n)")
				aux = input().capitalize()
				if aux == "Y":
					caminho = caminho2
				else:
					caminho = caminho1
			elif caminho1.exists():
				caminho = caminho1
			elif caminho2.exists():
				caminho = caminho2
			else:
				print("\nNão existe nenhum sinal com esse nome.")
				continue

			if nome_apaga == "std":
				print("Esse é o sinal padrão, e não pode ser excluído.")
				continue

			caminho.unlink()
			print("\nO sinal foi apagado.")

			if nome_apaga == nome_sinal:
				nome_sinal = "std"
			
		elif escolha == "F":
			print("Você escolheu focar em outro sinal.\n")

			print("Seu sinal é uma imagem? (y/n)")
			isImage = input().capitalize()

			nome_foca = input("\nDigite o nome do sinal que deseja analisar: ")

			if isImage == "Y":
				isImage = True
				caminho = Path(f'Imagens/{nome_foca}.pgm')
			else:
				isImage = False
				caminho = Path(f'Sinais/{nome_foca}.txt')

			if caminho.exists() and salvou:
				nome_sinal = nome_foca
				if isImage:
					sinal, _, _ = ul.le_arquivo_sinal(caminho, True)
				else:
					sinal, tempos, dt = ul.le_arquivo_sinal(caminho)
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

		#MENU RUÍDO?????

		elif escolha == "R":
			print("Você escolheu adicionar ruído gaussiano a um sinal.")
			print("O ruído gaussiano é gerado a partir de uma função de densidade de probabilidade, definida como: ")
			print("\n\tP(x) = 1/(sigma * sqrt(2 * pi)) * exp(-((x - mu)^2)/(2 * sigma^2))")
			print("\nOnde mu indica a média, e sigma o desvio padrão.")

			snr_db = float(input("Entre com o valor da SNR desejada em dB: "))
			nome_salva = input("Entre com um nome para dar ao sinal ruidoso: ")

			if isImage:
				sinal_ruidoso = ul.adiciona_ruido(sinal, mode = "snr", param = snr_db, isImage = True, outputpath = f"Imagens/{nome_salva}.pgm")
			else:
				sinal_ruidoso = ul.adiciona_ruido(sinal, mode = "snr", param = snr_db)
				ul.salva_sinal(sinal_ruidoso, tempos, nome_salva)
			
			print("\nSinal ruidoso criado.")

		elif escolha == "C":
			print("Você escolheu calcular o SNR do sinal.")
			original, _, _ = ul.le_arquivo_sinal(input("Entre com o caminho do sinal original: "), isImage)
			snr = ul.snr(original, sinal, isImage = isImage)
			print(f"Esse sinal possui SNR de {snr}")

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
				if isImage:
					return sinal, None, None
				else:
					return sinal, tempos, dt
			elif not salvou:
				print("Você tem alterações não salvas, tem certeza que deseja continuar? (y/n)")
				escolha3 = str(input()).capitalize()

				if escolha3 == "N":
					continue
				elif escolha3 == "Y":
					if isImage:
						return sinal, None, None
					else:
						return sinal, tempos, dt

def menu():
	global nome_sinal

	sinal, tempos, dt = ul.le_arquivo_sinal(f"Sinais/{nome_sinal}.txt")

	def print_menu():
		print("Bem-vindo à resolução do Problema 5!") 
		print("Escolha sua opção: ")
		print("\tS: Mostra o sinal gerado.\tP: Modifica os sinais.")
		print("\tF: Trabalha com a FT do sinal.\tW: Trabalha com a WT do sinal.")
		print("\tM: Mostra este menu novamente.\tX: Termina o programa.")
		print("Foco: ", nome_sinal)

	print_menu()

	while True:
		escolha = str(input("\nDigite sua escolha: ")).capitalize()
		print("\n")

		if escolha == "S":
			print("Você escolheu ver o gráfico do sinal no domínio do tempo.")

			mostrar_sinal(sinal, tempos, isImage)

		elif escolha == "P":
			print("\n")
			sinal, tempos, dt = menu_muda_sinal(sinal, tempos, dt)
			print("\n")
			print_menu()
		
		elif escolha == "F":
			print("\n")
			menu_fourier(sinal, tempos, isImage)
			print("\n")
		
		elif escolha == "W":
			print("\n")
			menu_wavelet(sinal, tempos, dt, isImage)
			print("\n")

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