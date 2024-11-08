# Rotação
rows, cols = imagem_binaria.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
imagem_rotacionada = cv2.warpAffine(imagem_binaria, M, (cols, rows))
cv2.imwrite('imagem_rotacionada.jpg', imagem_rotacionada)

# Realce de contraste
imagem_enhanced = cv2.equalizeHist(imagem_binaria)
cv2.imwrite('imagem_enhanced.jpg', imagem_enhanced)
