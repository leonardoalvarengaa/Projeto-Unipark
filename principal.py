import cv2 #importanto a biblioteca opencv
import numpy as np
img = cv2.imread('C:\\Users\\dudaa\\OneDrive\\Documentos\\GitHub\\Projeto-Unipark\\IMAGENS\\Carros\\carro1.jpg') #criando uma variavel pra imagem e buscando ela

cv2.imshow('carro 1', img) #dando um nome de cabeçalho para a telinha que vai exibir a img e mostrando a imagem na tela

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #criando uma versao com cor da imagem em cinza pq n tem como reconhecer padroes nela colorida
#cv2.imshow('cinza', cinza)

#aqui o programa ate pode receber uma img colorida, mas ira utilizar a cinza
_, bin = cv2.threshold(cinza, 100, 255, cv2.THRESH_BINARY ) #definindo o limite o min ou max de preto e do branco e convertendo todas as cores para esse limite
#cv2.imshow('bin', bin)

#desfocando os ruídos e amplificando as formas geométricas
desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
#cv2.imshow('desfoque', desfoque)

#contornando a imagem
contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #conta cotorno dentro de contorno e aproxima tds os contornos, salvo na variavel cotornos

for c in contornos:
       perimetro = cv2.arcLength(c, True)
       aprox = cv2.approxPolyDP(c, 0.02 * perimetro, True)        
       if len(aprox) == 4:
            (x, y, altura, largura) = cv2.boundingRect(aprox)
            cv2.rectangle(img, (x, y), (x + altura, y + largura), (0, 255, 0), 2)
cv2.imshow("contornos", img)

#cv2.drawContours(img, contornos, -1, (0, 255, 0), 2)
#cv2.imshow('cont', img)


cv2.waitKey() #tirando a telinha com a img do loop infinito. esse comando mantém ela aberta ate que cliquemos em uma teclha ou fora dela
cv2.destroyAllWindows() #para garantir que as janelas sejam fechadas corretamente quando a execução do programa terminar
