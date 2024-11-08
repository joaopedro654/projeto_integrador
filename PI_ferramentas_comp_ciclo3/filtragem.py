imagem_suavizada = cv2.GaussianBlur(imagem_binaria, (5, 5), 0)
cv2.imwrite('imagem_suavizada.jpg', imagem_suavizada)
