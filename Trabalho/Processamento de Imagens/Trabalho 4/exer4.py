import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift, ifftshift
import imageio

# Carregar a imagem em escala de cinza
imagem = imageio.imread("Trabalho 4\\Input\\bird.pgm")

# Exibir a imagem original
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.show()

# Aplicar a Transformada de Fourier 2D
f_transform = fft2(imagem)
f_transform_shifted = fftshift(f_transform)

# Calcular o espectro de magnitude e normalizar
magnitude_spectrum = np.log(np.abs(f_transform_shifted) + 1)
magnitude_spectrum = 255 * magnitude_spectrum / np.max(magnitude_spectrum)

# Exibir o espectro de Fourier
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Espectro de Fourier')
plt.show()

# Desfazer o shift e aplicar a Transformada Inversa de Fourier
f_transform_unshifted = ifftshift(f_transform_shifted)
imagem_reconstruida = ifft2(f_transform_unshifted)
imagem_reconstruida = np.abs(imagem_reconstruida)

# Exibir a imagem reconstruída
plt.imshow(imagem_reconstruida, cmap='gray')
plt.title('Imagem Reconstruída')
plt.show()

# Calcular e exibir a diferença com a imagem original
diferenca = imagem - imagem_reconstruida
plt.imshow(diferenca, cmap='gray')
plt.title('Diferença entre a Imagem Original e a Reconstruída')
plt.show()

# Mostrar valores máximo e mínimo da diferença
print(f"Máximo: {np.max(diferenca)}, Mínimo: {np.min(diferenca)}")

# Remover todas as linhas ímpares do espectro de Fourier
f_transform_shifted[1::2, :] = 0

# Aplicar a Transformada Inversa de Fourier
f_transform_unshifted = ifftshift(f_transform_shifted)
imagem_reconstruida = ifft2(f_transform_unshifted)
imagem_reconstruida = np.abs(imagem_reconstruida)

# Exibir a imagem reconstruída
plt.imshow(imagem_reconstruida, cmap='gray')
plt.title('Imagem Reconstruída com Linhas Ímpares Removidas')
plt.show()

# Mostrar dimensão da imagem resultante
print(f"Dimensão da imagem resultante: {imagem_reconstruida.shape}")

# Zerar linhas alternadamente (5 zeradas, 5 mantidas)
rows = imagem.shape[0]
for i in range(0, rows, 10):
    f_transform_shifted[i:i+5, :] = 0

# Aplicar a Transformada Inversa de Fourier
f_transform_unshifted = ifftshift(f_transform_shifted)
imagem_reconstruida = ifft2(f_transform_unshifted)
imagem_reconstruida = np.abs(imagem_reconstruida)

# Exibir a imagem reconstruída
plt.imshow(imagem_reconstruida, cmap='gray')
plt.title('Imagem Reconstruída com Linhas Alternadamente Zeradas')
plt.show()

# Mostrar dimensão da imagem resultante
print(f"Dimensão da imagem resultante: {imagem_reconstruida.shape}")

# Zerar todas as linhas ímpares e colunas ímpares
f_transform_shifted[1::2, :] = 0
f_transform_shifted[:, 1::2] = 0

# Aplicar a Transformada Inversa de Fourier
f_transform_unshifted = ifftshift(f_transform_shifted)
imagem_reconstruida = ifft2(f_transform_unshifted)
imagem_reconstruida = np.abs(imagem_reconstruida)

# Exibir a imagem reconstruída
plt.imshow(imagem_reconstruida, cmap='gray')
plt.title('Imagem Reconstruída com Linhas e Colunas Ímpares Zeradas')
plt.show()

# Mostrar dimensão da imagem resultante
print(f"Dimensão da imagem resultante: {imagem_reconstruida.shape}")
