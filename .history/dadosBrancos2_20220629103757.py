import cv2
from cv2 import THRESH_BINARY
from cv2 import erode
import numpy as np
from numpy import binary_repr

imagem = cv2.imread("img/dadosBrancos2.jpg")          # Carregar a imagem
res = cv2.resize(imagem, dsize=( 666, 444), interpolation=cv2.INTER_CUBIC) # Redimensionar Img ################
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)     # GrayScale
blur = cv2.blur(gray,(3,3))                       # Blur ###############

ret,binary = cv2.threshold(blur , 80 ,255, cv2.THRESH_BINARY)         # Binarização ################
ret1,binary1 = cv2.threshold(binary,127,255,cv2.THRESH_BINARY_INV)   # Inverter a Binarização

contours, hierarchy = cv2.findContours(binary1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Procura os Objetos
cont = len(contours)                                                                     # Conta os Objetos

cv2.drawContours(res, contours, -1, (0,255,0), 3) 

print("Resultado dos dados: ", cont)

cv2.imshow("Dilatation", res)

cv2.waitKey(0)
