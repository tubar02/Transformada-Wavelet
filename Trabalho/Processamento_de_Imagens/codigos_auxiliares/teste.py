import numpy as np
from numpy.fft import fft2, ifft2, fftshift, ifftshift
import matplotlib.pyplot as plt
from math import log10
import my_image_lib_0_4 as img

n = 50

# Carregar imagem em escala de cinza
imagem = img.Image('Trabalho 4\\Input\\bird.pgm')

img.print_grayscale_image(imagem)

# Aplicar a transformada de Fourier
f_transform = fft2(imagem.pixels)
f_transform_shifted = fftshift(f_transform)

# Visualizar a transformada de Fourier
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)
valor = 255/log10(np.max(magnitude_spectrum))
magnitude_spectrum *= valor
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

# Aplicar filtragem (exemplo: zerar o centro)
rows, cols = len(imagem.pixels), len(imagem.pixels[0])
crow, ccol = rows // 2 , cols // 2
f_transform_shifted[crow-n:crow+n, ccol-n:ccol+n] = 0

# Visualizar a transformada de Fourier
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)
valor = 255/log10(np.max(magnitude_spectrum))
magnitude_spectrum = np.multiply(valor, magnitude_spectrum)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum after Filter')
plt.show()

# Transformada inversa
f_transform_filtered = ifftshift(f_transform_shifted)
inverse_transform = ifft2(f_transform_filtered)
inverse_image = np.absolute(inverse_transform)
inverse2 = np.real(inverse_transform)

# Visualizar a imagem filtrada
plt.imshow(inverse_image, cmap='gray', vmin=0, vmax=255)
plt.title('Imagem Filtrada')
plt.show()

# Visualizar a imagem filtrada
plt.imshow(inverse2, cmap='gray', vmin=0, vmax=255)
plt.title('Imagem Filtrada')
plt.show()

#Reaplica a transformada
fft_inver_image = fft2(inverse_image)
fft_inver_shift = fftshift(fft_inver_image)
magnitude_spectrum = np.log(np.abs(fft_inver_shift) + 1)
valor = 255/log10(np.max(magnitude_spectrum))
magnitude_spectrum *= valor
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

#Reaplica a transformada
fft_inver_image = fft2(inverse2)
fft_inver_shift = fftshift(fft_inver_image)
magnitude_spectrum = np.log(np.abs(fft_inver_shift) + 1)
valor = 255/log10(np.max(magnitude_spectrum))
magnitude_spectrum *= valor
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

teste = fft2(inverse_transform)
teste = np.absolute(teste)
teste = fftshift(teste)
magnitude_spectrum = np.log(np.abs(teste) + 1)
valor = 255/log10(np.max(magnitude_spectrum))
magnitude_spectrum *= valor
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()