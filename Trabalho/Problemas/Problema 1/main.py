import useful_lib

#inicialização dos dados
n_pontos = 2 ** 11 
with open("first_parameters.txt", "r") as valores_iniciais: #recebe os primeiros dados
	S_0 = valores_iniciais.readline().split()[2]
	omega = valores_iniciais.readline().split()[2]
	T = valores_iniciais.readline().split()[2]

def menu():
	print("Bem-vindo à resolução do Problema 1.") 
	print("Escolha sua opção: ")
	print("\tS: Mostra o sinal gerado.")

	escolha = str(input()).capitalize()

	print(escolha)

def main():
	menu()
	return 0

if __name__ == "__main__":
	main()