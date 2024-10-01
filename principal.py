import cv2
import pytesseract
import json

# Tentando importar o arquivo JSON
with open('json.json', 'r') as f:
    dados_json = json.load(f)

# Lendo o arquivo TXT com coordenadas
with open('carro1.txt', 'r') as f:
    linhas = f.readlines()
    for linha in linhas:
        print(linha.strip())  # Exibe as coordenadas

# Carregar a imagem
img = cv2.imread('C:\\Users\\dudaa\\OneDrive\\Documentos\\GitHub\\Projeto-Unipark\\IMAGENS\\Carros\\carro1.jpg')
cv2.imshow('carro 1', img)  # Exibir a imagem original

# Converter para escala de cinza
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binarizar a imagem
_, bin = cv2.threshold(cinza, 120, 255, cv2.THRESH_BINARY)  # Ajuste o valor 120
cv2.imshow('Binarizada', bin)  # Exibir imagem binarizada

# Usar Canny para detectar bordas
bordas = cv2.Canny(bin, 50, 150)  # Ajuste os valores se necessário
cv2.imshow('Bordas', bordas)  # Exibir imagem de bordas

# Encontrar contornos
contornos, hier = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar retângulos em torno dos contornos encontrados
for c in contornos:
    perimetro = cv2.arcLength(c, True)
    aprox = cv2.approxPolyDP(c, 0.02 * perimetro, True)        
    if len(aprox) == 4:  # Verifica se é um quadrilátero
        (x, y, largura, altura) = cv2.boundingRect(aprox)
        cv2.rectangle(img, (x, y), (x + largura, y + altura), (0, 255, 0), 2)

# Mostrar a imagem final com os contornos
cv2.imshow("Contornos", img)

cv2.waitKey(0)  # Mantém a janela aberta até uma tecla ser pressionada
cv2.destroyAllWindows()  # Fecha todas as janelas
