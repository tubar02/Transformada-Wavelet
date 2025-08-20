def pause(printa = "\n[Enter] para continuar..."):
	"""Pausa o fluxo do programa para receber uma entrada que não será usada."""
	try:
		lixo = input(printa)
	except EOFError:
		pass

def faz_escolha(pergunta: str, escolhas: list[str]) -> str:
	"""Lê string e valida contra um conjunto de opções (case-insensitive)."""
	escolhas = [escolha.upper() for escolha in sorted(escolhas)]
	while True:
		escolha = input(pergunta).strip().upper()
		if escolha in escolhas:
			return escolha
		
		print(f"\nOpção inválida. Válidas: {' | '.join(escolhas)}\n")

def sim_ou_nao(pergunta: str) -> bool:
	"""Lê resposta a pergunta de sim ou não, e retorna True ou False."""
	escolha = faz_escolha(pergunta + " (Y/N): ", ["Y", "N"])
	if escolha == "Y":
		return True
	return False

def pede_inteiro(pergunta: str, min: None | int = None, max: None | int = None) -> int:
	"""Lê e retorna um inteiro, a partir de uma pergunta para o usuário."""
	while True:
		try:
			x = int(input(pergunta).strip())
			if (min is not None and x < min) or (max is not None and x > max):
				print(f"Fora do intervalo [{min}, {max}].")
				continue
			return x
		except:
			print("Inteiro inválido.")

def main():
    pede_inteiro("Me dá um número entre 1 e 5: ", 1, 5)

if __name__ == "__main__":
    main()