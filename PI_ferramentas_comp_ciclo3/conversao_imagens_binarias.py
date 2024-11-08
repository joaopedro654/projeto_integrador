import cv2
import numpy as np

# Carregar imagem
imagem = cv2.imread('./image/cavalo44.jpg', 0)

# Converter para binária
_, imagem_binaria = cv2.threshold(imagem, 128, 255, cv2.THRESH_BINARY)

# Salvar imagem binária
cv2.imwrite('imagem_binaria.jpg', imagem_binaria)

# Rotação
rows, cols = imagem_binaria.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
imagem_rotacionada = cv2.warpAffine(imagem_binaria, M, (cols, rows))
cv2.imwrite('imagem_rotacionada.jpg', imagem_rotacionada)

# Realce de contraste
imagem_enhanced = cv2.equalizeHist(imagem_binaria)
cv2.imwrite('imagem_enhanced.jpg', imagem_enhanced)

imagem_suavizada = cv2.GaussianBlur(imagem_binaria, (5, 5), 0)
cv2.imwrite('imagem_suavizada.jpg', imagem_suavizada)
