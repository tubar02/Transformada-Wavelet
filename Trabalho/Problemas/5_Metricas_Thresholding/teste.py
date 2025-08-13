import os

parte_antiga = input("Entre com a parte a ser trocada: ")
nova_parte = input("Entre com a troca: ")

pasta = '.\\Gráficos'

for nome in os.listdir(pasta):
	if parte_antiga in nome:
		novo_nome = nome.replace(parte_antiga, nova_parte)
		caminho_antigo = os.path.join(pasta, nome)
		caminho_novo = os.path.join(pasta, novo_nome)
		os.rename(caminho_antigo, caminho_novo)