"""Automate wavelet thresholding experiments on MRI image.

This script corrupts the MRI image with several SNR levels, applies
wavelet transforms using different families, performs hard and soft
thresholding and reconstructs the image. Intermediate images and
wavelet coefficient plots are saved with descriptive names, and the SNR
of the reconstructed images is stored in ``snr_results.csv`` for later
analysis.
"""

from pathlib import Path
import csv
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import useful_lib as ul

OUTPUT_DIR = Path("Gráficos")
IMAGE_DIR = Path("Imagens")

def save_image(img_obj, path, title):
	"""Salva um objeto ``Image`` como um PNG em escala de cinza com um título."""
	arr = np.asarray(img_obj.pixel())
	plt.figure()
	plt.imshow(arr, cmap="gray", vmin=0, vmax=255)
	plt.title(title)
	plt.axis("off")
	plt.savefig(path, bbox_inches="tight", pad_inches=0)
	plt.close()

def save_wavelet_level(wt_img, level, path, title):
	"""Salva o plot dos coeficientes wavelet para um nível específico do objeto ``Wavelet_Image``."""
	max_level = wt_img.level
	cA = wt_img.coef[0]
	detalhes = wt_img.coef[max_level - level + 1]
	cH, cV, cD = detalhes
	fig, axs = plt.subplots(1, 4, figsize=(12, 4))
	axs[0].imshow(np.abs(cA), cmap="gray")
	axs[0].set_title(f"Aproximação {max_level}")
	axs[1].imshow(np.abs(cH), cmap="gray")
	axs[1].set_title(f"Detalhe Horizontal {level}")
	axs[2].imshow(np.abs(cV), cmap="gray")
	axs[2].set_title(f"Detalhe Vertical {level}")
	axs[3].imshow(np.abs(cD), cmap="gray")
	axs[3].set_title(f"Detalhe Diagonal {level}")
	for ax in axs:
		ax.axis("off")
	plt.suptitle(title)
	plt.tight_layout()
	plt.savefig(path, bbox_inches="tight", pad_inches=0)
	plt.close(fig)

def main():
	OUTPUT_DIR.mkdir(exist_ok=True)
	IMAGE_DIR.mkdir(exist_ok=True)

	original, _, _ = ul.le_arquivo_sinal(IMAGE_DIR / "MRI.pgm", True)
	save_image(original, OUTPUT_DIR / "MRI_original.png", "MRI Original")

	snr_values = [7.5, 10, 12.5, 15, 17.5, 20]
	wavelets = ["haar", "db2", "sym2", "coif1"]
	level = 2
	methods = {"hard": ul.hard_thresholding, "soft": ul.soft_thresholding}

	results = []
	for snr_in in snr_values:
		nome_arquivo = f"MRI_{snr_in}dB"
		noisy_path = IMAGE_DIR / (nome_arquivo + ".pgm")
		noisy = ul.adiciona_ruido(original, mode="snr", param=snr_in,
								isImage=True, outputpath=str(noisy_path))
		save_image(noisy, OUTPUT_DIR / (nome_arquivo + ".png"),
				f"MRI {snr_in} dB")
		sigma = ul.snr(original, noisy, retorno="sigma", isImage=True)
		limiar = ul.visu_shrink(noisy, sigma, True)

		for wave in wavelets:
			wt = ul.aplica_DTWT_em_sinal(noisy, wave, level, True)
			for i in range(1, level + 1):
				save_wavelet_level(wt, i,
								OUTPUT_DIR / f"WT_{wave}_L{i}_{snr_in}dB_before.png",
								f"WT {wave} L{i} {snr_in}dB - Antes")
			for method_name, method in methods.items():
				wt_filtered = method(deepcopy(wt), limiar, True)

				for i in range(1, level + 1):
					save_wavelet_level(
						wt_filtered, i,
						OUTPUT_DIR / f"WT_{wave}_L{i}_{snr_in}dB_{method_name}.png",
						f"WT {wave} L{i} {snr_in}dB - {method_name}")
					
				rec_path = IMAGE_DIR / f"MRI_{snr_in}dB_{wave}_{method_name}.pgm"
				recon = ul.aplica_IDTWT_em_sinal(wt_filtered, isImage=True,
												outputpath=str(rec_path))
				save_image(
					recon,
					OUTPUT_DIR / f"MRI_{snr_in}dB_{wave}_{method_name}.png",
					f"Rec {wave} {method_name} {snr_in}dB")
				snr_out = ul.snr(original, recon, isImage=True)
				results.append([snr_in, wave, level, method_name, snr_out])

	with open("snr_results.csv", "w", newline="") as f:
		writer = csv.writer(f)
		writer.writerow(["input_snr_db", "wavelet_family", "level", "threshold", "output_snr_db"])
		writer.writerows(results)

if __name__ == "__main__":
	main()
	