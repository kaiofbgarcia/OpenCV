import cv2
from cv2 import THRESH_BINARY
import numpy as np


imagem = cv2.imread("img/dadosVerdes1.png")          # Carregar a imagem
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)     # GrayScale
blur = cv2.blur(gray,(3,3))                       # Blur ###############

ret,binary = cv2.threshold(blur , 127 ,255, cv2.THRESH_BINARY)         # Binarização ################
ret1,binary1 = cv2.threshold(binary,127,255,cv2.THRESH_BINARY_INV)   # Inverter a Binarização

contours, hierarchy = cv2.findContours(binary1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Procura os Objetos
cont = len(contours)                                                                     # Conta os Objetos

cv2.drawContours(imagem, contours, -1, (0,255,0), 3) 

print("Resultado dos dados: ", cont)

cv2.imshow("Dilatation", imagem)

cv2.waitKey(0)
