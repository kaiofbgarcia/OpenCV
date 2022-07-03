import cv2
from cv2 import THRESH_BINARY
from cv2 import erode
import numpy as np
from numpy import binary_repr

imagem = cv2.imread("imgDados/dadosPilha2.jpg")          # Carregar a imagem
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)     # GrayScale
blur = cv2.blur(gray,(3,3))                       # Blur ###############

ret,binary = cv2.threshold(blur , 30 ,255, cv2.THRESH_BINARY)         # Binarização ################
ret1,binary1 = cv2.threshold(binary,127,255, cv2.THRESH_BINARY_INV)   # Inverter a Binarização

kernel = np.ones((5,5), np.uint8)                   # Erosão
erosion = cv2.erode(binary1, kernel, iterations=1)  # Erosão
dilation = cv2.dilate(erosion, kernel, iterations=1) #Dilatação

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Procura os Objetos
cont = len(contours)                                                                     # Conta os Objetos

cv2.imshow("Resize", imagem) # Printa sem o desenho 

cv2.drawContours(imagem, contours, -1, (0,255,0), 3)     # Desenha os Objetos

print("Resultado dos dados: ", cont)  # Mostra o resultado

cv2.imshow("Grayscale", gray)             # Mostra a imagem cinza
cv2.imshow("Blur", blur)                  # Mostra a imagem borrada
cv2.imshow("Threshold", binary)           # Mostra a imagem primeira binarização
cv2.imshow("Threshold Inv", binary1)      # Mostra a imagem segunda binarização
cv2.imshow("Erode", erosion)              # Mostra a imagem apos erosão
cv2.imshow("Dilatation", dilation)        # Mostra a imagem apos dilatação
cv2.imshow("Draw", imagem)                # Mostra a imagem(com o desenho já)

cv2.waitKey(0)
