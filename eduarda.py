# Importa a biblioteca OpenCV para manipulação de imagens e vídeos
import cv2

# Importa a biblioteca NumPy, usada para manipulação de arrays numéricos
import numpy as np

# Carrega a imagem 'eduarda.jpg' em cores (RGB)
# O argumento 'cv2.IMREAD_COLOR' indica que a imagem será carregada com cores
img = cv2.imread('eduarda.jpg', cv2.IMREAD_COLOR)

# Cria uma janela chamada 'hello', onde a imagem será exibida
cv2.namedWindow('hello')

# Exibe a imagem carregada na janela 'hello'
cv2.imshow('hello', img)

# Aguarda até que uma tecla seja pressionada antes de fechar a janela
cv2.waitKey()
